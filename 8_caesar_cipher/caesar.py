def cipher(message, shift, direction):
  ascii_base_value = 32
  ascii_ceil_value = 126
  ascii_char_range = ascii_ceil_value - ascii_base_value + 1
  return_message = ""

  if direction == "encode" or direction == "e":
    def encode(message, shift_amount):
      encrypted_message = ""
      for letter in message:
        ascii_value = ord(letter)
        if ascii_value + shift_amount > ascii_ceil_value:
          ascii_value -= ascii_char_range
        ascii_value += shift_amount
        encrypted_message += chr(ascii_value)
      return encrypted_message
    return_message = encode(message, shift)

  else:
    def decode(message, shift_amount):
      decrypted_message = ""
      for letter in message:
        ascii_value = ord(letter)
        if ascii_value - shift_amount < ascii_base_value:
          ascii_value += ascii_char_range
        ascii_value -= shift_amount
        decrypted_message += chr(ascii_value)
      return decrypted_message
    return_message = decode(message, shift)

  return return_message