# take input from user
greetings = ["Day One", "Day Two"]

for greeting in greetings:
    print(greeting)

name = input("What is your name? ")
print(len(name))

# Random name generator 
band_name = []
questions = ["What was the name of the city you grew up in?", "What was the name of your pet while growing up?"]
for question in questions:
    print(question)
    name = input("")
    band_name.append(name)
print("Your band name could be", " ".join(band_name))
