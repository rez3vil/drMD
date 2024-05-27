## BASIC LIBS
import os
from os import path as p
import subprocess
from subprocess import run
import string
from shutil import copy
import time
## drMD UTILS
from pdbUtils import pdbUtils
from instruments import drFixer 
#####################################################################################

def prep_protocol(config):
    outDir = config["pathInfo"]["outputDir"]
    prepDir = p.join(outDir,"00_prep")
    prepLog = p.join(prepDir,"prep.log")

    os.makedirs(prepDir,exist_ok=True)

    ###### skip prep if complete ######
    amberParams = False
    inputCoords = False
    wholeDir = p.join(prepDir,"WHOLE")
    if p.isdir(p.join(wholeDir)):
        for file in os.listdir(wholeDir):
            if p.splitext(file)[1] == ".prmtop":
                amberParams = p.join(wholeDir,file)
            elif p.splitext(file)[1] == ".inpcrd":
                inputCoords = p.join(wholeDir,file)
            if p.splitext(file)[1] == ".pdb" and not file == "MERGED.pdb":
                pdbFile = p.join(wholeDir, file)
            
    if amberParams and inputCoords:
        return pdbFile, inputCoords, amberParams
    
    ### MAIN PREP PROTOCOL ###
    if "ligandInfo" in config:
        ## SPLIT INPUT PDB INTO PROT AND ONE FILE PER LIGAND
        inputPdb = config["pathInfo"]["inputPdb"]
        split_input_pdb(inputPdb =inputPdb,
                        config = config,
                        outDir=prepDir)
        ## PREPARE LIGAND PARAMETERS, OUTPUT LIGAND PDBS
        ligandPdbs,ligandFileDict = prepare_ligand_parameters(config = config, outDir = prepDir, prepLog = prepLog)
        ## PREPARE PROTEIN STRUCTURE
        proteinPdbs = prepare_protein_structure(config=config, outDir = prepDir, prepLog=prepLog)
        ## RE-COMBINE PROTEIN AND LIGAND PDB FILES
        wholePrepDir = p.join(prepDir,"WHOLE")
        os.makedirs(wholePrepDir,exist_ok=True)
        allPdbs = proteinPdbs + ligandPdbs
        outName = config["pathInfo"]["outputName"]
        mergedPdb = p.join(wholePrepDir,"MERGED.pdb")
        pdbUtils.mergePdbs(pdbList=allPdbs, outFile = mergedPdb)
        ## MAKE AMBER PARAMETER FILES WITH TLEAP
        inputCoords, amberParams = make_amber_params(outDir = wholePrepDir,
                            ligandFileDict=ligandFileDict,
                            pdbFile= mergedPdb,
                            outName= outName,
                            prepLog= prepLog)
        return mergedPdb, inputCoords, amberParams
    
    else:
        ## PREPARE PROTEIN STRUCTURE
        proteinPdbs = prepare_protein_structure(config=config, outDir = prepDir, prepLog = prepLog)  
        ## MERGE PROTEIN PDBS
        outName = config["pathInfo"]["outputName"]
        mergedPdb = p.join(p.join(prepDir,"PROT","MERGED.pdb"))
        pdbUtils.mergePdbs(pdbList=proteinPdbs, outFile = mergedPdb)
        ## MAKE AMBER PARAMETER FILES WITH TLEAP
        inputCoords, amberParams = make_amber_params(outDir = p.join(prepDir,"PROT"),
                                                        pdbFile= mergedPdb,
                                                        outName= outName,
                                                        prepLog = prepLog)
        return mergedPdb, inputCoords, amberParams

