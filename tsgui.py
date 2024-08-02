import os
import shutil
import psutil
import subprocess

input_dir = r"C:\Users\mario\Documents\switch data\JKSV"
destiny_dir = r"C:\Users\mario\Desktop\JKSV"

# obtain disk partitions
user_partitions = psutil.disk_partitions()

# filter all partitions to removable and FAT32/exFAT only
user_partitions_matches = []
for partition in user_partitions:
    # validate if it is a removable partition
    if "removable" in partition.opts:
        # validate partition's file system
        if "FAT32" in partition.fstype:
            user_partitions_matches.append(partition.mountpoint)
        elif "exFAT" in partition.fstype:
            user_partitions_matches.append(partition.mountpoint)
# prompt user to select origin SD
for partition in user_partitions_matches:
    print(partition)
chosen_origin_source = input("enter partition letter:")
# get folders from JKSV
folders = os.listdir(f"{chosen_origin_source}:\\JKSV")
# print total folders(games)
print("Total games:", len(folders))
# enumerate and print folders(games)
for i,folder in enumerate(folders):
    print(i+1,folder)
    # si es ls jksv marcarla par luego imprmir su contenido automaticamente
# get selected folder(game)
selected_folder = input("Choose a game:")
# remove extra number to match folder's index
selected_folder = int(selected_folder)-1
selected_game_name = folders[selected_folder]
print(folders[selected_folder])
action = input("c copy or d delete?:")
if action == "c":
    # get destiny's url path
    selected_destiny = input("select destiny folder:")
    destiny_dir = destiny_dir if selected_destiny == "" else selected_destiny
    print("seleted destiny route: ", destiny_dir)
    confirm_action = input("c confirm or ca cancel:")
    if confirm_action == "c":
        # build final origin's url path
        dir_origin = chosen_origin_source + ":\\JKSV\\" + selected_game_name
        # build final destiny's url path
        dir_destiny = destiny_dir + "\\" + selected_game_name
        # copy folder
        shutil.copytree(dir_origin, dir_destiny)
        print("game save data copied succesfully!")
    else:
        print("operation cancelled")
elif action == "d":
    confirm_action = input("c confirm or ca cancel:")
    print("folder deleted")
    print("thank you")
