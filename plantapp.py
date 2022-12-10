from prettytable import PrettyTable
from plantclass import Plant

# Prettytable data pre-filled
your_table = PrettyTable(['Plant Name','No. Days Since Watered', 'No. Days Since Re-Pot','Near Window'])
# your_table.add_row(["MONSTERA",'','','',])
# your_table.add_row(["POTHOS",'','','',])
# your_table.add_row(["PEACE LILY",'','','',])
# your_table.add_row(["FICUS",'','','',])
# your_table.add_row(["SUCCULENT",'','','',])

# Plant class data
MONSTERA = Plant("monstera", 11, 365, True)
POTHOS = Plant("pothos", 7, 365, False)
PEACE_LILY = Plant("peace lily", 7, 730, False)
FICUS = Plant("ficus", 5, 730, True)
SUCCULENT = Plant("succulent", 3, 730, True)

# Introduction to the app
print("\n\n\n\nWelcome to PLANTAPP. \n")
print("This app is designed to assist you with some basic care taking of your indoor house-plants. \n")
print("Currently, this app supports the following popular indoor house-plants: \n\nMONSTERA\nPOTHOS\nPEACE LILY\nFICUS\nSUCCULENT\n")
print("If you have any plants outside of this list, please come back another time when our list is updated! \nBut for now, let's help you out with what we support :) \n")
input("\n\nPress ENTER to continue...\n\n")
print("To get started, press 'A' to add your first plant to your collection. \n")

# Instructions for user input
instructions = "\nINSTRUCTIONS: \n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'R' to REMOVE a plant from your collection. \n3. Enter 'F' to FINALISE your plant collection. \n "
# print(instructions)

# Function for adding and removing plants to the users plant collection.
def update_plant_collection():
    user_option = input("\nWhat would you like to do?\n")
    if user_option.upper() == "A":
        add_plant = input("\nWhich plant would you like to add? \n")

        if add_plant.upper() == "MONSTERA":
            print("\n You added MONSTERA! \n")
            your_table.add_row(["MONSTERA",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "POTHOS":
            print("\n You added POTHOS! \n")
            your_table.add_row(["POTHOS",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "PEACE LILY":
            print("\n You added PEACE LILY! \n")
            your_table.add_row(["PEACE LILY",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "FICUS":
            print("\n You added FICUS! \n")
            your_table.add_row(["FICUS",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant.upper() == "SUCCULENT":
            print("\n You added SUCCULENT! \n")
            your_table.add_row(["SUCCULENT",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()
        
        else:
            print("\nIVALID SELECTION! Please select 'A', 'R' or 'F'\n")
            update_plant_collection()

    elif user_option.upper() == "R":
        remove_plant = input("\nWhich plant would you like to remove? \n'1' for ROW 1\n'2' for ROW 2\n'3' for ROW 3 and so on...\n")
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

        else:
            print("\nIVALID SELECTION! Please select 'A', 'R' or 'F'\n")
            update_plant_collection()
        
    elif user_option.upper() == "F":
        print("\nThanks, your collection is complete!\n")
         
    else:
        print("\nIVALID SELECTION! Please select 'A', 'R' or 'F'\n")
        update_plant_collection()

update_plant_collection()

print(your_table)
print("\nThe above table is your final collection.\n")

input("\n\nPress ENTER to continue...\n\n")

print("\nTell me a little bit more about your " + (your_table.rows[0][0]) + "...\n")

def fill_table_data():

    row_one_data = []

    if your_table.rows[0][0] == "MONSTERA" or "POTHOS" or "PEACE LILY" or "FICUS" or "SUCCULENT":
        add_plant_data = input("How many days since you last watered your " + (your_table.rows[0][0]) + "? ")
        row_one_data.append(add_plant_data)
        add_plant_data = (input("How many days since you last re-potted your " + (your_table.rows[0][0]) + "? "))
        row_one_data.append(add_plant_data)
        add_plant_data = (input("Y or N, do you keep your " + (your_table.rows[0][0]) + " near a window? "))

        if add_plant_data == "Y":
            row_one_data.append(True)

        elif add_plant_data == "N":
            row_one_data.append(False)

        
        print(row_one_data)
        
fill_table_data()