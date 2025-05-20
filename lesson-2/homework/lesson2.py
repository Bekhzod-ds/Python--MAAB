# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input("What is your name? ").strip().title()
year = int(input(f"Hey {name}, What is your year of birth? "))

age = 2025 - year
print(f"{name}, your age is {age}!")

# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[1::2])
txt = 'MsaatmiazD'
print(txt[0::2])

#Extract the residence area from the following text:
txt = "I'am John. I am from London"
print(txt.split()[-1])

# Write a Python program that takes a user input string and prints it in reverse order.
txt = input("You can write anything to get it in reverse order: ")
print(txt[::-1])

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

text = input("Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum value:", max(numbers))


# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("Enter a word to check for palindrome: ").strip().lower()
if word == word[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")


# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Enter your email address: ").strip()
if '@' in email:
    domain = email.split('@')[-1]
    print("Domain:", domain)
else:
    print("Invalid email address.")


# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(chars, k=length))
print("Generated password:", password)

