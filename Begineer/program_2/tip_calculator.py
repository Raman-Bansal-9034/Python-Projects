print("\nWelcome to the tip calculator!\n")

total_bill = float(input("What was the total bill? $"))  # Converting string to float

tip_percentage = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))

number_of_people = int(input("How many people want to split the bill? "))

new_total_bill_with_tip = ((100+tip_percentage)/100)*total_bill

bill_per_person = "{:.2f}".format(round(new_total_bill_with_tip/number_of_people, 2))

# To round off to 2 digit after decimal. Add if number derived does not contain 2 digits after decimal, show 0 instead.
# .format() to convert to string in a particular format.

print(f"\nEach person should pay: ${bill_per_person}")
