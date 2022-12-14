from prettytable import PrettyTable
import numpy as np
from random import randint
import pandas
import pytest
from requests import get
from plantclass import Plant
from plantclass import userPlant
import os

os.system("clear")

# Prettytable collumn header pre-filled.
your_table = PrettyTable(['Your Plant Collection 🌱',])

# Variable defined as an empty list for appending plant names for user collection.
program_plant_name_list = []

# Variable defined as an empty list for appending the data associated to each plant in users collection.
program_plant_data_list = []

# Introduction to the app, explaining usecase.
print(r"""  
             __                   __                                   
    ____    / /  ____ _   ____   / /_         ____ _    ____     ____   
   / __ \  / /  / __ `/  / __ \ / __/        / __ `/   / __ \   / __ \ 
  / /_/ / / /  / /_/ /  / / / // /_         / /_/ /   / /_/ /  / /_/ / _
 / .___/ /_/   \__,_/  /_/ /_/ \__/         \__,_/   / .___/  / .___/ (_)
/_/                                                 /_/      /_/

""")

def introduction():
    print("\n\nWelcome to PLANTAPP. \n")
    print("This app is designed to assist you with some basic care taking of your indoor house-plants. \n")
    print("Currently, this app supports the following popular indoor house-plants: \n\nMONSTERA\nPOTHOS\nPEACE LILY\nFICUS\nSUCCULENT\nDRACAENA\nALOE VERA\nPEPEROMIA\nSNAKE PLANT\nTRADESCANTIA\nCHINESE EVERGREEN\nHOYA\nANTHURIUM\nPARLOR PALM\nPHILODENDRON\n")
    print("If you have any plants outside of this list, please come back another time when our list is updated! \nBut for now, let's help you out with what we support :) \n")
    input("\n\nPress ENTER to continue...\n\n")
    os.system("clear")
introduction()

# Instructions for user, to be printed throughout app.
instructions = "\nINSTRUCTIONS: \n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'R' to REMOVE a plant from your collection. \n3. Enter 'F' to FINALISE your plant collection. \n "

# List of supported plants for referencing inside functions.
supported_plants = [
    "MONSTERA",
    "POTHOS",
    "PEACE LILY",
    "FICUS",
    "SUCCULENT",
    "DRACAENA",
    "ALOE VERA",
    "PEPEROMIA",
    "SNAKE PLANT",
    "TRADESCANTIA",
    "CHINESE EVERGREEN",
    "HOYA",
    "ANTHURIUM",
    "PARLOR PALM",
    "PHILODENDRON",
    ]

# Function to initialize the first feature of program - adds the first plant to users collection.
def get_started():
    user_option = input("To get started, enter 'A' to add a plant to your collection.\n\n")
    os.system("clear")
    if user_option.upper() == "A":
        add_plant = input("\nWhich plant would you like to add?\n\n MONSTERA \n POTHOS \n PEACE LILY \n FICUS \n SUCCULENT \n DRACAENA \n ALOE VERA \n PEPEROMIA \n SNAKE PLANT \n TRADESCANTIA \n CHINESE EVERGREEN \n HOYA \n ANTHURIUM \n PARLOR PALM \n PHILODENDRON \n\n")
        os.system("clear")
        if add_plant.upper() in supported_plants:
            print(f"\n You added {add_plant.upper()}! \n")
            your_table.add_row([add_plant.upper()])
            program_plant_name_list.append(add_plant.upper())
            print(your_table)
            print(instructions)
        else:
            print("INVALID SELECTION!")
            get_started()        
    else:
        get_started()
get_started()            
      
