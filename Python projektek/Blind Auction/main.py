from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.

should_continue = True
print(logo)

bidders = {}

while should_continue:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  
  bidders[name] = bid
  
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  if other_bidders == "no":
    should_continue = False

  clear()


winner = ""
winner_bid = 0
for bidder in bidders:
  if bidders[bidder] > winner_bid:
    winner = bidder
    winner_bid = bidders[bidder]

print(f"The winner is {winner} with a bid of ${winner_bid}.")

    
  





