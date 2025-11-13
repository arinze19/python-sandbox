from art import gavel

print(gavel)
print("Welcome to Silent Bidder")

bids = {}
choice = True
# while the choice is true display the game logic 
# Ask for user name and bid 
# ask if there is still another user
# repeat process until no more bids are in place.
# loop through the dictionary and determine the one with the highest bid 

while choice:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n$"))
    
    bids[name] = bid
    
    user_input = input("Are there any other bidders? \n").lower()
    
    if user_input == "no":
        choice = False
    elif user_input == "yes":
        print("\n" * 100)
    else: 
        choice = False
        print("Not a viable option, closing for safe measures")
    
winner = ""
score = 0


for key, value in bids.items():
    if value > score:
        score = value
        winner = key
        
print(f"The winner of the bid is {winner} with ${score}")
    