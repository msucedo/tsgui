import os
import shutil

input_dir = r"C:\Users\mario\Documents\switch data\JKSV"
destiny_dir = r"C:\Users\mario\Desktop\JKSV"


# prompt user for origin folder
chosen_origin_folder = input("enter a folder's route:")
input_dir = input_dir if chosen_origin_folder == "" else chosen_origin_folder
print("selected route: ", input_dir)
# get folders from JKSV
folders = os.listdir(input_dir)
# print total folders(games)
print("Total games:", len(folders))
# print folders(games)
for i,folder in enumerate(folders):
    print(i+1,folder)
# get selected folder(game)
selected_folder = input("Choose a game:")
# remove extra number to match folder's index
selected_folder = int(selected_folder)-1
selected_game_name = folders[selected_folder]
print(folders[selected_folder])
action = input("c copy or d delete?:")
if action == "c":
    selected_destiny = input("select destiny folder:")
    destiny_dir = destiny_dir if selected_destiny == "" else selected_destiny
    print("seleted destiny route: ", destiny_dir)
    confirm_action = input("c confirm or ca cancel:")
    if confirm_action == "c":
        dir_origin = input_dir + "\\" + selected_game_name
        dir_destiny = destiny_dir + "\\" + selected_game_name
        shutil.copytree(dir_origin, dir_destiny)
        print("game save data copied succesfully!")
    else:
        print("operation cancelled")
elif action == "d":
    confirm_action = input("c confirm or ca cancel:")
    print("folder deleted")
    print("thank you")
