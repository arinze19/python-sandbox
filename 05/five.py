# Notes
# sum() - argument is an iterable item
# max() - gets the max item in an iterable item
# range(start, stop [not inclusive], step) - can only be used in a for_loop | not inclusive of the the last index
# shuffle() - shuffles an array/list

# lists = [1,15,30,9,20,100,23,18,27]
# max_score = 0

# for item in lists:
#     if item > max_score:
#         max_score = item
# print(max_score)

# Password generator
import random

print("Welcome to PyPassword Generator")

# Letters
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter = int(input("How many letters would you like in your password? \n"))
symbol = int(input("How many symbols would you like in your password? \n"))
number = int(input("How many numbers would you like in your password? \n"))

# char = [""] * (letter + symbol + number)
char = []

for num in range(letter):
    char.append(random.choice(letters))
for num in range(symbol):
    char.append(random.choice(symbols))
for num in range(number):
    char.append(random.choice(numbers))
    
random.shuffle(char)
    
print("".join(char))




# for num in range(letter):
#     # generate a random index from char
#     index = random.randint(0, len(char) - 1)
    
#     # if the index is not empty, generate another
#     while char[index] != "":
#         index = random.randint(0, len(char) - 1)
    
#     # insert random choice of letter into index
#     char[index] = random.choice(letters)

     
# for num in range(symbol):
#      # generate a random index from char
#     index = random.randint(0, len(char) - 1)
    
#     # if the index is not empty, generate another
#     while char[index] != "":
#         index = random.randint(0, len(char) - 1)
    
#     # insert random choice of letter into index
#     char[index] = random.choice(symbols)
    
# for num in range(number):
#      # generate a random index from char
#     index = random.randint(0, len(char) - 1)
    
#     # if the index is not empty, generate another
#     while char[index] != "":
#         index = random.randint(0, len(char) - 1)
    
#     # insert random choice of letter into index
#     char[index] = random.choice(numbers)
    
