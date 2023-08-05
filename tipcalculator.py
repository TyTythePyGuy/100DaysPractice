#Welcomes the user to the tip calculator, letting them know what it is.
print("Welcome to the tip calculator!")
#Created a value for the bill while also asking for it
bill = input("What was the total bill? $")
#created a value for the tip while also asking for it and letting them know not to add a percent sign
tip = input("What percentage tip would you like to leave? Do not add a percent sign. ")
#created a value for total people splitting the bill
people = input("How many people are splitting the bill? ")
#converted the bill, tip, and people to a float
billflt = float(bill)
tipflt = float(tip)
peopleflt = float(people)
#did the calculations for the total with tip split between all people
total = round((billflt/peopleflt) * (1 + tipflt/100), 2)
#used an f-string to print the amount that each person should pay.
print(f"Each person should pay ${total}")
