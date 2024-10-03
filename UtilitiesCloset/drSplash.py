## BASIC PYTHON LIBRARIES
from subprocess import run
import textwrap

##  CLEAN CODE
from typing import Optional

###########################################################################################

def print_drMD_logo() -> None:
    """
    Prints the DRMD logo.

    Returns:
        None
    """
    run(["clear"])
    tealColor = "\033[38;5;37m" 
    resetTextColor = "\033[0m"
    print(tealColor+
          """
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕
            dddddddd                                                                       
            d::::::d                   MMMMMMMM               MMMMMMMMDDDDDDDDDDDDD         
            d::::::d                   M:::::::M             M:::::::MD::::::::::::DDD     
            d::::::d                   M::::::::M           M::::::::MD:::::::::::::::DD   
            d:::::d                    M:::::::::M         M:::::::::MDDD:::::DDDDD:::::D  
    ddddddddd:::::drrrrr   rrrrrrrrr   M::::::::::M       M::::::::::M  D:::::D    D:::::D 
  dd::::::::::::::dr::::rrr:::::::::r  M:::::::::::M     M:::::::::::M  D:::::D     D:::::D
 d::::::::::::::::dr:::::::::::::::::r M:::::::M::::M   M::::M:::::::M  D:::::D     D:::::D
d:::::::ddddd:::::drr::::::rrrrr::::::rM::::::M M::::M M::::M M::::::M  D:::::D     D:::::D
d::::::d    d:::::d r:::::r     r:::::rM::::::M  M::::M::::M  M::::::M  D:::::D     D:::::D
d:::::d     d:::::d r:::::r     rrrrrrrM::::::M   M:::::::M   M::::::M  D:::::D     D:::::D
d:::::d     d:::::d r:::::r            M::::::M    M:::::M    M::::::M  D:::::D     D:::::D
d:::::d     d:::::d r:::::r            M::::::M     MMMMM     M::::::M  D:::::D    D:::::D 
d::::::ddddd::::::ddr:::::r            M::::::M               M::::::MDDD:::::DDDDD:::::D  
 d:::::::::::::::::dr:::::r            M::::::M               M::::::MD:::::::::::::::DD        
  d:::::::::ddd::::dr:::::r            M::::::M               M::::::MD::::::::::::DDD     
   ddddddddd   dddddrrrrrrr            MMMMMMMM               MMMMMMMMDDDDDDDDDDDDD

⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕
                    Molecular Dynamics: Just what the Doctor Ordered!
    """
    +resetTextColor)
###########################################################################################
def print_prep_failed(errorMessage: str, stepName) -> None:
    redText = "\033[31m"
    yellowText = "\033[33m"
    resetTextColor = "\033[0m"


    wrappedErrorMessage = textwrap.fill(str(errorMessage), 80).replace("\n", "\n\t")

    print(redText+
          f"""
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕

    ██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗    
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║    
    ██████╔╝██████╔╝█████╗  ██████╔╝███████║██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║    
    ██╔═══╝ ██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║    
    ██║     ██║  ██║███████╗██║     ██║  ██║██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║    
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    

        ███████╗████████╗███████╗██████╗     ███████╗ █████╗ ██╗██╗     ███████╗██████╗        
        ██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗       
        ███████╗   ██║   █████╗  ██████╔╝    █████╗  ███████║██║██║     █████╗  ██║  ██║       
        ╚════██║   ██║   ██╔══╝  ██╔═══╝     ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║       
        ███████║   ██║   ███████╗██║         ██║     ██║  ██║██║███████╗███████╗██████╔╝       
        ╚══════╝   ╚═╝   ╚══════╝╚═╝         ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝  
        At step {yellowText}{stepName}{redText}
        With Error:
        {yellowText}{wrappedErrorMessage}{redText}

        Please check the preparation log file for further details
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕{resetTextColor}
""")

    exit(1)

###########################################################################################


def print_performing_first_aid() -> None:
    
    yellowText = "\033[33m"
    resetTextColor = "\033[0m"

    print(yellowText+
          """
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕

       ██████  ███████ ██████  ███████  ██████  ██████  ███    ███ ██ ███    ██  ██████  
       ██   ██ ██      ██   ██ ██      ██    ██ ██   ██ ████  ████ ██ ████   ██ ██       
       ██████  █████   ██████  █████   ██    ██ ██████  ██ ████ ██ ██ ██ ██  ██ ██   ███ 
       ██      ██      ██   ██ ██      ██    ██ ██   ██ ██  ██  ██ ██ ██  ██ ██ ██    ██ 
       ██      ███████ ██   ██ ██       ██████  ██   ██ ██      ██ ██ ██   ████  ██████  
  
                 ███████ ██ ██████  ███████ ████████      █████  ██ ██████  
                 ██      ██ ██   ██ ██         ██        ██   ██ ██ ██   ██ 
                 █████   ██ ██████  ███████    ██        ███████ ██ ██   ██ 
                 ██      ██ ██   ██      ██    ██        ██   ██ ██ ██   ██ 
                 ██      ██ ██   ██ ███████    ██        ██   ██ ██ ██████  
                                                           
                             Your simulation has crashed...
                             drMD will attempt to rescue it...
         You may need to adjust your simulation parameters in your config file!
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕
          """
          +resetTextColor)
    

