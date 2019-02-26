### This is a simple text based RPG made in Python by
### Ryan J. Wilson
from classes import *


print("""The year is 2222. I don't know why I chose that year, but I did.
This game is based on you getting your ass kicked by some kind of
monster. But I am too lazy to write the story line right this 
second. So I am just putting a bunch of placeholder words right
here for now. Because I hate writing the actual story line for
a game. Note to self. Find someone to write the story lines for
all your games. End note""")

player_name = input("Enter Players Name: ")
character_name = input("What would you like to name your character: ")

inventory = Inventory()
recieve_gift = input("Would you like to recieve a gift? Enter y for yes or n for no ")
if (recieve_gift.capitalize() == "Y"):
    inventory.add_item(Item('Sword', 5, 1, 15, 2))
    inventory.add_item(Item('Armor', 0, 10, 25, 5))
else:
    inventory.add_item(Item("", 0, 0, 0, 0))

inventory.print_items()

print (""" You start off in some city that again has no name, I just need
a place holder for now. So %s, you are in the city go_fuck_yourself in
the state of with_a_baseball_bat. So %s, where would you like to go?""" %(character_name, character_name))

menu = """1. Go to the armory
2. Goto the doctor
3. Continue
4. End Game"""
print(menu)

menu_selection = input("Please pick between 1 and 4: ")

menu_selection = int(menu_selection)


def menu_switch_case(player_selection):
    switch = {
        1: "Yeah, the armory is closed till I write the story",
    
        2: "Doctors are for pussies...at least till I write the story",
   
        3: "I can let you continue, but there is nothing else yet",

        4: "Good bye!"
        }
    return switch.get(player_selection, "please pick a number between 1 and 4") 

while menu_selection != 3:
   
    if menu_selection != 4:
        print(menu_switch_case(menu_selection))
        menu_selection = input("Please pick between 1 and 4: ")
        menu_selection = int(menu_selection)
    else:
        menu_selection = 3
