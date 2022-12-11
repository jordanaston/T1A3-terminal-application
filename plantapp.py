from prettytable import PrettyTable
from plantclass import Plant
from plantclass import userPlant
import os

os.system("clear")

# Prettytable data pre-filled
your_table = PrettyTable(['Plant Name','No. Days Since Watered', 'No. Days Since Re-Pot','Near Window'])

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
print("\n\nWelcome to PLANTAPP. \n")
print("This app is designed to assist you with some basic care taking of your indoor house-plants. \n")
print("Currently, this app supports the following popular indoor house-plants: \n\nMONSTERA\nPOTHOS\nPEACE LILY\nFICUS\nSUCCULENT\nDRACAENA\nALOE VERA\nPEPEROMIA\nSNAKE PLANT\nTRADESCANTIA\nCHINESE EVERGREEN\nHOYA\nANTHURIUM\nPARLOR PALM\nPHILODENDRON\n")
print("If you have any plants outside of this list, please come back another time when our list is updated! \nBut for now, let's help you out with what we support :) \n")
input("\n\nPress ENTER to continue...\n\n")
os.system("clear")
print("To get started, press 'A' to add your first plant to your collection. \n")

# Instructions for user input
instructions = "\nINSTRUCTIONS: \n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'R' to REMOVE a plant from your collection. \n3. Enter 'F' to FINALISE your plant collection. \n "