#####################################################################################
def find_ligand_charge(ligDf,ligName,outDir,pH):
    ## uses propka to identify charges on a ligand
    #make a temportaty pdb file from the ligand dataframe
    os.chdir(outDir)
    ligDf = pdbUtils.fix_atom_names(ligDf)
    tmpPdb = p.join(outDir,f"{ligName}.pdb")
    pdbUtils.df2pdb(ligDf,tmpPdb,chain=False)
    # run propka 
    proPkaCommand = f"propka3 {tmpPdb}"
    run_with_log(proPkaCommand,False,None)

    proPkaFile = f"{ligName}.pka"
    # read propka output to extract charge at specified pH
    with open(proPkaFile,"r") as f:
        pkaPredictions = []
        extract = False
        for line in f:
            if line.startswith("SUMMARY OF THIS PREDICTION"):
                extract = True
            if extract and line.startswith("-"):
                break
            if extract and not line =="\n":
                pkaPredictions.append(line.split())
        pkaPredictions = pkaPredictions[2:]
        totalCharge = 0
        for pred in pkaPredictions:
            if pred[-1][0] == "O":
                if float(pred[-2]) < pH:
                    totalCharge += -1
            elif pred[-1][0] == "N":
                if float(pred[-2]) > pH:
                    totalCharge += 1
    # clean up
    os.remove(tmpPdb)
    os.remove(proPkaFile)
    return totalCharge

#####################################################################################
def split_input_pdb(inputPdb,config,outDir):
    # read whole pdb into a df
    pdbDf = pdbUtils.pdb2df(inputPdb)
    # write each ligand to a separate pdb file
    ligandsDict = config["ligandInfo"]["ligands"]
    for ligand in ligandsDict:
        ligandName = ligand["ligandName"]
        ligPrepDir = p.join(outDir,ligandName)
        os.makedirs(ligPrepDir,exist_ok=True)
        ligDf = pdbDf[pdbDf["RES_NAME"]==ligandName]
        pdbUtils.df2pdb(ligDf,p.join(ligPrepDir,f"{ligandName}.pdb"),chain=False)
        pdbDf.drop(pdbDf[pdbDf["RES_NAME"]==ligandName].index,inplace=True)
    # write protein only to pdb file
    protPrepDir = p.join(outDir,"PROT")
    os.makedirs(protPrepDir,exist_ok=True)
    # ## deal with ions
    # ionResidues = ["FE2"]
    # ionDf = pdbDf[pdbDf["RES_NAME"].isin(ionResidues)]
    # pdbDf.drop(pdbDf[pdbDf["RES_NAME"].isin(ionResidues)].index,inplace=True)
    # if len(ionDf) > 0:
    #     pdbUtils.df2pdb(ionDf, p.join(protPrepDir,"IONS.pdb"))

    pdbUtils.df2pdb(pdbDf,p.join(protPrepDir,"PROT.pdb"))
#############################  PROTONATION & PDB CREATION ###############################
def ligand_protonation(ligand,ligPrepDir,ligandName,ligandPdbs, prepLog):
    if ligand["protons"]:
        ligPdb = p.join(ligPrepDir,f"{ligandName}.pdb")
        ligDf = pdbUtils.pdb2df(ligPdb)
        ligDf = pdbUtils.fix_atom_names(ligDf)
        pdbUtils.df2pdb(ligDf, ligPdb)
        rename_hydrogens(ligPdb, ligPdb)
        ligandPdbs.append(ligPdb)
        return ligPdb, ligandPdbs
    else:
        # # find pdb ligand pdb file
        ligPdb = p.join(ligPrepDir,f"{ligandName}.pdb")
        ligPdb_H = p.join(ligPrepDir,f"{ligandName}_H.pdb")
        obabelCommand = f"obabel {ligPdb} -O {ligPdb_H} -h"
        run_with_log(obabelCommand, prepLog,ligPdb_H)
        ligPdb_newH = p.join(ligPrepDir,f"{ligandName}_newH.pdb")
        rename_hydrogens(ligPdb_H,ligPdb_newH)
        # run pdb4amber to get compatable types and fix atom numbering
        ligPdb_amber = p.join(ligPrepDir,f"{ligandName}_amber.pdb")
        pdb4amberCommand = f"pdb4amber -i {ligPdb_newH} -o {ligPdb_amber}"
        run_with_log(pdb4amberCommand,prepLog,ligPdb_amber)
        ligPdb = ligPdb_amber
        ligandPdbs.append(ligPdb)
        return ligPdb, ligandPdbs
