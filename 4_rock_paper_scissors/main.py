# namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
# names = namesAsCSV.split(", ")

# names.extend(["Chuck", "Zoey"])
# names.append("Phillip")

# print(names)

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇

# x = int(position[0]) - 1
# y = int(position[1]) - 1

# map[y][x] = "💰"

# # Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = []
choices.append({"name": "Rock", "art": rock})
choices.append({"name": "Paper", "art": paper})
choices.append({"name": "Scissors", "art": scissors})

# get and print user choice
choice = input("Rock, Paper or Sissors? ").lower()
if choice == "rock" or choice == "0":
    print(choices[0]["art"])
    print("You played " + choices[0]["name"])
elif choice == "paper" or choice == "1":
    print(choices[1]["art"])
    print("You played " + choices[1]["name"])
elif choice == "scissors" or choice == "2":
    print(choices[2]["art"])
    print("You played " + choices[2]["name"])

# print computer choice
computer_choice = random.randint(0, 2)
print(choices[computer_choice]["art"])
print("The computer played " + choices[computer_choice]["name"])

selections = str(choice)+str(computer_choice)
winning_conditions = ["01", "10", "21"]
draw_conditions = ["00", "11", "22"]

if selections in winning_conditions:
    print("You Won! 😁")
elif selections in draw_conditions:
    print("It's a draw! 🔫")
else:
    print("You lose! 👎")
