alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
from art import logo
should_continue = True
while should_continue:
  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += char


    print(f"Here's the {cipher_direction}d result: {end_text}")
  #Import and print the logo from art.py when the program starts.
  print(logo)
  #Created a while loop that continues to execute the program if the user types 'yes'.

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #Added some code so that the program continues to work even if the user enters a shift number greater than 26.
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Do you want to go again? Type yes or no ")
  if result == "no":
    should_continue = False
