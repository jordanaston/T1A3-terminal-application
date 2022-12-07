
from prettytable import PrettyTable
from plant_class import Plant

your_table = PrettyTable(['Plant Name','No. Days Since Watered', 'No. Days Since Re-Pot','Near Window'])

MONSTERA = Plant("monstera", 11, 365, True)
DEVILS_IVY = Plant("devils ivy", 7, 365, False)
PEACE_LILY = Plant("peace lily", 7, 730, False)
FICUS = Plant("ficus", 5, 730, True)
SUCCULENT = Plant("succulent", 3, 730, True)

# todays_date = ""

print("Welcome to PLANTAPP.")

instructions = "\n1: Enter 'A' to ADD a new plant to your collection. \n2: Enter 'D' to DELETE a plant from your collection. "

print(instructions)

print("\nWhat would you like to do?\n")

# print(str(input(your_table.add_row())))

print(your_table)