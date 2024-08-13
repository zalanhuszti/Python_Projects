
import random
from replit import clear
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  else:
    return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)
  
  is_game_over = False
  user_cards = []
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  
  computer_cards = []
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())
  
  while not is_game_over:
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
      
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
      draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
       
      
    if draw_another_card == "y":
      user_cards.append(deal_card())
    else:
      is_game_over = True
      
  
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


