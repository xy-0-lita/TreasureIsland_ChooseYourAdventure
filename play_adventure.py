"""
Treasure Island - A Text Adventure Game
Created for 100 Days of Python Bootcamp - Day 3
Author: [Your Name]
Description: Navigate a mysterious island to find hidden treasure.
             Make the right choices or face game over!
"""

import time
from colorama import Fore, init

init(autoreset=True)

def play_adventure():
    print(r'''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print(Fore.CYAN + "Welcome to Treasure Island.")
    print(Fore.CYAN + "Your quest is to find the treasure.")
    print("You find yourself on a foggy toll road. A fork lies ahead. Which way will you choose?")
    time.sleep(1)
    first_choice = input(Fore.MAGENTA + "Choose 'left' or 'right' to proceed.").lower()
    time.sleep(1)
    if first_choice == 'right':
        print(Fore.RED + "You head further into dense fog and denser overgrowth, right into a bear trap. You lose your legs. Game over. ")
        return
    elif first_choice == 'left':
        print("You walk along the road for the better part of a day, finding yourself at the edge of a large lake.")
        time.sleep(1)
        second_choice = input(Fore.MAGENTA + "Will you wait for a boat, or try to swim? Choose 'wait' or 'swim.").lower()
        time.sleep(1)
        if second_choice == 'swim':
            print(Fore.RED + "You got attacked by a disgruntled trout. Game over.")
            return
        elif second_choice == "wait":
            print("You arrive at a tranquil island in the middle of the lake. A modest house with three doors stands before you.")
            time.sleep(1)
            print("One door is yellow, another blue, the last red. Which door will you walk through?")
            time.sleep(1)
            third_choice = input(Fore.MAGENTA + "Choose 'red', 'yellow', or 'blue' to proceed.").lower()
            if third_choice == 'red':
                print(Fore.RED + "You choose to enter the room of perilous flames. Game over.")
                return
            elif third_choice == 'yellow':
                print(Fore.YELLOW + "You found the treasure of the ancient kings! You win!")
            elif third_choice == 'blue':
                print(Fore.RED + "You choose the room of carnivorous beasts. Game over.")
                return
            else:
                print(Fore.RED + "You chose a door that doesn't exist. Game over.")
                return
        else:
            print(Fore.LIGHTWHITE_EX + "A wizard is unhappy with your lack of pluck.")
            return
    else:
        print(Fore.LIGHTWHITE_EX + "You have abandoned the quest.")
        return
    
def main():
    while True:
        play_adventure()
        replay = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye.")
            break
if __name__ == "__main__":
    main()