# Function for adding and removing plants to the users plant collection.
def update_plant_collection():
    user_option = input("\nWhat would you like to do?\n")
    os.system("clear")
    if user_option.upper() == "A":
        add_plant = input("\nWhich plant would you like to add?\n\n MONSTERA \n POTHOS \n PEACE LILY \n FICUS \n SUCCULENT \n DRACAENA \n ALOE VERA \n PEPEROMIA \n SNAKE PLANT \n TRADESCANTIA \n CHINESE EVERGREEN \n HOYA \n ANTHURIUM \n PARLOR PALM \n PHILODENDRON \n\n")
        os.system("clear")
        if add_plant.upper() == "MONSTERA":
            print("\n You added MONSTERA! \n")
            your_table.add_row(["MONSTERA",'','','',])
            program_plant_name_list.append("MONSTERA")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "POTHOS":
            print("\n You added POTHOS! \n")
            your_table.add_row(["POTHOS",'','','',])
            program_plant_name_list.append("POTHOS")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "PEACE LILY":
            print("\n You added PEACE LILY! \n")
            your_table.add_row(["PEACE LILY",'','','',])
            program_plant_name_list.append("PEACE LILY")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "FICUS":
            print("\n You added FICUS! \n")
            your_table.add_row(["FICUS",'','','',])
            program_plant_name_list.append("FICUS")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "SUCCULENT":
            print("\n You added SUCCULENT! \n")
            your_table.add_row(["SUCCULENT",'','','',])
            program_plant_name_list.append("SUCCULENT")
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        elif add_plant.upper() == "DRACAENA":
            print("\n You added DRACAENA! \n")
            your_table.add_row(["DRACAENA",'','','',])
            program_plant_name_list.append("DRACAENA")
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        elif add_plant.upper() == "ALOE VERA":
            print("\n You added ALOE VERA! \n")
            your_table.add_row(["ALOE VERA",'','','',])
            program_plant_name_list.append("ALOE VERA")
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        elif add_plant.upper() == "PEPEROMIA":
            print("\n You added PEPEROMIA! \n")
            your_table.add_row(["PEPEROMIA",'','','',])
            program_plant_name_list.append("PEPEROMIA")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "SNAKE PLANT":
            print("\n You added SNAKE PLANT! \n")
            your_table.add_row(["SNAKE PLANT",'','','',])
            program_plant_name_list.append("SNAKE PLANT")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "TRADESCANTIA":
            print("\n You added TRADESCANTIA! \n")
            your_table.add_row(["TRADESCANTIA",'','','',])
            program_plant_name_list.append("TRADESCANTIA")
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        elif add_plant.upper() == "CHINESE EVERGREEN":
            print("\n You added CHINESE EVERGREEN! \n")
            your_table.add_row(["CHINESE EVERGREEN",'','','',])
            program_plant_name_list.append("CHINESE EVERGREEN")
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        elif add_plant.upper() == "HOYA":
            print("\n You added HOYA! \n")
            your_table.add_row(["HOYA",'','','',])
            program_plant_name_list.append("HOYA")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "ANTHURIUM":
            print("\n You added ANTHURIUM! \n")
            your_table.add_row(["ANTHURIUM",'','','',])
            program_plant_name_list.append("ANTHURIUM")
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "PARLOR PALM":
            print("\n You added PARLOR PALM! \n")
            your_table.add_row(["PARLOR PALM",'','','',])
            program_plant_name_list.append("PARLOR PALM")
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        elif add_plant.upper() == "PHILODENDRON":
            print("\n You added PHILODENDRON! \n")
            your_table.add_row(["PHILODENDRON",'','','',])
            program_plant_name_list.append("PHILODENDRON")
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        else:
            print("\nIVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
            update_plant_collection()

    elif user_option.upper() == "R":
        print(your_table)
        remove_plant = input("\nWhich plant would you like to remove? \n'1' for ROW 1\n'2' for ROW 2\n'3' for ROW 3 and so on...\n")
        os.system("clear")
        if remove_plant == "1":
            print("\n You removed PLANT 1 from your collection. \n")
            your_table.del_row(0)
            program_plant_name_list.remove(program_plant_name_list[0])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "2":
            print("\n You removed PLANT 2 from your collection. \n")
            your_table.del_row(1)
            program_plant_name_list.remove(program_plant_name_list[1])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "3":
            print("\n You removed PLANT 3 from your collection. \n")
            your_table.del_row(2)
            program_plant_name_list.remove(program_plant_name_list[2])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "4":
            print("\n You removed PLANT 4 from your collection. \n")
            your_table.del_row(3)
            program_plant_name_list.remove(program_plant_name_list[3])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "5":
            print("\n You removed PLANT 5 from your collection. \n")
            your_table.del_row(4)
            program_plant_name_list.remove(program_plant_name_list[4])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "6":
            print("\n You removed PLANT 6 from your collection. \n")
            your_table.del_row(5)
            program_plant_name_list.remove(program_plant_name_list[5])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "7":
            print("\n You removed PLANT 7 from your collection. \n")
            your_table.del_row(6)
            program_plant_name_list.remove(program_plant_name_list[6])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "8":
            print("\n You removed PLANT 8 from your collection. \n")
            your_table.del_row(7)
            program_plant_name_list.remove(program_plant_name_list[7])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "9":
            print("\n You removed PLANT 9 from your collection. \n")
            your_table.del_row(8)
            program_plant_name_list.remove(program_plant_name_list[8])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "10":
            print("\n You removed PLANT 10 from your collection. \n")
            your_table.del_row(9)
            program_plant_name_list.remove(program_plant_name_list[9])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "11":
            print("\n You removed PLANT 11 from your collection. \n")
            your_table.del_row(10)
            program_plant_name_list.remove(program_plant_name_list[10])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "12":
            print("\n You removed PLANT 12 from your collection. \n")
            your_table.del_row(11)
            program_plant_name_list.remove(program_plant_name_list[11])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "13":
            print("\n You removed PLANT 13 from your collection. \n")
            your_table.del_row(12)
            program_plant_name_list.remove(program_plant_name_list[12])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "14":
            print("\n You removed PLANT 14 from your collection. \n")
            your_table.del_row(13)
            program_plant_name_list.remove(program_plant_name_list[13])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "15":
            print("\n You removed PLANT 15 from your collection. \n")
            your_table.del_row(14)
            program_plant_name_list.remove(program_plant_name_list[14])
            print(your_table)
            print(instructions)
            update_plant_collection()  

        else:
            print("\nIVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
            update_plant_collection()
        
    elif user_option.upper() == "F":
        print("\nThanks, your collection is complete!\n")
         
    else:
        print("\nIVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
        update_plant_collection()

update_plant_collection()

# Shows user their final plant collection 
print(your_table)
print("\nThe above table is your final collection.\n")

input("\n\nPress ENTER to continue...\n\n")
os.system("clear")

# Gets plant data from user (last water,last re-pot,location) and stores data in a list
print(your_table)
plant_data = []
for plant in program_plant_name_list:
    print("\nTell me a little bit more about your " + plant + "...\n")
    add_plant_data = int(input("How many days since you last watered your " + plant + "? "))
    plant_data.append(add_plant_data)
    add_plant_data = int(input("How many days since you last re-potted your " + plant + "? "))
    plant_data.append(add_plant_data)
    add_plant_data = (input("Y or N, do you keep your " + plant + " near a window? "))
    if add_plant_data.upper() == "Y":
        plant_data.append(True)
    elif add_plant_data.upper() == "N":
        plant_data.append(False)
    else:
        print("\nIVALID SELECTION! Please select 'Y' or 'N' \n")

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


# ZIPS all the plants names from the user with all the plant data from the user together to create a DICT for comparing with plant class data
all_user_plant_data = dict(zip(program_plant_name_list, user_plant_data_list))
print("\n\n")
print(all_user_plant_data)
