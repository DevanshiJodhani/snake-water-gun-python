#  snake water gun game!! 

import random


def check(computer, user):
    if(computer == user):
        return 0
    elif(computer == "water" and user == "snake"):
        return 1
    elif(computer == "gun" and user == "water"):
        return 1
    elif(computer == "snake" and user == "gun"):
        return 1
    else:
        return -1
        
def computer_choice():
    com = ["snake", "water", "gun"]
    return random.choice(com)

def check_winner():
    if(score == 1):
        return name
    elif(score == -1):
        return "computer"

def write_in_file():
    f = open("./day_55/score.txt", "a")
    lines = [f"{name} vs computer, {wineer} is winner and score is {score}\n"]
    f.writelines(lines)
    f.close()

name = input("enter your name:  ")
while True:
    print("Let's play the game !")
    user = int(input("Enter your choice: \nPress 1 for Snake.\nPress 2 for Water\nPress 3 for Gun\nPress 4 to end the game.\n"))

    if(user==1):
        user="snake"
    elif(user==2):
        user="water"
    elif(user==3):
        user="gun"
    else:
        print("Thank you for playing game!")

    computer = computer_choice()
    score = check(computer, user)
    print("computer choosen :- ", computer)
    print("And you choosen : -", user)
    if(score == 0):
        print("your game is tie !")
    elif(score == 1):
        print("you won the game ")
    else:
        print("you lose the game")
        
    print("Your score is :- ", score)

    wineer = check_winner()
    print(wineer)
    write_in_file()












