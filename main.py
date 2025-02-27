import os

bids = {}
continue_bidding = True

while continue_bidding:
    bidder_name = input("What is your bidder name? ")
    bid_price = float(input("What is your bid price? $"))
    bids[bidder_name] = bid_price
    
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    
    if should_continue not in ["yes", "no"]:
        print("Invalid input. Please type 'Yes' or 'No'.")
        continue
    
    if should_continue == 'no':
        continue_bidding = False
        winner = max(bids, key=bids.get)
        print(f"The winner is {winner} with a bid of ${bids[winner]:.2f}")
    elif should_continue == 'yes':
        print("\n" * 20)
