from caesar import cipher
from art import logo
from console import cls

print(logo)

direction_correct_inputs = ['e', 'd', 'encode', 'decode']

go = True
while go:
  direction = input("Type 'encode' to encode, type 'decode' to decode:\n").lower()
  if direction not in direction_correct_inputs:
    print("Please input e, encode, d, or decode")
  else:
    text = input("Type your message:\n")
    try:
      shift = int(input("Type the shift number:\n"))
      message = cipher(text, shift, direction)
      print(message)
    except ValueError:
      print("You can only shift by an integer value")

  restart = input("\n\nStart over (Y/N)?")
  if restart == "Y" or restart == "y":
    cls()
  else:
    go = False

print("Well, hopefully it worked. Bye!")