# Function for adding/ removing plants and finalising the users plant collection.
def update_plant_collection():
    user_option = input("\nWhat would you like to do?\n")
    os.system("clear")
    # Allows user to add plant to their collection.
    if user_option.upper() == "A":
        add_plant = input("\nWhich plant would you like to add?\n\n MONSTERA \n POTHOS \n PEACE LILY \n FICUS \n SUCCULENT \n DRACAENA \n ALOE VERA \n PEPEROMIA \n SNAKE PLANT \n TRADESCANTIA \n CHINESE EVERGREEN \n HOYA \n ANTHURIUM \n PARLOR PALM \n PHILODENDRON \n\n")
        os.system("clear")
        if add_plant.upper() in supported_plants:
            print(f"\n You added {add_plant.upper()}! \n")
            your_table.add_row([add_plant.upper()])
            program_plant_name_list.append(add_plant.upper())
            print(your_table)
            print(instructions)
            update_plant_collection()
        else:
            print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
            update_plant_collection()
    # Allows user to remove plant from their collection.
    elif user_option.upper() == "R":
        print(your_table)
        while True:
            try:
                remove_plant = int(input("\nWhich plant would you like to remove? \n\nPress '0' for PLANT 1\nPress '1' for PLANT 2\nPress '2' for PLANT 3 and so on...\n\n"))
                os.system("clear")
                break
            except ValueError:
                os.system("clear")
                print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
        if remove_plant <= len(program_plant_name_list) and len(program_plant_name_list) > 0:
                print(f"\nYou removed PLANT in position {(str(remove_plant))} from your collection. \n")
                your_table.del_row(int(remove_plant))
                program_plant_name_list.remove(program_plant_name_list[remove_plant])
                print(your_table)
                print(instructions)
                update_plant_collection()
        else:
            print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
            update_plant_collection()
    # Finalises collection and moves on.
    elif user_option.upper() == "F":
        print("\nThanks, your collection is complete!\n")  
    else:
        print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
        update_plant_collection()
update_plant_collection()

# Variable declared as a dictioanry which will store the names of the plants in the users plant collection as KEYS.
all_user_plant_data = {}

# Stores the user plant collection names as KEYS.
for plant in program_plant_name_list:
    all_user_plant_data.update({plant:''})

# Shows user their final plant collection in prettytable. 
print(your_table)

# Continue prompt.
input("\n\nPress ENTER to continue...\n\n")
os.system("clear")

# Takes input from user as an integer re: when they last watered each plant in their collection.
print(your_table)
plant_data = []
def get_user_water_freq():
    for plant in program_plant_name_list:
        print("\n\n\n\nTell me a little bit more about your " + plant + "...\n")
        while True:
            try:
                add_water_data = int(input("How many days since you last watered your " + plant + "? "))
                plant_data.append(add_water_data)
                all_user_plant_data.update({plant: [add_water_data]})
                break
            except ValueError:
                os.system("clear")
                print(your_table)
                print("\nINVALID INPUT! Please enter a Number...\n")
get_user_water_freq()

# Clears for next feature.
os.system("clear")
print("\n\nThanks for the info about WATERING your plants!\n\n\n")
print(your_table)

# Takes input from user as an integer re: when they last re-potted each plant in their collection.
def get_user_repot_freq():
    for plant in program_plant_name_list:
        print("\n\n\n\nTell me a little bit more about your " + plant + "...\n")
        while True:
            try:
                add_repot_data = int(input("How many days since you last re-potted your " + plant + "? "))
                plant_data.append(add_repot_data)
                all_user_plant_data[plant].append(add_repot_data)
                break
            except ValueError:
                os.system("clear")
                print(your_table)
                print("\nINVALID INPUT! Please enter a Number...\n")
get_user_repot_freq()

# Clears for next feature.
os.system("clear")
print("\n\nThanks for the info about RE-POTTING your plants!\n\n\n")
print(your_table)

# Takes input from user as a string and converts to boolean re: is their plant located near a window.
def get_user_plant_location():
    for plant in program_plant_name_list:
        print(f"\n\n\n\nTell me a little bit more about your {plant} ...\n")
        while True:
            add_location_data = (input(f"Y or N, do you keep your {plant} near a window? "))
            if add_location_data.upper() == 'Y': 
                plant_data.append(True)
                all_user_plant_data[plant].append((True))
                break
            elif add_location_data.upper() == 'N': 
                plant_data.append(False)
                all_user_plant_data[plant].append((False))   
                break
            else:
                print("\nINVALID SELECTION! Please enter 'Y' or 'N' \n")   
                os.system("clear")
                print(your_table)    
get_user_plant_location()

# Continue prompt.
print("\n\n\nThanks for all the data! \n\n")
input("\nPress ENTER to continue...\n\n")
os.system("clear")

# Prints pretty table back to the user one last time.
print(your_table)
print("\n\nBased on the details you've submitted, here is some handy information! \n\n\n")

