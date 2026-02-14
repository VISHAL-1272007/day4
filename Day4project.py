import random
print("Welcome to Stone 🪨Paper📃 Scissors✂️!")
print("THIS GAME IS YOU❤️❤️VS COMPUTER🖥️💻 ")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'    ____)____
          _______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[rock, paper, scissors]
user_input=int(input("What do you choose?  Type 0 For ROCK🪨🪨,Type 1 For PAPER📰📃,Type 2 For SCISSORS✂️✂️"))
if 0 <= user_input <= 2:
    print(game_images[user_input])
computer_choice=random.randint(0,2)
print("Computer choice")
print(game_images[computer_choice])
if user_input==computer_choice:
    print("Match Draw📍🤝")
elif user_input==0 and computer_choice==1:
    print("You lose!")
    print("Get a better luck next time😊😉")
elif user_input==2 and computer_choice==1:
    print("You Win!")
    print("You Beat computer well done✅🤝🥳")
elif user_input==1 and computer_choice==2:
    print("you lose")
    print("Get a better luck next time😊😉")
elif user_input==2 and computer_choice==0:
    print("You lose")
    print("Get a better luck next time😊😉")
elif user_input==1 and computer_choice==0:
    print("You win")
    print("You Beat computer well done✅🤝🥳")
elif user_input==0 and computer_choice==2:
    print("You win")
    print("You Beat computer well done✅🤝🥳")
else:
    print("YOU INVALID NUMBER ")




