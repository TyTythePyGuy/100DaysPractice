from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

def start():
  print(logo)
  print("Hello, welcome to the secret bidding auction.")


def winner(d):
  return max(d, key = d.get)


bids = {}
bidding = True

start()
while bidding == True:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  bids[name] = bid
  next_user = input("Are there any other bidders? y/n ")
  if next_user == 'n':
    bidding = False
    winner(bids)
    winning_name = winner(bids)
    winning_bid = bids[winner(bids)]
  clear()
print(f"The winner is {winning_name} with a bid of ${winning_bid}.")
###Below this is how you would actually loop through the dictionary, instead of just gathering the highest value like I did###
# from replit import clear
# from art import logo
# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
