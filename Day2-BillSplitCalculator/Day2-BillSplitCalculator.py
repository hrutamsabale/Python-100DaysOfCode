print("Welcome to the split calculator!\n")
total_bill=float(input("What is the total bill? $"))
tip_percent=float(input("What percent of the bill do you wish to tip? "))
tip=total_bill*(tip_percent/100)
people=int(input("How many people are paying? "))
perperson="{:.2f}".format(((total_bill+tip)/people))
tip_print="{:.2f}".format(tip)
print(f"Each person has to pay ${perperson}. Total tip is ${tip_print}.")
