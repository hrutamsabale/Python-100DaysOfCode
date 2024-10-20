from replit import clear
bidders={}
to_continue=True
while to_continue:
  name=input("Enter your name: ")
  bid=int(input("Enter your bid $"))
  bidders[name]=bid
  choice=input("Are there any more bidders? ").lower()
  if choice=="no":
    to_continue=False
  clear()
highest_bid=0
bidders_name=""
for bidder in bidders:
  if bidders[bidder]>highest_bid:
    highest_bid=bidders[bidder]
    bidders_name=bidder
print(f"The highest bid is for ${highest_bid} by {bidders_name}")
