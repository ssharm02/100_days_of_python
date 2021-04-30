import bidding_art
print(bidding_art.logo)

bidding_dictionary = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, they won with a bid of ${highest_bid}")


def highest_bid():
    bidding_finished = False
    while not bidding_finished:
        user_name = input("What is your name? ")
        user_bid = int(input("what is your bid? $"))

        bidding_dictionary[user_name] = user_bid

        user_choice = input("Do you want to bid yes or no? ")
        if user_choice == "no":
            bidding_finished = True
            find_highest_bidder(bidding_dictionary)
        elif user_choice == "yes":
            print('\n' * 25)


highest_bid()