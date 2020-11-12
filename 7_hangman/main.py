import random
from os import system, name 

def cls(): 
    #windows 
    if name == 'nt': 
        _ = system('cls') 
    #mac and linux
    else: 
        _ = system('clear') 

#get a radom work from the list
from hangman_words import word_list
chosen_word = random.choice(word_list)

#for test display the correct word
#print(f'Winning word is {chosen_word}')

word_length = len(chosen_word)
display = ['_'] * word_length
guessed_letters = []
lives = 6

from hangman_art import stages
from hangman_art import logo
print(logo)

while True:
  #cls()
  print(stages[lives])
  print(" ".join(display))
  guess = input("GUESS A LETTER: ").lower()
  
  #check if letter
  if not guess.isalpha():
    print("\nOnly letters please! You loose a life for being silly.")

  #check if letter has already be guessed
  if guess in guessed_letters:
    print("\nThat letter has already be guessed, try again.")
    continue
  else:
    guessed_letters.append(guess)
    
  if guess in chosen_word:
    for i in range(word_length):
      letter = chosen_word[i]
      if letter == guess:
          display[i] = letter
  else:
    lives -= 1
    if lives <= 0:
      print(stages[lives])
      print("\nYou lose, you ran out of lives! Hangman!")
      print(f"The word was {chosen_word}")
      break
    else:
      print(f"\n'{guess}' is not in the word you have {lives} lives left")

  if '_' not in display:
    print(f"\nYou win! The word was {chosen_word}")
    break