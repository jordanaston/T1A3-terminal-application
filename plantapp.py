from prettytable import PrettyTable
import numpy as np
from random import randint
import pandas
from requests import get
from plantclass import Plant
from plantclass import userPlant
import os

os.system("clear")


# Prettytable data pre-filled
# your_table = PrettyTable(['Plant Name','No. Days Since Watered', 'No. Days Since Re-Pot','Near Window'])
your_table = PrettyTable(['Your Plant Collection 🌱',])

# List to handle data behind scenes 
program_plant_name_list = []

# Dictionary storing user plant data to corresponding plant name
program_plant_data_list = []

# Object Data for Plant Class
MONSTERA = Plant("MONSTERA", 11, 365, True)
POTHOS = Plant("POTHOS", 7, 365, False)
PEACE_LILY = Plant("PEACE_LILY", 7, 730, False)
FICUS = Plant("FICUS", 5, 730, True)
SUCCULENT = Plant("SUCCULENT", 3, 730, True)
DRACAENA = Plant("DRACAENA", 12, 1460, False)
ALOE_VERA = Plant("ALOE_VERA", 18, 1095, True)
PEPEROMIA = Plant("PEPEROMIA", 10, 730, True)
SNAKE_PLANT = Plant("SNAKE_PLANT", 7, 2555, True)
TRADESCANTIA = Plant("TRADESCANTIA", 7, 356, False)
CHINESE_EVERGREEN = Plant("CHINESE_EVERGREEN", 8, 730, True)
HOYA = Plant("HOYA", 14, 2190, False)
ANTHURIUM = Plant("ANTHURIUM", 7, 730, False)
PARLOR_PALM = Plant("PARLOR_PALM", 7, 1095, False)
PHILODENDRON = Plant("PHILODENDRON", 11, 1095, True)


# Introduction to the app

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

# Instructions for user input
instructions = "\nINSTRUCTIONS: \n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'R' to REMOVE a plant from your collection. \n3. Enter 'F' to FINALISE your plant collection. \n "

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


# Function to initialize first feature of program and adds the first plant to users collection.
def get_started():
    user_option = input("To get started, press 'A' to add a plant to your collection.\n\n")
    os.system("clear")
    if user_option.upper() == "A":
        add_plant = input("\nWhich plant would you like to add?\n\n MONSTERA \n POTHOS \n PEACE LILY \n FICUS \n SUCCULENT \n DRACAENA \n ALOE VERA \n PEPEROMIA \n SNAKE PLANT \n TRADESCANTIA \n CHINESE EVERGREEN \n HOYA \n ANTHURIUM \n PARLOR PALM \n PHILODENDRON \n\n")
        os.system("clear")
        if add_plant.upper() in supported_plants:
            print("\n You added " + add_plant.upper() + "! \n")
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
    if user_option.upper() == "A":
        add_plant = input("\nWhich plant would you like to add?\n\n MONSTERA \n POTHOS \n PEACE LILY \n FICUS \n SUCCULENT \n DRACAENA \n ALOE VERA \n PEPEROMIA \n SNAKE PLANT \n TRADESCANTIA \n CHINESE EVERGREEN \n HOYA \n ANTHURIUM \n PARLOR PALM \n PHILODENDRON \n\n")
        os.system("clear")
        if add_plant.upper() in supported_plants:
            print("\n You added " + add_plant.upper() + "! \n")
            your_table.add_row([add_plant.upper()])
            program_plant_name_list.append(add_plant.upper())
            print(your_table)
            print(instructions)
            update_plant_collection()
        else:
            print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
            update_plant_collection()
     
    elif user_option.upper() == "R":
        print(your_table)
        remove_plant = int(input("\nWhich plant would you like to remove? \n\nPress '0' for PLANT 1\nPress '1' for PLANT 2\nPress '2' for PLANT 3 and so on...\n\n"))
        os.system("clear")
        if remove_plant <= len(program_plant_name_list):
                print("\nYou removed PLANT in position " + (str(remove_plant)) + " from your collection. \n")
                your_table.del_row(int(remove_plant))
                program_plant_name_list.remove(program_plant_name_list[remove_plant])
                print(your_table)
                print(instructions)
                update_plant_collection()
        else:
            print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
            update_plant_collection()
 
    elif user_option.upper() == "F":
        print("\nThanks, your collection is complete!\n")
         
    else:
        print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
        update_plant_collection()
update_plant_collection()


# Declaring Dictioanry and storing the names of the plants (the user input) as KEYS
all_user_plant_data_2 = {}

for plant in program_plant_name_list:
    all_user_plant_data_2.update({plant:''})


# Shows user their final plant collection 
print(your_table)

input("\n\nPress ENTER to continue...\n\n")
os.system("clear")

# Gets plant data from user (last water,last re-pot,location) and stores data in a list
print(your_table)
plant_data = []

def get_user_water_freq():
    for plant in program_plant_name_list:
        print("\n\n\n\nTell me a little bit more about your " + plant + "...\n")
        while True:
            try:
                add_water_data = int(input("How many days since you last watered your " + plant + "? "))
                plant_data.append(add_water_data)
                all_user_plant_data_2.update({plant: [add_water_data]})
                break
            except ValueError:
                os.system("clear")
                print(your_table)
                print("\nINVALID INPUT! Please enter a Number...\n")
get_user_water_freq()


print("\n\nThanks for the info about WATERING your plants!\n\n")
os.system("clear")
print(your_table)


def get_user_repot_freq():
    for plant in program_plant_name_list:
        print("\n\n\n\nTell me a little bit more about your " + plant + "...\n")
        while True:
            try:
                add_repot_data = int(input("How many days since you last re-potted your " + plant + "? "))
                plant_data.append(add_repot_data)
                all_user_plant_data_2[plant].append(add_repot_data)
                break
            except ValueError:
                os.system("clear")
                print(your_table)
                print("\nINVALID INPUT! Please enter a Number...\n")
