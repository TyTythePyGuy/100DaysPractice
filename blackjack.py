import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo
print(logo)
def blackjack():
  
  your_cards = []
  computer_cards = []
  playing = True
  while playing == True:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
      for player in range(0,2):
        your_cards.append(random.choice(cards))
        score = sum(your_cards)
      print(f"Your cards: {your_cards}, current score: {score}")
      for computer in range(0,2):
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
      print(f"Computer's first card: {computer_cards[0]}")
      if computer_score == 21 and score != 21:
        print(f"Computer Blackjack! You lose.")
        playing = False
        blackjacklackjack()
      if score == 21:
        print(f"Blackjack!! Your score is {score}!")
        playing = False
        blackjack()
      hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
      if hit_me == 'y':
        your_cards.append(random.choice(cards))
        score = sum(your_cards)
        if score > 11:
          your_cards[0] = 1
        print(f"Your cards: {your_cards}, current score: {score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if score == 21 and computer_score < 21:
          print(f"Blackjack!! Your score is {score}")
          playing = False
          blackjack()
        elif score == 21 and computer_score == 21:
          print(f"Tie. You both have {score}")
          playing = False
          blackjack()
        elif score > 21:
          print(f"You busted, your score was {score}. You lose!")
          playing = False
          blackjack()
        elif computer_score <= 15:
          computer_cards.append(random.choice(cards))
          if computer_score > 21:
            print(f"You win, the computer bust with a score of {computer_score}")
            playing = False
          blackjack()
        else:
          hit_me
      else:
        print(f'Your final hand: {your_cards}, final score: {score}')
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        if score > computer_score:
          print("You win!")
          playing = False
          blackjack()
        else:
          print("Computer wins!")
          playing = False
          blackjack()
  
  
blackjack()
