### This is a simple text based RPG made in Python by
### Ryan J. Wilson
from classes import *
print("The year is 2222. I don't know why I chose that year, but I did.")
print("This game is based on you getting your ass kicked by some kind of")
print("monster. But I am too lazy to write the story line right this ")
print("second. So I am just putting a bunch of placeholder words right")
print("here for now. Because I hate writing the actual story line for")
print("a game. Note to self. Find someone to write the story lines for")
print(" all your games. End note")

playerName=input("What is your name player? ")
characterName =input("What would you like to name your character? ")

print(playerName)
print(characterName)
inventory = Inventory()
recieveGift= input("Would you like to recieve a gift? Enter y for yes or n for no ")
if (recieveGift.capitalize() == "Y"):
    inventory.add_item(Item('Sword', 5, 1, 15, 2))
    inventory.add_item(Item('Armor', 0, 10, 25, 5))
else:
    inventory.add_item(Item("", 0, 0, 0, 0))

inventory.print_items()