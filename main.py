rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player_name = input("What is your Name?\n")
choose = int(input(f"{player_name}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
bot_choice = random.randint(0, 2)

if choose == 0 and bot_choice == 0:
  print(f"{player_name} chose\n{rock}")
  print(f"Computer chose\n{rock}")
  print("Its a draw. Try again")
elif choose == 1 and bot_choice == 0:
  print(f"{player_name} chose\n{paper}")
  print(f"Computer chose\n{rock}")
  print(f"{player_name} WINS!")
elif choose == 2 and bot_choice == 0:
  print(f"{player_name} chose\n{scissors}")
  print(f"Computer chose\n{rock}")
  print(f"{player_name} LOSES")
elif choose == 0 and bot_choice == 1:
  print(f"You chose\n{rock}")
  print(f"Computer chose\n{paper}")
  print(f"{player_name} LOSES")
elif choose == 0 and bot_choice == 2:
  print(f"You chose\n{rock}")
  print(f"Computer chose\n{scissors}")
  print(f"{player_name} WINS!")
elif choose == 1 and bot_choice == 1:
  print(f"You chose\n{paper}")
  print(f"Computer chose\n{paper}")
  print("Its a draw. Try again")
elif choose == 1 and bot_choice == 2:
  print(f"You chose\n{paper}")
  print(f"Computer chose\n{scissors}")
  print(f"{player_name} LOSES")
elif choose == 2 and bot_choice == 1:
  print(f"You chose\n{scissors}")
  print(f"Computer chose\n{paper}")
  print(f"{player_name} WINS!")
else:
  print("You typed an invalid entry, Try again.")