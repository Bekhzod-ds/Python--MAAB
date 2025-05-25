import math
from datetime import datetime

# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 2. Person Class
class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age


# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero."
        return a / b


# 4. Shape and Subclasses
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# 5. Binary Search Tree
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.key:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value > self.key:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def search(self, value):
        if value == self.key:
            return True
        elif value < self.key and self.left:
            return self.left.search(value)
        elif value > self.key and self.right:
            return self.right.search(value)
        return False


# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return "Stack is empty."
        return self.items.pop()


# 7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total(self):
        return sum(self.items.values())


# 9. Stack with Display
class StackWithDisplay:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty."
        return self.stack.pop()

    def display(self):
        print("Stack contents:", self.stack)


# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty."
        return self.queue.pop(0)


# 11. Bank Class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"{amount} withdrawn. New balance: {self.balance}"

    def get_balance(self):
        return f"{self.name}'s balance: {self.balance}"

