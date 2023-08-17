import random
def game():
  guessing = True
  def logo():
    logo = """
                               ('-.    .-')     .-')            ('-.               .-') _             _   .-')   .-. .-')    ('-.  _  .-')   
                             _(  OO)  ( OO ).  ( OO ).         ( OO ).-.          ( OO ) )           ( '.( OO )_ \  ( OO ) _(  OO)( \( -O )  
      ,----.    ,--. ,--.   (,------.(_)---\_)(_)---\_)        / . --. /      ,--./ ,--,' ,--. ,--.   ,--.   ,--.);-----.\(,------.,------.  
     '  .-./-') |  | |  |    |  .---'/    _ | /    _ |         | \-.  \       |   \ |  |\ |  | |  |   |   `.'   | | .-.  | |  .---'|   /`. ' 
     |  |_( O- )|  | | .-')  |  |    \  :` `. \  :` `.       .-'-'  |  |      |    \|  | )|  | | .-') |         | | '-' /_)|  |    |  /  | | 
     |  | .--, \|  |_|( OO )(|  '--.  '..`''.) '..`''.)       \| |_.'  |      |  .     |/ |  |_|( OO )|  |'.'|  | | .-. `.(|  '--. |  |_.' | 
    (|  | '. (_/|  | | `-' / |  .--' .-._)   \.-._)   \        |  .-.  |      |  |\    |  |  | | `-' /|  |   |  | | |  \  ||  .--' |  .  '.' 
     |  '--'  |('  '-'(_.-'  |  `---.\       /\       /        |  | |  |      |  | \   | ('  '-'(_.-' |  |   |  | | '--'  /|  `---.|  |\  \  
      `------'   `-----'     `------' `-----'  `-----'         `--' `--'      `--'  `--'   `-----'    `--'   `--' `------' `------'`--' '--' 
    """
    print(logo)
  logo()
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  number = random.randint(1, 100)
  #print(number)
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    attempts = 10
  elif difficulty == 'hard':
    attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.")
  while guessing == True:
  
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"You win! The number was! {guess}")
      guessing = False
    elif guess > number:
      print("Too high! Guess again!")
      attempts -= 1
      print(f"You have {attempts} attempts remaining.")
    elif guess < number:
      print("Too low. 😕 Guess again!")
      attempts -= 1
      print(f"You have {attempts} attempts remaining")
    if attempts == 0:
      print(f"You lose, the number was {number}.")
      guessing = False

game()
