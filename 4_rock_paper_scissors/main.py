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

valid_input = True
choices = []
choices.append({"name" : "Rock", "art" : rock})
choices.append({"name" : "Paper", "art" : paper})
choices.append({"name" : "Scissors", "art" : scissors})

#get and print user choice
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
else:
  print("You can only input 'Rock', 'Paper', 'Scissors', or a number between 0-2")
  valid_input = False

if valid_input:
  #print computer choice
  computer_choice = random.randint(0,2)
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
