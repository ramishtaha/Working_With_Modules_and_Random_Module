# Importing the Random Module
import random

# Symbols to use in the game
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

# A list of Actions
actions = [rock, paper, scissors]

print("Welcome to the Game 'Rock Paper Scissors'\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Generate a Random choice for the Computer
computer_choice = random.randint(0, 2)

# Print out the Symbol User Chose
print("You Choose:")
print(actions[user_choice])

# Print out the Random Choice the computer choose
print("Computer chose:")
print(actions[computer_choice])

# Conditional Statements to Check The result of the Game
if computer_choice == user_choice:
    print("Draw!")

else:
    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (
            user_choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("You Loose!")
