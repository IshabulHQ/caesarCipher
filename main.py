alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction,text,shift):
    message = ""
    for i in range(0, len(text)):
        location = alphabet.index(text[i])
        if (direction.lower() == "encode"):
            message += alphabet[location + shift]
        elif (direction.lower() == "decode"):
            message += alphabet[location - shift]
    print(f"Here's the {direction}d result: {message}")




should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(direction,text,shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

