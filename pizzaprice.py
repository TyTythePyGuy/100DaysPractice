### This is how **I** finished the challenge
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sbill = 15
mbill = 20
lbill = 25
if size == "S":
    if add_pepperoni == "Y":
        sbill += 2
        if extra_cheese == "Y":
            sbill += 1
            print(f"Your final bill is: ${sbill}.")
        else:
            print(f"Your final bill is: ${sbill}.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            sbill += 1
            print(f"Your final bill is: ${sbill}.")
        else:
            print(f"Your final bill is: ${sbill}.")
if size == "M":
    if add_pepperoni == "Y":
        mbill += 3
        if extra_cheese == "Y":
            mbill += 1
            print(f"Your final bill is: ${mbill}.")
        else:
            print(f"Your final bill is: ${mbill}.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            sbill += 1
            print(f"Your final bill is: ${mbill}.")
        else:
            print(f"Your final bill is: ${mbill}.")
if size == "L":
    if add_pepperoni == "Y":
        lbill += 3
        if extra_cheese == "Y":
            lbill += 1
            print(f"Your final bill is: ${lbill}.")
        else:
            print(f"Your final bill is: ${lbill}.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            lbill += 1
            print(f"Your final bill is: ${lbill}.")
        else:
            print(f"Your final bill is: ${lbill}.")

### This is the most efficient way to finish the challenge
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
