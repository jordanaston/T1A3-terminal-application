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
print("\nWelcome to PLANTAPP. \n")
print("This app is designed to assist you with some basic care taking of your indoor house-plants. \n")
print("Currently, this app supports the following popular indoor house-plants: \n\nMONSTERA\nPOTHOS\nPEACE LILY\nFICUS\nSUCCULENT\n")
print("If you have any plants outside of this list, please come back another time when our list is updated! \nBut for now, let's help you out with what we support :) \n")
print("To get started, tell me a little bit about your current house-plant situation. \n")


# Instructions for user input
instructions = "\nINSTRUCTIONS: \n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'R' to REMOVE a plant from your collection. \n3. Enter 'F' to FINALISE your plant collection. \n "
print(instructions)



# Function for adding and removing plants to the users plant collection.
# user_option = input("\nWhat would you like to do?\n")

# LETS TAKE INPUT OF ALL PLANTS AT ONCE TO AVOID WET CODE > THEN YOU CAN USE INSTRUCTIONS (A,R,E) TO ADD / REMOVE / FINISH

def update_plant_collection():

    user_option = input("\nWhat would you like to do?\n")
    if user_option == "A":
        add_plant = input("\nWhich plant would you like to add? \n")

        if add_plant == "MONSTERA":
            print("\n You added MONSTERA! \n")
            your_table.add_row(["MONSTERA",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant == "POTHOS":
            print("\n You added POTHOS! \n")
            your_table.add_row(["POTHOS",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant == "PEACE LILY":
            print("\n You added PEACE LILY! \n")
            your_table.add_row(["PEACE LILY",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant == "FICUS":
            print("\n You added FICUS! \n")
            your_table.add_row(["FICUS",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif add_plant == "SUCCULENT":
            print("\n You added SUCCULENT! \n")
            your_table.add_row(["SUCCULENT",'','','',])
            print(your_table)
            print(instructions)
            update_plant_collection()


    elif user_option == "R":
        remove_plant = input("Which plant would you like to remove? \n'1' for ROW 1\n'2' for ROW 2\n'3' for ROW 3 and so on...\n ")
        if remove_plant == "1":
            print("\n You removed plant 1 from your collection. \n")
            your_table.del_row(0)
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "2":
            print("\n You removed plant 2 from your collection. \n")
            your_table.del_row(1)
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "3":
            print("\n You removed plant 3 from your collection. \n")
            your_table.del_row(2)
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "4":
            print("\n You removed plant 4 from your collection. \n")
            your_table.del_row(3)
            print(your_table)
            print(instructions)
            update_plant_collection()

        elif remove_plant == "5":
            print("\n You removed plant 5 from your collection. \n")
            your_table.del_row(4)
            print(your_table)
            print(instructions)
            update_plant_collection()  
        
    elif user_option == "F":
        print("Thanks!")
        # break
        
    else:
        print("IVALID SELECTION! Please select 'A', 'R' or 'F'")
        update_plant_collection()

update_plant_collection()



# print(your_table)

