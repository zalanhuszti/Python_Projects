#import random, logos and the dataset

import random
from art import logo, vs
from game_data import data
from replit import clear

#choosing_item function to choose a random item from the game data
def choosing_item():
  dataset_length = len(data)
  index = random.randint(0, dataset_length - 1)
  return data[index]

#Creating the compare function

def checking_answer(a_followers, b_followers, player_guess):
  
  if a_followers["follower_count"] > b_followers["follower_count"] and player_guess == "a":
    return True
  elif a_followers["follower_count"] < b_followers["follower_count"] and player_guess == "b":
    return True
  else:
    return False

#Creating a function, which prints the information for the player
def printing_information(celebrity):
  return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}."

player_score = 0
is_game_over = False

while not is_game_over:
  print(logo)
  if player_score > 0:
    print(f"You're right! Current score: {player_score}.")
  
  if player_score == 0:
    a_celebrity = choosing_item()
  b_celebrity = choosing_item()

  while a_celebrity == b_celebrity:
    b_celebrity = choosing_item()
  
  a_printed_information = printing_information(a_celebrity)
  print(f"Compare A: {a_printed_information}")
  print(vs)
  b_printed_information = printing_information(b_celebrity)
  print(f"Against B: {b_printed_information}")
  
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if checking_answer(a_celebrity, b_celebrity, guess):
    player_score += 1
    a_celebrity = b_celebrity
    clear()
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {player_score}")
    is_game_over = True




  
  
    
    