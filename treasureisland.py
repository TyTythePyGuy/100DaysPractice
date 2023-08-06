#I created a choose your own adventure game with multiple routes.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'. ")
if crossroad == "left":
  lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
  if lake == "wait":
    island = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ")
    if island == "blue":
      print("You open the door and are greated by goblins. They look hungry and have a fire going. Game Over.")
    elif island == "red":
      print("You enter the house, there is a treasure chest in the middle. As you walk towards it you are engulfed in flames. Game Over.")
    elif island == "yellow":
      print("You enter the yellow door. The room is filled with treasure, now how will you get it back? Congratulations, you win!")
    else:
      print("You waited too long to decide, a turtle got the money before you. Game Over")
  else:
    print("You are swallowed whole by a giant trout. Is that a wooden doll? This will be your grave.")
else:
  print("You fell into a hole. You are dead")

