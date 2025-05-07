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

