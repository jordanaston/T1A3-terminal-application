from prettytable import PrettyTable
from plantclass import Plant
import os

os.system("clear")

# Prettytable data pre-filled
your_table = PrettyTable(['Plant Name','No. Days Since Watered', 'No. Days Since Re-Pot','Near Window'])

# List to handle data behind scenes 
program_plant_name_list = []

# Object Data for Plant Class
MONSTERA = Plant("monstera", 11, 365, True)
POTHOS = Plant("pothos", 7, 365, False)
PEACE_LILY = Plant("peace lily", 7, 730, False)
FICUS = Plant("ficus", 5, 730, True)
SUCCULENT = Plant("succulent", 3, 730, True)
DRACAENA = Plant("dracaena", 12, 1460, False)
ALOE_VERA = Plant("aloe vera", 18, 1095, True)
PEPEROMIA = Plant("peperomia", 10, 730, True)
SNAKE_PLANT = Plant("snake plant", 7, 2555, True)
TRADESCANTIA = Plant("tradescantia", 7, 356, False)
CHINESE_EVERGREEN = Plant("chinese evergreen", 8, 730, True)
HOYA = Plant("hoya", 14, 2190, False)
ANTHURIUM = Plant("anthurium", 7, 730, False)
PARLOR_PALM = Plant("palor palm", 7, 1095, False)
PHILODENDRON = Plant("philodendron", 11, 1095, True)

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
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "2":
            print("\n You removed PLANT 2 from your collection. \n")
            your_table.del_row(1)
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "3":
            print("\n You removed PLANT 3 from your collection. \n")
            your_table.del_row(2)
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "4":
            print("\n You removed PLANT 4 from your collection. \n")
            your_table.del_row(3)
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "5":
            print("\n You removed PLANT 5 from your collection. \n")
            your_table.del_row(4)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "6":
            print("\n You removed PLANT 6 from your collection. \n")
            your_table.del_row(5)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "7":
            print("\n You removed PLANT 7 from your collection. \n")
            your_table.del_row(6)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "8":
            print("\n You removed PLANT 8 from your collection. \n")
            your_table.del_row(7)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "9":
            print("\n You removed PLANT 9 from your collection. \n")
            your_table.del_row(8)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "10":
            print("\n You removed PLANT 10 from your collection. \n")
            your_table.del_row(9)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "11":
            print("\n You removed PLANT 11 from your collection. \n")
            your_table.del_row(10)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "12":
            print("\n You removed PLANT 12 from your collection. \n")
            your_table.del_row(11)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "13":
            print("\n You removed PLANT 13 from your collection. \n")
            your_table.del_row(12)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "14":
            print("\n You removed PLANT 14 from your collection. \n")
            your_table.del_row(13)
            print(your_table)
            print(instructions)
            update_plant_collection()  

        elif remove_plant == "15":
            print("\n You removed PLANT 15 from your collection. \n")
            your_table.del_row(14)
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
    add_plant_data = input("How many days since you last watered your " + plant + "? ")
    plant_data.append(add_plant_data)
    add_plant_data = (input("How many days since you last re-potted your " + plant + "? "))
    plant_data.append(add_plant_data)
    add_plant_data = (input("Y or N, do you keep your " + plant + " near a window? "))
    if add_plant_data.upper() == "Y":
        plant_data.append(True)
    elif add_plant_data.upper() == "N":
        plant_data.append(False)
    else:
        print("\nIVALID SELECTION! Please select 'Y' or 'N' \n")
print(plant_data)



# Merging list of plant data with list of plant names to create a dictionary
print(plant_data[3:6])









# PROBABLY DELETE ALL OF THIS FOR DRY

# def fill_table_data():

#     row_one_data = []

#     if your_table.rows[0][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         add_plant_data = input("How many days since you last watered your " + (your_table.rows[0][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[0][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[0][0]) + " near a window? "))
#         if add_plant_data == "Y":
#             row_one_data.append(True)
#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     if your_table.rows[1][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[1][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[1][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[1][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[1][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)
    
#     if your_table.rows[2][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[2][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[2][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[2][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[2][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)

#     if your_table.rows[3][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[3][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[3][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[3][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[3][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)
    
#     if your_table.rows[4][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[4][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[4][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[4][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[4][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)
    
#     if your_table.rows[5][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[5][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[5][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[5][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[5][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)
    
#     if your_table.rows[6][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[6][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[6][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[6][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[6][0]) + " near a window? \n"))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)
    
#     if your_table.rows[7][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[7][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[7][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[7][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[7][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)

#     else:
#         print(row_one_data)
    
#     if your_table.rows[8][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[8][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[8][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[8][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[8][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)

#     else:
#         print(row_one_data)
        

#     if your_table.rows[9][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[9][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[9][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[9][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[9][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)

#     if your_table.rows[10][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[10][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[10][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[10][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[10][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)

#     if your_table.rows[11][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[11][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[11][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[11][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[11][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)

#     if your_table.rows[12][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[12][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[12][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[12][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[12][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)

#     if your_table.rows[13][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[13][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[13][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[13][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[13][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)
    
#     if your_table.rows[14][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT" or "DRACAENA" or "ALOE VERA" or "PEPEROMIA" or "SNAKE PLANT" or "TRADESCANTIA" or "CHINESE EVERGREEN" or "HOYA" or "ANTHURIUM" or "PARLOR PALM" or "PHILODENDRON":
#         print("\n\nTell me a little bit more about your " + (your_table.rows[14][0]) + "...")
#         add_plant_data = input("\nHow many days since you last watered your " + (your_table.rows[14][0]) + "? ")
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[14][0]) + "? "))
#         row_one_data.append(add_plant_data)
#         add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[14][0]) + " near a window? "))

#         if add_plant_data == "Y":
#             row_one_data.append(True)

#         elif add_plant_data == "N":
#             row_one_data.append(False)
        
#     else:
#         print(row_one_data)


#         print(row_one_data)
#         # fill_table_data()
        
        
# fill_table_data()

# print(row_one_data)