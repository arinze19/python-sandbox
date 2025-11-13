from calculator_art import calculator



def calculator_app():
    print(f"""
    **************** WELCOME TO THE CALCULATOR APP ****************
    {calculator}
    """)

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def divide(a, b):
        return a / b

    def multiply(a, b):
        return a * b


    previous_number = None  

    while True:
        if not previous_number:
            first_number = float(input("What's your first number?: "))
        else:
            first_number = previous_number
            previous_number = None
            
        operation = input("What is your operation? (*, /, +, -): ")
        
        match operation:
            case "/":
                operation = divide
            case "+":
                operation = add
            case "-":
                operation = subtract
            case "*":
                operation = multiply
            case _:
                print("No operation matches your input, please try again from the following options (*, /, +, -)") # have a loop here until the user adds a valid option
                return None

        second_number = float(input("What's your second number?: "))
        result = operation(first_number, second_number)
        
        print(f"Your calculation result is {result}")
        
        choice = input("""
            Do you want to start a fresh calculation or do you want to add to your current result? 
            Y: to continue with previous result
            N: to start new calculations
            Q: to quit program
            """).lower()
        
        if choice == "y":
            previous_number = result
        elif choice == "q":
            return None
        else: 
            print("\n" * 20)

calculator_app()