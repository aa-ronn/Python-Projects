import time

# 1. Create a greeting for your program.
print("Hey there, welcome to The Band Name Generator")
# 2. Ask the user for the city that they grew up in.
city = input("What city did you grow up in?\n")
# 3. Ask the user for the name of a pet.
pet = input("What is the name of your pet?\n")
# 4. Combine the name of their city and pet and show them their band name.

print("Your band name could be...\n")

# Add a Loading indicator for no reason whatsoever
for x in range(0, 5):
    b = "Loading" + "." * x
    print(b, end="\r")
    time.sleep(.200)

print("The " + city + " "+pet)
# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
