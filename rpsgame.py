import os
import random
import time
from rps_functions import gesture, get_hand, splash_screen
from colors import bcolors
from msvcrt import getwch

os.system('cls')

print(bcolors.HEADER + bcolors.BOLD)
splash_screen("START")

wins = 0
losses = 0
plays = 0

while True:
    print(bcolors.YELLOW + "___________________________________")
    print("(R)ock, (P)aper, (S)cissors: ")

    while True:                             # Check keystrokes
        human_select = getwch().upper()
        if human_select == "Q":
            print(bcolors.HEADER + bcolors.BOLD, end="")
            splash_screen("QUIT")
            print(bcolors.ENDC)
            time.sleep(2)
            exit()

        if human_select == "0" or human_select == "1" or human_select == "2" or human_select == "R" or human_select == "P" or human_select == "S":
            break

    ai_select = random.randint(0, 2)

    human = get_hand(human_select)
    ai = get_hand(str(ai_select))

    os.system('cls')

    plays += 1

    print("The AI chose:", end="")
    gesture(ai)
    print("You chose:", end="")
    gesture(human)

    if ai == human:
        print(bcolors.CYAN + bcolors.BOLD + "IT'S A TIE" + bcolors.ENDC)
    elif human == "ROCK":
        if ai == "SCISSORS":
            print(bcolors.GREEN + bcolors.BOLD + "YOU WON!" + bcolors.ENDC)
            wins += 1
        else:
            print(bcolors.FAIL + bcolors.BOLD + "YOU LOST" + bcolors.ENDC)
            losses += 1
    elif human == "PAPER":
        if ai == "ROCK":
            print(bcolors.GREEN + bcolors.BOLD + "YOU WON!" + bcolors.ENDC)
            wins += 1
        else:
            print(bcolors.FAIL + bcolors.BOLD + "YOU LOST" + bcolors.ENDC)
            losses += 1
    elif human == "SCISSORS":
        if ai == "PAPER":
            print(bcolors.GREEN + bcolors.BOLD + "YOU WON!" + bcolors.ENDC)
            wins += 1
        else:
            print(bcolors.FAIL + bcolors.BOLD + "YOU LOST" + bcolors.ENDC)
            losses += 1
    print(f"Wins: {str(wins)} | Losses: {losses} | Turns: {plays}")
