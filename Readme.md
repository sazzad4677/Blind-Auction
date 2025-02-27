# Silent Auction Bidding System

This Python program implements a simple **silent auction** where multiple bidders can submit their bids. The highest bidder wins.

## Features
- Accepts multiple bidders' names and their bid amounts.
- Ensures valid numerical input for bids.
- Continues accepting bids until users decide to stop.
- Clears the screen after each bid for a fair auction experience.
- Announces the highest bidder at the end.

## How to Use
1. Run the script in a Python environment.
2. Enter the name of the bidder.
3. Enter the bid amount (must be a number).
4. When prompted, type `"Yes"` to add another bidder or `"No"` to end the bidding.
5. The program announces the highest bidder and their bid amount.

## Example Run
```
What is your bidder name? Alice
What is your bid price? $100
Are there any other bidders? Type 'Yes' or 'No': Yes

What is your bidder name? Bob
What is your bid price? $150
Are there any other bidders? Type 'Yes' or 'No': No
The winner is Bob with a bid of $150.00
```

## Requirements
- Python 3.x
- Works on Windows, macOS, and Linux

## Notes
- If an invalid bid amount is entered, the program will ask for a valid input.
- If a user enters an invalid response for continuing, it will prompt them again.

## License
This project is open-source and free to use.