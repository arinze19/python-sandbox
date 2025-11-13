# print("Number of letters in your name", len(input("What is your name? ")))
# print(round(13.3532, 2))

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = round((float(input("How much tip would you like to give? ")) / 100), 2)
size = float(input("How many people should split the bill? "))
print("These are the variables", total, tip, size)
result = round(((total + (total * tip)) / size), 2)
print("Each person should pay:", result)

# Notes
# Type Casting - int(), str(), float(), bool()
# Value Error, Syntax Error,
# divisions always return a floating point number (implicit type_casting) || use "//" to floor division (more like a truncator)
# f string