from art import icon
import random 

print(
    f"""
    ===================== THIS IS GUESSER ============================================
    {icon}
    ===================== THIS IS GUESSER ============================================
    Welcome to Guesser!
    I'm thinking of a number from 1 to 100.
    """
    )

# select a difficulty level 
session = True
difficulty = None
trials = 0
secret_number = random.randint(0, 100)

while session:
    # try to use "not diffi"
    while difficulty != "easy" and difficulty != "hard":
        difficulty = input("Please input a difficulty level. Type 'easy' or 'hard': ")
        
        if difficulty == "easy":
            trials = 10
        elif difficulty == "hard":
            trials = 5
    
    guess = int(input("Make a guess: "))
    
    print("\n")
    if guess == secret_number:
        print("Congratulations, you have won the game! 🏆")
        session = False
    elif guess < secret_number: 
        trials -= 1
        print(
            "Your guess is too low \n"
            "Guess again. \n"
            f"You have {trials} attempts left. \n\n\n"
        )
    else:
        trials -= 1
        print(
            "Your guess is too high \n"
            "Guess again. \n"
            f"You have {trials} attempts left. \n\n\n"
        )
    
    if not trials:
        print("You have lost the game, Better luck next time champ 😭")
        session = False
    
    
        
    
    
    

