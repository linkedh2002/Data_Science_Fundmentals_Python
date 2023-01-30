import random
print("-----------------------------------------")
print("Let's Play Rock🪨, paper📃, Scissors✂️")
print("-----------------------------------------")
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Type Rock/Paper/Scissors or Q to Quit the game: ").lower()
    if user_pick == "q":
        break

    if user_pick not in options:
        print("Please Enter the Valid input.")
        continue

    random_number = random.randint(0, 2)    #rock -> 0 ; paper -> 1 ; scissors -> 2
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick)

    if user_pick == "rock" and computer_pick == "scissors":
        print("You Won!🔥")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You Won!🔥")
        user_wins += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You Won!🔥")
        user_wins += 1

    else:
        print("You Lost!😏")
        computer_wins +=1
print("-----------------------------------------")
print("You Won", user_wins, "times.")
print("Computer Won", computer_wins, "times.")
print("-----------------------------------------")
print("GOODBYE!! THANKS FOR PLAYING!!!")