def print_first_aid_failed(errorOpenMM) -> None:
    """
    Prints the first aid failed message.

    Returns:    
        None
    """ 
    redText = "\033[31m"
    yellowText = "\033[33m"

    resetTextColor = "\033[0m"

    print(redText+
          f"""
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕

            ███████ ██ ██████  ███████ ████████      █████  ██ ██████  
            ██      ██ ██   ██ ██         ██        ██   ██ ██ ██   ██ 
            █████   ██ ██████  ███████    ██        ███████ ██ ██   ██ 
            ██      ██ ██   ██      ██    ██        ██   ██ ██ ██   ██ 
            ██      ██ ██   ██ ███████    ██        ██   ██ ██ ██████  
                                                                    
                                                                    
                ███████  █████  ██ ██      ███████ ██████              
                ██      ██   ██ ██ ██      ██      ██   ██             
                █████   ███████ ██ ██      █████   ██   ██             
                ██      ██   ██ ██ ██      ██      ██   ██             
                ██      ██   ██ ██ ███████ ███████ ██████

        drMD failed to rescue your simulation.
        The following error was returned by OpenMM:

        {yellowText}{errorOpenMM}{redText}

        This is likely due to unphysically high energies in your simulation.
    
        Try some of the following:
        -> reduce the timestep of your simulation
        -> reduce the temperature of your simulation
        -> if you are using any restraints, reduce their force constants

⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕
                                                          
"""
+resetTextColor)
    


###########################################################################################
def print_config_error(configDisorders) -> None:
    """
    Prints an error message indicating that the config file was not found.

    Returns:
        None
    """
    redText = "\033[31m"
    yellowText = "\033[33m"
    orangeText = "\033[38;5;208m"
    greenText = "\033[32m"
    resetTextColor = "\033[0m"


    print(redText+
          """
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕
          
 ▄████▄  ▒█████   ███▄    █   █████▒██▓ ▄████    ▓█████  ██▀███   ██▀███   ▒█████   ██▀███  
▒██▀ ▀█ ▒██▒  ██▒ ██ ▀█   █ ▓██   ▒▓██▒██▒ ▀█▒   ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
▒▓█    ▄▒██░  ██▒▓██  ▀█ ██▒▒████ ░▒██▒██░▄▄▄░   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
▒▓▓▄ ▄██▒██   ██░▓██▒  ▐▌██▒░▓█▒  ░░██░▓█  ██▓   ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  
▒ ▓███▀ ░ ████▓▒░▒██░   ▓██░░▒█░   ░██░▒▓███▀▒   ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
░ ░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒ ░   ░▓  ░▒   ▒    ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░  ▒    ░ ▒ ▒░ ░ ░░   ░ ▒░ ░      ▒ ░ ░   ░     ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
░       ░ ░ ░ ▒     ░   ░ ░  ░ ░    ▒ ░ ░   ░       ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ 
░ ░         ░ ░           ░         ░       ░       ░  ░   ░        ░         ░ ░     ░     
░          
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕
          """)
    print(f"{resetTextColor}The following disorders have been found in your config file:")    
    print(f"{resetTextColor}Colour Key: | {greenText}Input Correct{resetTextColor} | {orangeText}Non Fatal, Default Used{resetTextColor} | {redText}Fatal Issue{resetTextColor} |")    


    for infoName, infoDisorders in configDisorders.items():
        if infoDisorders is None:
            continue
        print(f"For the config entry {yellowText}{infoName}{resetTextColor}, the following problems were found:")
        for argName, argDisorder in infoDisorders.items():
            if argDisorder is None:
                print(f"\t{yellowText}{argName}: {greenText}Input Correct!{resetTextColor}")
            elif isinstance(argDisorder, str):
                if "default" in argDisorder.lower():
                    print(f"\t{yellowText}{argName}: {orangeText}{argDisorder}{resetTextColor}")
                else:
                    print(f"\t{yellowText}{argName}: {redText}{argDisorder}{resetTextColor}")

            elif isinstance(argDisorder, list):
                print(f"\t{yellowText}{argName}: {redText}{argDisorder}{resetTextColor}")
            elif isinstance(argDisorder, dict):
                print(f"in sub-entry {yellowText}{argName}{resetTextColor}:")
                for actualArgName, actualArgDisorder in argDisorder.items():
                    if actualArgDisorder is None:
                            print(f"\t{yellowText}{actualArgName}: {greenText}Input Correct!{resetTextColor}")
                    elif isinstance(actualArgDisorder, str):
                        print(f"\t{yellowText}{actualArgName}: {redText}{actualArgDisorder}{resetTextColor}")
                    elif isinstance(actualArgDisorder, list):
                        print(f"\t{yellowText}{actualArgName}: {redText}{actualArgDisorder}{resetTextColor}")

    print(resetTextColor)
    exit(1)
###########################################################################################
def print_pdb_error() -> None:
    """
    Prints an error message indicating that problems have been found in the pdb files

    Returns:
        None
    """
    redText = "\033[31m"
    resetTextColor = "\033[0m"


    print(redText+
          """
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕

            ██▓███  ▓█████▄  ▄▄▄▄      ▓█████  ██▀███   ██▀███   ▒█████   ██▀███  
            ▓██░  ██▒▒██▀ ██▌▓█████▄    ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
            ▓██░ ██▓▒░██   █▌▒██▒ ▄██   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
            ▒██▄█▓▒ ▒░▓█▄   ▌▒██░█▀     ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  
            ▒██▒ ░  ░░▒████▓ ░▓█  ▀█▓   ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
            ▒▓▒░ ░  ░ ▒▒▓  ▒ ░▒▓███▀▒   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
            ░▒ ░      ░ ▒  ▒ ▒░▒   ░     ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
            ░░        ░ ░  ░  ░    ░       ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ 
                        ░     ░            ░  ░   ░        ░         ░ ░     ░     
⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕⚕
          """
          +resetTextColor)
###########################################################################################



if __name__ == "__main__":
    print_drMD_logo()
    print_config_error()
    print_pdb_error()
    print_performing_first_aid()
  