###############################  MOL2 CREATION #####################################
def  ligand_mol2(ligand,inputDir,ligandName,ligParamDir,ligPrepDir,ligPdb,ligFileDict, prepLog):
    ####  MOL2 CREATION ####
    # look for mol2 from config, then in ligParamDir, if not found, create new mol2
    if ligand["mol2"]:  # look in config
        ligMol2 = p.join(inputDir,f"{ligandName}.mol2")

    elif p.isfile(p.join(ligParamDir,f"{ligandName}.mol2")): # look in ligParamDir
        ligMol2 = p.join(ligParamDir,f"{ligandName}.mol2")
    else:  # convert to mol2 with antechamber
        charge = ligand["charge"]
        ligMol2 = p.join(ligPrepDir,f"{ligandName}.mol2")
        antechamberCommand = f"antechamber -i {ligPdb} -fi pdb -o {ligMol2} -fo mol2 -c bcc -s 2 -nc {charge}"
        run_with_log(antechamberCommand,prepLog,ligMol2)
        # copy to ligParamDir for future use
        copy(ligMol2,p.join(ligParamDir,f"{ligandName}.mol2"))
    # add mol2  path to ligFileDict 
    ligFileDict.update({"mol2":ligMol2})
    return ligMol2, ligFileDict
######################### TOPPAR CREATION ##########################################
def ligand_toppar(ligand,inputDir,ligandName,ligParamDir,ligPrepDir,ligMol2,ligFileDict, prepLog):
    # look for frcmod from config, then in ligParamDir, if not found, create new frcmod
    if ligand["toppar"]: # look in config
        ligFrcmod = p.join(inputDir,f"{ligandName}.frcmod") 
    elif p.isfile(p.join(ligParamDir,f"{ligandName}.frcmod")): # look in ligParamDir
        ligFrcmod = p.join(ligParamDir,f"{ligandName}.frcmod")    
    else :    # use mol2 to generate amber parameters with parmchk2
        ligFrcmod = p.join(ligPrepDir,f"{ligandName}.frcmod")
        parmchk2Command = f"parmchk2 -i {ligMol2} -f mol2 -o {ligFrcmod}"
        run_with_log(parmchk2Command,prepLog,ligFrcmod)
        copy(ligFrcmod,p.join(ligParamDir,f"{ligandName}.frcmod"))
    # add frcmod path to ligFileDict
    ligFileDict.update({"frcmod":ligFrcmod})

    return ligFileDict
#####################################################################################
def prepare_ligand_parameters(config, outDir, prepLog):
    # read inputs from config file
    ligandsDict = config["ligandInfo"]["ligands"]
    inputDir = config["pathInfo"]["inputDir"]
    mainDir = p.dirname(config["pathInfo"]["outputDir"])
    # create a dir to save parameter files in (saves re-running on subsequent runs)
    ligParamDir = p.join(mainDir,"01_ligand_parameters")
    os.makedirs(ligParamDir,exist_ok=True)
    # initialise list to store pdb files and dict to store all info
    ligandPdbs = []
    ligandFileDict = {}
    # for each ligand in config
    for ligand in ligandsDict:
        ligFileDict = {}
        # find files and directories
        ligandName = ligand["ligandName"]
        ligPrepDir = p.join(outDir,ligandName)
        os.chdir(ligPrepDir)

        ligPdb, ligandPdbs       = ligand_protonation(ligand,ligPrepDir,ligandName,ligandPdbs,prepLog)  

        ligMol2, ligFileDict    = ligand_mol2(ligand,inputDir,ligandName,ligParamDir,
                                              ligPrepDir,ligPdb,ligFileDict,prepLog)
        
        ligFileDict             =       ligand_toppar(ligand,inputDir,ligandName,ligParamDir,
                                                      ligPrepDir,ligMol2,ligFileDict,prepLog)

        ligandFileDict.update({ligandName:ligFileDict})
    return ligandPdbs, ligandFileDict
#####################################################################################
def rename_hydrogens(pdbFile,outFile):
    pdbDf = pdbUtils.pdb2df(pdbFile)
    hDf = pdbDf[pdbDf["ELEMENT"]=="H"]
    letters = list(string.ascii_uppercase)
    numbers = [str(i) for i in range(1,10)]
    newNameHs = []
    for letter in letters:
        for number in numbers:
            newNameHs.append("H"+letter+number)
    count = 0
    for index, row in hDf.iterrows():
        pdbDf.loc[index,"ATOM_NAME"] = newNameHs[count]
        count += 1
    pdbUtils.df2pdb(pdbDf,outFile,chain=False)
