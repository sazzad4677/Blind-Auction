bids = {}
continue_bidding = True

while continue_bidding:
    bidder_name = input("What is your bidder name? ")
    bid_price = float(input("What is your bid price? $"))
    bids[bidder_name] = bid_price
    should_continue = input("Are there any bidders? Type 'Yes' or 'No'. \n ").lower()
    if should_continue != "yes" or should_continue != "no":
        print("Invalid input. Please try again.")
    if should_continue == 'no':
        continue_bidding = False
        winner = max(bids, key=bids.get)
        print("The winner is " + winner)
    elif should_continue == 'yes':
        print("\n" * 20)
        continue
