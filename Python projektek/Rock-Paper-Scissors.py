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

#Write your code below this line 👇

list = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input > 2 or user_input < 0:
    print("You typed an invalid number, you lose.")
    
else: 

    print(list[user_input])
    
    print("Computer chose:")
    
    print(list[computer_choice])
    
    
    if list[user_input] == paper and list[computer_choice] == paper:
        print("It's a draw.")
    elif list[user_input] == scissors and list[computer_choice] == scissors:
        print("It's a draw.")
    elif list[user_input] == rock and list[computer_choice] == paper:
        print("You lose.")
    elif list[user_input] == paper and list[computer_choice] == scissors:
        print("You lose.")
    elif list[user_input] == scissors and list[computer_choice] == rock:
        print("You lose.")
    elif  list[user_input] == rock and list[computer_choice] == rock:
        print("It's a draw.")
    else:
        print("You won!")




