# The Idea Picker
# By: John Fiore - 08/19/2024

import random
import os
import platform

responses = [
    "Let's go with",
    "Try out",
    "What about",
    "I pick",
    "Go with"
]

def randResp():
    return random.choice(responses)

def clearcon():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def pause():
    print("\nType 'reroll' to go again, or 'exit' to close the app.")
    while True:
        inp = input("> ").strip().lower()
        if inp == "reroll":
            return True
        elif inp == "exit":
            return False
        else:
            print("Invalid input. Please type 'reroll' or 'exit'.")

def main():
    while True:
        clearcon()
        print("Hello! What would you like me to decide for you?")
        inp1 = input("1. ")
        inp2 = input("2. ")

        # Randomize between the two inputs
        rand = random.choice([1, 2])

        if rand == 1:
            print(randResp(), inp1)
        else:
            print(randResp(), inp2)

        # Pause and handle reroll or exit
        if not pause():
            break

def open():
    clearcon()
    print("======[IDEA PICKER]======")
    print("        1. Start         ")
    print("        2. Exit          ")
    print("=========================")
    print("v1.0")
    print("(c) 2024 John Fiore")
    print("=========================")
    
    inp = input("> ")

    if inp == "1":
        main()
    else:
        print("Closing.")

if __name__ == "__main__":
    open()
