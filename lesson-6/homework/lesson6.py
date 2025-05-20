# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore to the next character.No underscore should be added at the end.

def insert_underscores(txt):
    result = ''
    i = 0
    count = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3:
            if txt[i] in 'aeiouAEIOU' or (i + 1 < len(txt) and txt[i+1] == '_'):
                if i + 1 < len(txt):
                    result += txt[i+1]
                    i += 1
            if i + 1 < len(txt):
                result += '_'
            count = 0
        i += 1
    return result

print(insert_underscores("hello"))         # Output: hel_lo
print(insert_underscores("assalom"))       # Output: ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  # Output: abc_abc_abcd_abcd_abcdef


# 2. Integer Squares Exercise
# Print squares of numbers from 0 to n-1

n = int(input("Enter a number: "))
for i in range(n):
    print(i ** 2)


# Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Exercise 3: Calculate sum from 1 to n
n = int(input("Enter number: "))
total = sum(range(1, n + 1))
print("Sum is:", total)

# Exercise 4: Multiplication table of a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

# Exercise 5: Display specific numbers from a list
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0 and num <= 150:
        print(num)

# Exercise 6: Count number of digits
num = int(input("Enter a number: "))
print("Number of digits:", len(str(abs(num))))

# Exercise 7: Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8: Print list in reverse using loop
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

# Exercise 9: Display numbers from -10 to -1
for i in range(-10, 0):
    print(i)

# Exercise 10: Display message "Done" after loop
for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Print all prime numbers in range
start, end = 25, 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12: Fibonacci series up to 10 terms
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b
print()

# Exercise 13: Factorial of a number
n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")


# 4. Return Uncommon Elements of Lists
# Return the elements that are not common between two lists

def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for elem in set(list1 + list2):
        count = abs(c1[elem] - c2[elem])
        result.extend([elem] * count)
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))           
print(uncommon_elements([1, 2, 3], [4, 5, 6]))          
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  