# Compares the values of each KEY in all_user_plant_data (plant names in user collection) 
# to the objects in the Plant class. Object has been defined as the variable PLANTDATA 
# and modulates according to the KEY in all_user_plant_data.
def recommendations():
    for key in all_user_plant_data.keys():
        if key == "MONSTERA":
            PLANTDATA = Plant("MONSTERA", 11, 365, True)
        if key == "POTHOS":
            PLANTDATA = Plant("POTHOS", 7, 365, False)
        if key == "PEACE LILY":    
            PLANTDATA = Plant("PEACE_LILY", 7, 730, False)
        if key == "FICUS":    
            PLANTDATA = Plant("FICUS", 5, 730, True)
        if key == "SUCCULENT":
            PLANTDATA = Plant("SUCCULENT", 3, 730, True)
        if key == "DRACAENA":
            PLANTDATA = Plant("DRACAENA", 12, 1460, False)
        if key == "ALOE VERA":
            PLANTDATA = Plant("ALOE_VERA", 18, 1095, True)
        if key == "PEPEROMIA":
            PLANTDATA = Plant("PEPEROMIA", 10, 730, True)
        if key == "SNAKE PLANT":
            PLANTDATA = Plant("SNAKE_PLANT", 7, 2555, True)
        if key == "TRADESCANTIA":
            PLANTDATA = Plant("TRADESCANTIA", 7, 356, False)
        if key == "CHINESE EVERGREEN":
            PLANTDATA = Plant("CHINESE_EVERGREEN", 8, 730, True)
        if key == "HOYA":
            PLANTDATA = Plant("HOYA", 14, 2190, False)
        if key == "ANTHURIUM":
            PLANTDATA = Plant("ANTHURIUM", 7, 730, False)
        if key == "PARLOR PALM":
            PLANTDATA = Plant("PARLOR_PALM", 7, 1095, False)
        if key == "PHILODENDRON":
            PLANTDATA = Plant("PHILODENDRON", 11, 1095, True)

        # Prints a recommendation based on the difference between the number of days 
        # since the user watered their plant and the no of days stored in the Plant class under water_freq.
        if all_user_plant_data[key][0] > getattr(PLANTDATA, "water_freq"):
            print("You're overdue on watering your " + key + " by " + str(((all_user_plant_data[key][0])) - ((getattr(PLANTDATA, "water_freq")))) + " days!\n")
        elif all_user_plant_data[key][0] == getattr(PLANTDATA, "water_freq"):
            print("Today's the day to water your " + key + " ! \n")
        else:
            print("No need to stress!, you have " + str(((getattr(PLANTDATA, "water_freq"))) - ((all_user_plant_data[key][0]))) + " days to water your " + key + "! \n")

        # Prints a recommendation based on the difference between the number of days 
        # since the user re-potted their plant and the no of days stored in the Plant class under repot_freq.
        if all_user_plant_data[key][1] > getattr(PLANTDATA, "repot_freq"):
                print("You're overdue on repotting your " + key + " by " + str(((all_user_plant_data[key][1])) - ((getattr(PLANTDATA, "repot_freq")))) + " days! \n")
        elif all_user_plant_data[key][1] == getattr(PLANTDATA, "repot_freq"):
            print("Today's the day to repot your " + key + " ! \n")
        else:
            print("You've got time!, you should re-pot your " + key + " in about " + str(((getattr(PLANTDATA, "repot_freq"))) - ((all_user_plant_data[key][1]))) + " days! \n")

        # Prints a recommendation based on whether or not the user keeps each plant near a window or not.
        if all_user_plant_data[key][2] and getattr(PLANTDATA, "near_window"):
                print(f"Your {key} is kept near a window, great stuff! {key}'s need a fair amount of sunlight to remain happy :)\n\n\n")
        elif not all_user_plant_data[key][2] and getattr(PLANTDATA, "near_window"):
            print(f"Your {key} is not kept near a window, this isn't great... {key}'s need a fair amount of sunlight to remain happy! \n\n\n")
        elif all_user_plant_data[key][2] and not getattr(PLANTDATA, "near_window"):
            print(f"Your {key} is kept near a window, this isn't great... {key}'s take offence to too much sunlight!\n\n\n")
        else:
            print(f"Your {key} is not kept near a window, great stuff! as you obviously already know, {key}'s take offence to too much sunlight! \n\n\n")
    print("\n\n")
recommendations()

# End of program.
print("Thank you for using PlantApp.\n\n\n\n")

if __name__ == "__main__":
    pass
