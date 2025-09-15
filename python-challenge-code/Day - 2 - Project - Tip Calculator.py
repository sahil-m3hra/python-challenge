# Write a python program to calculate the bill and split among friends including tip.
# Tasks:
# Accept: What is the total bill? $
# Accept: How much tip would you like to give? 10, 12 or 15?
# Accept: How many people to split the bill?
# Output: Each person should pay: $xxx.xx

bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")