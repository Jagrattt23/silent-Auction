# import os
print("*****WELCOME TO THE SILENT AUCTON PROGRAM*****")
def find_winner(bitter_details):
    highest_bid=0
    winner=""
    for bidder in bitter_details:
        bidding_price=bitter_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"here is the list of all bidders: {bitter_details}")        
    print(f"The  winner is {winner} with a bid price of {highest_bid}")




bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("what is your name?:\n")
    price=int(input("what is your bid price?:\n"))
    bidder_data[name]=price
    more_bidder=input("Are there any more bidder? Type 'yes' or 'no':\n").lower()
    if more_bidder=='no':
        end_of_bidding=True
        find_winner(bidder_data) 
    # elif more_bidder=="yes":
    #     os.system('cls')

                                                                       
