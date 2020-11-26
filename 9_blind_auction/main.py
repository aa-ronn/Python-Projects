from replit import clear
from art import logo
print(logo)

cont_bidding = False
bids = {}
name = ""
bid = 0
more_bidders = ""

print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What is your bid?: "))
bids[name] = bid
more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
if more_bidders == 'y' or more_bidders == 'yes':
  cont_bidding = True
clear()

while cont_bidding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))
  bids[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if more_bidders == 'y' or more_bidders == 'yes':
    cont_bidding = True
  else:
    cont_bidding = False
  clear()

highest_bid = {}
for bid in bids:
    if not highest_bid:
      highest_bid["name"] = bid
      highest_bid["bid"] = bids[bid]
    elif bids[bid] > highest_bid["bid"]:
      highest_bid["name"] = bid
      highest_bid["bid"] = bids[bid]
    elif bids[bid] == highest_bid["bid"]:
      highest_bid["name"] = "DRAW"
      highest_bid["bid"] = bid["bid"]

print(f"The winner is {highest_bid['name']} with a bid of ${highest_bid['bid']}")



