
# 1. Modify String with Underscores
def modify_string_with_underscores(txt):
    result = []
    i = 0
    skip_next = False
    vowels = 'aeiouAEIOU'

    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0 and txt[i] not in vowels:
            if i + 1 < len(txt) and txt[i + 1] != '_':
                result.append('_')
        i += 1
    return ''.join(result).rstrip('_')

print(modify_string_with_underscores("hello"))       # hel_lo
print(modify_string_with_underscores("assalom"))     # ass_alom
print(modify_string_with_underscores("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef


# 2. Integer Squares with Error Handling
try:
    num_inputs = int(input("Enter a number: "))
    for number in range(num_inputs):
        print(number ** 2)
except ValueError:
    print("Invalid input. Please enter an integer.")


# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Exercise 3: Sum of all numbers to N
try:
    number = int(input("Enter a number: "))
    total_sum = sum(range(1, number + 1))
    print(f"Sum is: {total_sum}")
except ValueError:
    print("Please enter a valid integer.")

# Exercise 4: Multiplication table
try:
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(number * i)
except ValueError:
    print("Please enter a valid integer.")

# Exercise 5: Display specific numbers from a list
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)

# Exercise 6: Count total digits
num = 75869
print(f"Number of digits: {len(str(num))}")

# Exercise 7: Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Exercise 8: Reverse list
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# Exercise 9: Display -10 to -1
for i in range(-10, 0):
    print(i)

# Exercise 10: Print "Done" after loop
for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Print prime numbers between 25 and 50
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if is_prime(num):
        print(num)

# Exercise 12: Fibonacci up to 10 terms
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# Exercise 13: Factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"5! = {factorial(5)}")


# 4. Return Uncommon Elements of Lists
from collections import Counter

def uncommon_elements(list1, list2):
    """
    Return elements that are not common between two lists, including duplicates.
    Parameters:
        list1 (list): First list of elements.
        list2 (list): Second list of elements.
    Returns:
        list: Elements not common to both lists.
    """
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    result = []

    for elem in counter1:
        if elem not in counter2:
            result.extend([elem] * counter1[elem])
    for elem in counter2:
        if elem not in counter1:
            result.extend([elem] * counter2[elem])
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]

