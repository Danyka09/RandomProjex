# This is a program for linking the default .minecraft to Prism instances
# we use mklink to link them; del for deleting files; rmdir or rd to remove folders
# ctrl + shift + L   to select all occurrences of a word
import os, ctypes, sys
from pathlib import Path

# okay this is ai help on relative paths, can think about implementing
# Path.home() / "AppData" / "Roaming" / ".minecraft"

def main():
    # the full paths; i know its not relative idk what its called but whatever idc to do it right now
    # minecraft_path = r"C:\Users\dsebo\AppData\Roaming\.minecraft"
    minecraft_path = Path.home() / "AppData" / "Roaming" / ".minecraft" #claude
    instance_name= input("Please enter the exact instance name: ")
    prism_path = Path.home() / "AppData" / "Roaming" / "PrismLauncher" / "instances" / instance_name / "minecraft" #claude
    # prism_path = rf"C:\Users\dsebo\AppData\Roaming\PrismLauncher\instances\{instance_name}\minecraft"

    # the specific commands
    link_folders = r"mklink /J"
    link_file = r"mklink"
    remove_folders = r"rmdir" #be careful with these
    remove_file = r"del"

    #the specific paths
    saves = r"\saves"
    screenshots = r"\screenshots"
    resourcepacks = r"\resourcepacks"
    shaderpacks = r"\shaderpacks"
    servers = r"\servers.dat"

    # deletion
    os.system(f'{remove_file} "{prism_path}{servers}"')
    os.system(f'{remove_folders} "{prism_path}{saves}"')
    os.system(f'{remove_folders} "{prism_path}{screenshots}"')
    os.system(f'{remove_folders} "{prism_path}{resourcepacks}"')
    os.system(f'{remove_folders} "{prism_path}{shaderpacks}"')

    # the commands for linking
    servers_command = f'{link_file} "{prism_path}{servers}" "{minecraft_path}{servers}"'
    saves_command = f'{link_folders} "{prism_path}{saves}" "{minecraft_path}{saves}"'
    screenshots_command = f'{link_folders} "{prism_path}{screenshots}" "{minecraft_path}{screenshots}"'
    resourcepacks_command = f'{link_folders} "{prism_path}{resourcepacks}" "{minecraft_path}{resourcepacks}"'
    shaderpacks_command = f'{link_folders} "{prism_path}{shaderpacks}" "{minecraft_path}{shaderpacks}"'
    # i have come to realise the variables were unnecesary but we keeping them
    os.system(servers_command)
    os.system(saves_command)
    os.system(screenshots_command)
    os.system(resourcepacks_command)
    os.system(shaderpacks_command)

#this stuff is copied, i do not understand what the hell this is but its necessary for admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    main()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, '"' + " ".join(sys.argv) + '"', None, 1)

input()
