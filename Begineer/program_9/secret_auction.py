from secret_auction_art import logo

bidding_finished = False

bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is : {winner} with a bid of ${highest_bid}")


print(logo)

while not bidding_finished:
    name = input("Enter your name? : ")
    bid = int(input(f"Hello Mr.{name}.\nWhat\'s your bid?\n$"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
