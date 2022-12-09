
from prettytable import PrettyTable
from plant_class import Plant

your_table = PrettyTable(['Plant Name','No. Days Since Watered', 'No. Days Since Re-Pot','Near Window'])
your_table.add_row(["MONSTERA",'','','',])
your_table.add_row(["DEVIL'S IVY",'','','',])
your_table.add_row(["PEACE LILY",'','','',])
your_table.add_row(["FICUS",'','','',])
your_table.add_row(["SUCCULENT",'','','',])


MONSTERA = Plant("monstera", 11, 365, True)
DEVILS_IVY = Plant("devils ivy", 7, 365, False)
PEACE_LILY = Plant("peace lily", 7, 730, False)
FICUS = Plant("ficus", 5, 730, True)
SUCCULENT = Plant("succulent", 3, 730, True)

print("\nWelcome to PLANTAPP. \n")
print("This app is designed to assist you with some basic care taking of your indoor house-plants. \n")
print("Currently, this app supports the following popular indoor house-plants: \n\nMONSTERA\nDEVIL'S IVY\nPEACE LILY\nFICUS\nSUCCULENT\n")
print("If you have any plants outside of this list, please come back another time when our list is updated! \nBut for now, let's help you out with what we support :) \n")
print("To get started, tell me a little bit about your current house-plant situation. \n")


# ---------------------------

instructions = "\n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'D' to DELETE a plant from your collection. "

print(instructions)

# ---------------------------

add_delete_plant = input("\nWhat would you like to do?\n")

def update_plant_collection():
    if add_delete_plant == "A":
        print("You chose to add a plant!")
    else:
        print("You didn't select anything...")

update_plant_collection()

# print(your_table)

