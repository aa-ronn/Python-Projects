def encode(message, shift_amount):
  encrypted_message = ""
  for letter in message:
    ascii_value = ord(letter)
    if ascii_value + shift_amount > 122:
      ascii_value -= 26
    ascii_value += shift_amount
    encrypted_message += chr(ascii_value)
  return encrypted_message
  
def decode(message, shift_amount):
  decrypted_message = ""
  for letter in message:
    ascii_value = ord(letter)
    if ascii_value - shift_amount < 97:
      ascii_value += 26
      if ascii_value < 97:
        ascii_value -= 26
    ascii_value -= shift_amount
    decrypted_message += chr(ascii_value)
  return decrypted_message

direction_correct_inputs = ['e', 'd', 'encode', 'decode']

direction = input("Type 'encode' to encode, type 'decode' to decode:\n").lower()
if direction not in direction_correct_inputs:
  print("Please input e, encode, d, or decode")
else:
  text = input("Type your message:\n").lower()
  try:
    shift = int(input("Type the shift number:\n"))
    if direction == "encode" or direction == 'e':
      encrypted_message = encode(text, shift)
      print(encrypted_message)
    elif direction == "decode" or direction == 'd':
      decrypted_message = decode(text, shift)
      print(decrypted_message)
  except ValueError:
    print("You can only shift by an integer value")