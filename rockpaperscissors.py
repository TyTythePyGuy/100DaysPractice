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
import random
play = "y"
while play == "y":
  user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
  if user >= 3 or user < 0:
    print("Invalid choice, you lose!")
  elif user == 0:
    print(rock)
  elif user == 1:
    print(paper)
  else:
    print(scissors)
  print("Computer Chose:")
  cpu = random.randint(0, 2)
  if cpu == 0:
    print(rock)
  elif cpu == 1:
    print(paper)
  else:
    print(scissors)
  if user == 0 and cpu == 1 or user == 1 and cpu == 2 or user == 2 and cpu == 0:
    print("You lose")
  if user == cpu:
    print("Draw")
  if user == 0 and cpu == 2 or user == 1 and cpu == 0 or user == 2 and cpu == 1:
    print("You win")
  play = input("This repl has exited, play again? y/n ")
