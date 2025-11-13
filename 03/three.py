# Modulo 
pizzas = {
    "L":  {
        "base": 25,
        "pepperoni": {
            "Y": 3,
            "N": 0
        },
        "cheese": {
            "Y": 1,
            "N": 0
        }
     },
    "M": {
        "base": 20,
        "pepperoni": {
            "Y": 3,
            "N": 0
        },
         "cheese": {
            "Y": 1,
            "N": 0
        }
        },
    "S": {
        "base": 15,
        "pepperoni": {
            "Y": 0,
            "N": 0
        },
         "cheese": {
            "Y": 1,
            "N": 0
        }
    }
}

print("Welcome to Python Pizza Deliveries")

amount = 0
size = input("What size of Pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

amount += pizzas[size]["base"] + pizzas[size]["pepperoni"][pepperoni] + pizzas[size]["cheese"][extra_cheese]
print(f"Your bill is ${amount}")

# Notes
# and | or | not
# 



