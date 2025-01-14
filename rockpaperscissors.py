import random
import sys

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

choice = input("What do you Choose? Type 0 for Rock, 1 for Paper, 2 for Scissors ")
if choice == "0":
    print("You chose rock " + rock)
elif choice == "1":
    print("You chose paper " + paper)
elif choice == "2":
    print("You chose scissors " + scissors)
else:
    print("You did not input one of the choices.")
    sys.exit()
# Randomizer for bot
rock_paper_scissors = [rock, paper, scissors]
bot_picker = random.choice(rock_paper_scissors)

if bot_picker == rock:
    print("The bot chose rock " + rock)
if bot_picker == paper:
    print("The bot chose paper " + paper)
if bot_picker == scissors:
    print("The bot chose scissors " + scissors)

# Game outcome
user_input = rock_paper_scissors[int(choice)]

if user_input == bot_picker:
    print("Tie.")
elif choice == "0" and bot_picker == scissors:
    print("You win.")
elif choice == "1" and bot_picker == rock:
    print("You win.")
elif choice == "2" and bot_picker == paper:
    print("You win.")
else:
    print("You lose")

