##This is how I solved it##
def prime_checker(number):
    comp = False
    if n == 1:
        print("It's not a prime number.")
    elif n > 1:
        for num in range(2, number):
            if (n % num) == 0:
                comp = True
                break
        if comp:
            print("It's not a prime number.")
        if not comp:
            print("It's a prime number.")






#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

###This is the code to solve from Dr. Angela##
