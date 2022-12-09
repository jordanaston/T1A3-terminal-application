from prettytable import PrettyTable
from plantclass import Plant

# Prettytable data pre-filled
your_table = PrettyTable(['Plant Name','No. Days Since Watered', 'No. Days Since Re-Pot','Near Window'])
# your_table.add_row(["MONSTERA",'','','',])
# your_table.add_row(["DEVIL'S IVY",'','','',])
# your_table.add_row(["PEACE LILY",'','','',])
# your_table.add_row(["FICUS",'','','',])
# your_table.add_row(["SUCCULENT",'','','',])

# Plant class data
MONSTERA = Plant("monstera", 11, 365, True)
DEVILS_IVY = Plant("devils ivy", 7, 365, False)
PEACE_LILY = Plant("peace lily", 7, 730, False)
FICUS = Plant("ficus", 5, 730, True)
SUCCULENT = Plant("succulent", 3, 730, True)

# Introduction to the app
print("\nWelcome to PLANTAPP. \n")
print("This app is designed to assist you with some basic care taking of your indoor house-plants. \n")
print("Currently, this app supports the following popular indoor house-plants: \n\nMONSTERA\nDEVIL'S IVY\nPEACE LILY\nFICUS\nSUCCULENT\n")
print("If you have any plants outside of this list, please come back another time when our list is updated! \nBut for now, let's help you out with what we support :) \n")
print("To get started, tell me a little bit about your current house-plant situation. \n")


# Instructions for for user input
instructions = "\nINSTRUCTIONS: \n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'R' to REMOVE a plant from your collection. "

print(instructions)





# Function for adding and removing plants to the users plant collection.
add_delete_plant = input("\nWhat would you like to do?\n")


def update_plant_collection():
    if add_delete_plant == "A":
        add_plant = input("Which plant would you like to add? ")
        if add_plant == "MONSTERA":
            print("You added MONSTERA!")
            your_table.add_row(["MONSTERA",'','','',])
            # print(your_table)
        elif add_plant == "DEVIL'S IVY":
            print("You added DEVIL'S IVY!")
            your_table.add_row(["DEVIL'S IVY",'','','',])
            # print(your_table)
        elif add_plant == "PEACE LILY":
            print("You added PEACE LILY!")
            your_table.add_row(["PEACE LILY",'','','',])
            # print(your_table)
        elif add_plant == "FICUS":
            print("You added FICUS!")
            your_table.add_row(["FICUS",'','','',])
            # print(your_table)
        elif add_plant == "SUCCULENT":
            print("You added SUCCULENT!")
            your_table.add_row(["SUCCULENT",'','','',])
            # print(your_table)


    elif add_delete_plant == "R":
        input("Which plant would you like to remove? ")
    
    elif add_delete_plant == "E":
        print("Thanks!")
        # break

update_plant_collection()










# print(your_table)