get_user_repot_freq()

print("\n\nThanks for the info about RE-POTTING your plants!\n\n")
os.system("clear")
print(your_table)

def get_user_plant_location():
    for plant in program_plant_name_list:
        print("\n\n\n\nTell me a little bit more about your " + plant + "...\n")
        while True:
            add_location_data = (input("Y or N, do you keep your " + plant + " near a window? "))
            if add_location_data.upper() == 'Y': 
                plant_data.append(True)
                all_user_plant_data_2[plant].append((True))
                break
            elif add_location_data.upper() == 'N': 
                plant_data.append(False)
                all_user_plant_data_2[plant].append((False))   
                break
            else:
                print("\nINVALID SELECTION! Please enter 'Y' or 'N' \n")       
get_user_plant_location()

print(plant_data)

print("\n\nTESTING\n\n")
print(all_user_plant_data_2)

# Extrapolate data from each plant. Getting each block of 3 list items from "plant_data", 
# storing them in lists then storing all of those lists inside a big list.
# This is so we can merge that data into a dictionary. EG: {'MONSTERA': [3, 185, True]}  
first_plant_list = []
second_plant_list = []
third_plant_list = []
fourth_plant_list = []
fifth_plant_list = []
sixth_plant_list = []
seventh_plant_list = []
eighth_plant_list = []
ninth_plant_list = []
tenth_plant_list = []
eleventh_plant_list = []
twelfth_plant_list = []
thirteenth_plant_list = []
fourteenth_plant_list = []
fifteenth_plant_list = []

user_plant_data_list = [
    first_plant_list,
    second_plant_list,
    third_plant_list,
    fourth_plant_list,
    fifth_plant_list,
    sixth_plant_list,
    seventh_plant_list,
    eighth_plant_list,
    ninth_plant_list,
    tenth_plant_list,
    eleventh_plant_list,
    twelfth_plant_list,
    thirteenth_plant_list,
    fourteenth_plant_list,
    fifteenth_plant_list
]

def add_data_to_lists():
    for data in plant_data[0:3]:
        first_plant_list.append(data)

    for data in plant_data[3:6]:
        second_plant_list.append(data)

    for data in plant_data[6:9]:
        third_plant_list.append(data)

    for data in plant_data[9:12]:
        fourth_plant_list.append(data)

    for data in plant_data[12:15]:
        fifth_plant_list.append(data)

    for data in plant_data[15:18]:
        sixth_plant_list.append(data)

    for data in plant_data[18:21]:
        seventh_plant_list.append(data)

    for data in plant_data[21:24]:
        eighth_plant_list.append(data)

    for data in plant_data[24:27]:
        ninth_plant_list.append(data)

    for data in plant_data[27:30]:
        tenth_plant_list.append(data)
            
    for data in plant_data[30:33]:
        eleventh_plant_list.append(data)

    for data in plant_data[33:36]:
        twelfth_plant_list.append(data)

    for data in plant_data[36:39]:
        thirteenth_plant_list.append(data)

    for data in plant_data[39:42]:
        fourteenth_plant_list.append(data)

    for data in plant_data[42:45]:
        fifteenth_plant_list.append(data)
add_data_to_lists()

# ZIPS all the plants names from the user with all the plant data from the user together to create a DICT for comparing with plant class data
all_user_plant_data = dict(zip(program_plant_name_list, user_plant_data_list))

# print(all_user_plant_data)
print("\n")

print("\nThanks for all the data! \n")
input("\nPress ENTER to continue...\n\n")
os.system("clear")

# def add_user_plant_data_to_prettytable():
#         your_table.add_row(first_plant_list)

print(your_table)

print("\n\nBased on the details you've submitted, here is some handy information! \n\n")


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

        if all_user_plant_data[key][0] > getattr(PLANTDATA, "water_freq"):
            print("You're overdue on watering your " + key + " by " + str(((all_user_plant_data[key][0])) - ((getattr(PLANTDATA, "water_freq")))) + " days!\n")
        elif all_user_plant_data[key][0] == getattr(PLANTDATA, "water_freq"):
            print("Today's the day to water your " + key + " ! \n")
        else:
            print("No need to stress!, you have " + str(((getattr(PLANTDATA, "water_freq"))) - ((all_user_plant_data[key][0]))) + " days to water your " + key + "! \n")

        if all_user_plant_data[key][1] > getattr(PLANTDATA, "repot_freq"):
                print("You're overdue on repotting your " + key + " by " + str(((all_user_plant_data[key][1])) - ((getattr(PLANTDATA, "repot_freq")))) + " days! \n")
        elif all_user_plant_data[key][1] == getattr(PLANTDATA, "repot_freq"):
            print("Today's the day to repot your " + key + " ! \n")
        else:
            print("You've got time!, you should re-pot your " + key + " in about " + str(((getattr(PLANTDATA, "repot_freq"))) - ((all_user_plant_data[key][1]))) + " days! \n")

        if all_user_plant_data[key][2] and getattr(PLANTDATA, "near_window"):
                print("Your " + key + " is near a window, this is good!\n")
        elif not all_user_plant_data[key][2] and getattr(PLANTDATA, "near_window"):
            print("Your " + key + " is not near a window, this is bad!\n")
        elif all_user_plant_data[key][2] and not getattr(PLANTDATA, "near_window"):
            print("Your " + key + " is near a window, this is bad!\n")
        else:
            print("Your " + key + " is not near a window, this is good!\n")
    print("\n\n")
recommendations()

def terminate_app():
    print("\n\nThank you for using PlantApp.\n\n")
terminate_app()

