from art import logo
from art import vs
from game_data import data
import random
### Function to get all the values for the first person to be compared
def get_a():
  global a
  global a_name
  global a_fc
  global a_desc
  global a_country
  a = random.randint(0, 49)
  a_name = (data[a]['name'])
  a_fc = (data[a]['follower_count'])
  a_desc = (data[a]['description'])
  a_country = (data[a]['country'])

### Function to get all the values for the second person to be compared
def get_b():
  global b
  global b_name
  global b_fc
  global b_desc
  global b_country
  b = random.choice([i for i in range(50) if i != a and i != 49])
  b_name = (data[b]['name'])
  b_fc = (data[b]['follower_count'])
  b_desc = (data[b]['description'])
  b_country = (data[b]['country'])


print(logo)
score = 0
get_a()
print(f"Compare A: {a_name}, a {a_desc}, from {a_country}.")
print(vs)
get_b()
print(f"Against B: {b_name}, a {b_desc}, from {b_country}.")
### After initial values are created, allows the rest of the game to be played in a loop.
playing = True
while playing == True:
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  if guess == 'a':
    if max(a_fc, a_fc) == a_fc:
      score += 1
      print(f"You're right! Current score: {score}.")
      get_b()
      print(f"Compare A: {a_name}, a {a_desc}, from {a_country}.")
      print(vs)
      print(f"Against B: {b_name}, a {b_desc}, from {b_country}.")
      continue
    elif max(a_fc, b_fc) == b_fc:
      print(f"Sorry, that's wrong!! Final score: {score}.")
      playing = False
  if guess == 'b':
    if max(a_fc, b_fc) == b_fc:
      score += 1
      print(f"You're right! Current score: {score}.")
      a_name = b_name
      a_fc = b_fc
      a_desc = b_desc
      a_country = b_country
      get_b()
      print(f"Compare A: {a_name}, a {a_desc}, from {a_country}.")
      print(vs)
      print(f"Against B: {b_name}, a {b_desc}, from {b_country}.")
      continue
    elif max(a_fc, b_fc) == a_fc:
      print(f"Sorry, that's wrong!! Final score: {score}.")
      playing = False
