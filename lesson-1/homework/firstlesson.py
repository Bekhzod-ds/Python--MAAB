# Given a side of square. Find its perimeter and area.

a = int(input("What is a? "))
b = int(input("What is b? "))

P = 2 * (a + b)
print(f"Perimeter of the square is {P}")

# Given diameter of circle. Find its length.

d = int(input("What is the diameter? "))

C = 3,14 * d
print(f"The length of the circle = {C}")

#Given two numbers a and b. Find their mean.

a = int(input("What is a? "))
b = int(input("What is b? "))

M = (a + b) / 2
print(f"The mean is {M}")

#Given two numbers a and b. Find their sum, product and square of each number.

a = int(input("What is a? "))
b = int(input("What is b? "))

S = a + b
P = a * b
a2 = a**2
b2 = b**2
print(f"""The sum is {S}, while the product is {P}, and square of a = {a2}, b = {b2}. """)