#####################################################################################
def prepare_protein_structure(config, outDir, prepLog):
    proteinDict = config["proteinInfo"]["proteins"]
    proteinPdbs = []
    # for each protein in config
    for protein in proteinDict:
        # find files and directories
        protPrepDir = p.join(outDir,"PROT")
        os.makedirs(protPrepDir,exist_ok=True)
        os.chdir(protPrepDir)
        protPdb = p.join(protPrepDir,"PROT.pdb")
        # check for PROT.pdb in protPrepDir (won't be there if noLigand)
        if not p.isfile(protPdb):
            copy(config["pathInfo"]["inputPdb"],protPdb)

        if not protein["protons"]:
            # print("adding protons to protein!")
            # # add protons with reduce
            # protPdb_h = p.join(protPrepDir,"PROT_h.pdb")
            # reduceCommand = f"reduce {protPdb} > {protPdb_h}"
            # run_with_log(reduceCommand,prepLog,protPdb_h)
            # proteinPdbs.append(protPdb_h)
            # openMM_pdb_fix(protPdb, protPdb_h)
            # proteinPdbs.append(protPdb_h) 
            print("nothing to do here!")
            #run pdb4amber to get compatable types and fix atom numbering
            # protPdb_amber = p.join(protPrepDir,"PROT_amber.pdb")
            # pdb4amberCommand = f"pdb4amber -i {protPdb_h} -o {protPdb_amber}"
            # run_with_log(pdb4amberCommand,prepLog,protPdb_amber)
        proteinPdbs.append(protPdb)
    
    return proteinPdbs


#####################################################################################
def make_amber_params(outDir, pdbFile, outName,prepLog,ligandFileDict=False):
    os.chdir(outDir)
    # write tleap input file
    tleapInput = p.join(outDir, "TLEAP.in")
    with open(tleapInput,"w") as f:
        # amber ff and tip3p ff
        f.write("source oldff/leaprc.ff14SB\n")
        f.write("source leaprc.gaff2\n")
        f.write("source leaprc.water.tip3p\n\n")
        ## ions ff
        f.write("loadamberparams frcmod.ions1lm_126_tip3p\n")
        f.write("loadamberparams frcmod.ions234lm_126_tip3p\n")

        if ligandFileDict:
            ## ligand mol2 and ff
            for ligandName in ligandFileDict:
                ligMol2 = ligandFileDict[ligandName]["mol2"]
                ligFrcmod = ligandFileDict[ligandName]["frcmod"]
                f.write(f"{ligandName} = loadmol2 {ligMol2}\n")
                f.write(f"loadamberparams {ligFrcmod}\n\n")

        ## whole protein structure
        f.write(f"mol = loadpdb {pdbFile}\n")
        # solvation and ions
        f.write("solvatebox mol TIP3PBOX 10.0\n")
        f.write("addions mol Na+ 0\n")
        f.write("addions mol Cl- 0\n")
        # save solvated pdb file
        solvatedPdb = f"{outName}.pdb"
        f.write(f"savepdb mol {solvatedPdb}\n")
        # save parameter files
        prmTop = p.join(outDir,f"{outName}.prmtop")
        inputCoords =  p.join(outDir,f"{outName}.inpcrd")
        f.write(f"saveamberparm mol {prmTop} {inputCoords}\n")
        f.write("quit\n")

    tleapOutput = p.join(outDir,"TLEAP.out")
    amberParams = p.join(outDir, f"{outName}.prmtop")
    tleapCommand = f"tleap -f {tleapInput} > {tleapOutput}"
    run_with_log(tleapCommand,prepLog,amberParams)

    inputCoords = p.join(outDir, f"{outName}.inpcrd")
    ## reset chain and residue IDs in amber PDB
    solvatedPdb = p.join(outDir,solvatedPdb)
    drFixer.reset_chains_residues(pdbFile, solvatedPdb)
    return inputCoords, amberParams
#####################################################################################
def run_with_log(command, prepLog, expectedOutput):
    maxRetries = 5
    retries = 0

    while retries < maxRetries:
        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if prepLog:
            with open(prepLog, "a") as log:
                log.write(process.stdout)
        if expectedOutput is None or p.isfile(expectedOutput):
            return
        else:
            print(f"Expected output:\n\t {expectedOutput}\n\t\t not found. Retrying...")
            retries += 1
            time.sleep(5)
    print("Maximum retries reached. Exiting...")

#####################################################################################