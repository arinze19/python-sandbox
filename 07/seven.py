import random
import hangman_art
import words 

lives = 6

# get a random item from word_list 
word = random.choice(words.animals)

# create a string variable and assign the length into it
template = ["_"] * len(word)


while "_" in template and lives > 0: 
    print(f"************************* You have {lives}/6 lives left *************************")
    user_input = input("Guess a letter: ").lower()
    
    if user_input in template:
        print(f"************************* Oops, looks like you have entered {user_input} before, Try another letter *************************")
    else:
        for index, character in enumerate(word):
            # verify if character in user input
            if character == user_input:
                template[index] = character
                
        # decrease lives score
        if user_input not in word:
            print(f"****************************** {user_input} is not a part of our secret word ******************************")
            lives -= 1
            
        print("".join(template)) # let the user know of their progress
        print(hangman_art.stages[len(hangman_art.stages) - (lives + 1)])
    
if lives == 0:
    print("****************************** Game Over. You lose! ******************************")
    print(f"************ the selected word was {word} ************")
else: 
    print("****************************** You Win! ******************************")