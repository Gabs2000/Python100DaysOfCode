# Tip Calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))

total = (total_bill * (tip_percentage / 100) + total_bill) / people_to_split
print(f'Each person should pay: {total}')