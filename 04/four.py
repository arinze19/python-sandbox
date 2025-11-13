import random

# print(random.randint(1, 10), random.random(), random.uniform(1, 10))
choices = ["Heads", "Tails"]
friends = ["Charlie", "Bob", "Alice", "Carlos", "Tevez"]

options = ["Rock", "Paper", "Scissors"]
 
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors \n")) # Come up with a better way to prevent adding strings
computer_choice = random.choice(options)

try:
    choice = options[choice]
    
    print("You chose: ", choice)
    print("Computer chose: ", computer_choice)
    
    if choice == computer_choice:
        print("This is a draw")
    elif choice == "Scissors" and computer_choice == "Paper":
        print("You Win!")
    elif choice == "Scissors" and computer_choice == "Rock":
        print("You Lose!")
    elif choice == "Rock" and computer_choice == "Paper":
        print("You Lose!")
    elif choice == "Rock" and computer_choice == "Scissors":
        print("You Win!")
    elif choice == "Paper" and computer_choice == "Rock":
        print("You Win!")
    elif choice == "Paper" and computer_choice == "Scissors":
        print("You Lose!")
    else: 
        print("You Lose!")
except IndexError:
    print("You have chosen an option that doesn't exist, You Lose!")



# Notes 
# 1. Index error
# 2. Randomisation
# 3. random.randint(a, b) - this is inclusive of both a and b
# 4. Modules 
# 5. list
#       - append(). 
#       - 
# 6. random.choice(...a sequence) | this is used for list 