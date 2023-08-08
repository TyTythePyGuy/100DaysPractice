#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

### One way to solve this, using the join method.
password = ""

for number in range(0, nr_letters):
  if number < nr_letters:
    password += letters[random.randint(0, len(letters)-1)]
for number in range(0, nr_symbols):
  if number < nr_symbols:
    password += symbols[random.randint(0, len(symbols)-1)]
for number in range(0, nr_numbers):
  if number < nr_numbers:
    password += numbers[random.randint(0, len(symbols)-1)]
print(''.join(random.sample(password,len(password))))
### Another way to solve this, turning the password into a list and appending the list
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for  char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))
##A list has been created and for every input that amount of each item is chosen randomly and added to the list
random.shuffle(password_list)
##The list that was created is shuffled around so the items are in a different order
password2 = ""
for char in password_list:
  password2 += char
print(password2)
#After a new value is created the value from password_list is added to it so it presents
#as a string, not a list. The new password is then printed.
