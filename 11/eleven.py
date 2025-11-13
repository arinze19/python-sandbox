import os 
import random
from art import blackjack_art

class Cards():
    def __init__(self):
        self.computer = []
        self.human = []
        self.deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        
        for _ in range(2):
            self.human.append(random.choice(self.deck))
            self.computer.append(random.choice(self.deck))
            
        # choice = random.randint(0, 1)
        
        # # I wonder if we can do "and choice"
        # while sum(self.computer) < 21 and choice == 1:
        #     self.computer.append(random.choice(self.deck))
        #     choice = random.randint(0, 1)
            
    def hit(self):
        # add a card to the human
        self.human.append(random.choice(self.deck))
        
        # determine if to add card to computer
        # I wonder if we can do "and choice"
        if random.randint(0, 1) == 1:
            self.computer.append(random.choice(self.deck))
            
        self.auto_check()
            
        # determine if to add a card to the computer 
        # if human or computer over 21, game over 
            
    def display_human(self):
        return self.human
        
    def display_computer(self):
        return self.computer
        
    def auto_check(self):
        if (sum(self.human) > 21):
            print("===================")
            print("Game over, You went over 21 😭. Your deck: ", self.human)
            print("===================")
            
        return None
    def display_result(self):
        if sum(self.computer) > sum(self.human):
            return "You lost  😭"
        elif sum(self.human) > sum(self.computer):
            return "You won 🏆"

      
        
# on select of no, compare and assign winner

def blackjack():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    
    while start == 'y':
        os.system("clear")
        
        print(blackjack_art)
        
        cards = Cards()
        
        # display user card and computers first card 
        print(f"Your cards: {cards.display_human()}, current score: {sum(cards.display_human())}")
        print(f"Computer's first card: {cards.display_computer()[0]}")
        
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        if choice == 'y':
            cards.hit()
        else:
            # display all cards 
            print(f"Your final hand: {cards.display_human()}, final score {sum(cards.display_human())}")
            print(f"Computer's final hand: {cards.display_computer()}, final score {sum(cards.display_computer())}")
            print(cards.display_result())
        
        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    print("It's a shame to see you go. Come back again some other time!")
      
blackjack()