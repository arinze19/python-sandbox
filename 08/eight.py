def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# greet_with(location="Lagos", name="Arinze") key=word arguments

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 
             'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z'
             ]

direction = input("Type 'encode' to encode, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the number of shift: \n"))

def caesar_cipher(direction, text, shift):
    # wonder if it passes by reference or value
    result = []
    
    if direction == 'encode' or direction == 'decode':
        for char in text:
            try:
                index = alphabets.index(char)
                calculated_shift = index + shift if direction == "encode" else index - shift
                
                result.append(alphabets[(calculated_shift) % len(alphabets)]) 
            except ValueError:
                result.append(char)
    else:
        print("Oops, looks like we do not cover that operation in this program.")
        
    return "".join(result)


# is there short_hand for key=word arguments
print(caesar_cipher(direction, text, shift))