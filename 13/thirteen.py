import assets 
import random
import os 

# pick a random character from list
def pick_character(data):
    return random.choice(data)

def compare(option_a, option_b, choice):
    """
    Get the user guess and compare between the two options if user is 
    correct or not 
    """
    if choice == "A":
        return option_a['follower_count']  >= option_b['follower_count']  
    else:
        return option_b['follower_count'] >= option_a['follower_count']

def higher_lower():
    # determine if game is in session
    session = True 
    
    # score to keep track of user progress
    score = 0
    
    # initially load up characters
    characters = { 
                  "A": pick_character(assets.data), 
                  "B": pick_character(assets.data) 
                }
    
    while session:
        # clear screen before start of program
        os.system("clear")
        
        print("=" * 12)
        print(assets.logo)
        print("=" * 12)
        
        print(f"Compare A: {characters['A']['name']}, A {characters['A']['description']} from {characters['A']['country']}")
        print(assets.versus)
        print(f"Against B: {characters['B']['name']}, A {characters['B']['description']} from {characters['B']['country']}")
        choice = input("Who has more followers? Type 'A' or 'B' ")
        
        result = compare(characters['A'], characters['B'], choice)
        
        # if user gets answer correctly, increment count
        if result:
            characters['A'] = characters[choice]
            characters['B'] = pick_character(assets.data)
            
            score += 1
        else:
            print(f"Game over champ, your score is {score}")
            session = False
    
higher_lower()