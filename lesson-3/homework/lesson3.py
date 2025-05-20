# Create a list containing five different fruits and print the third fruit.
List = ["apple", "grape", "banana", "avacado", "cherry"]
print(List[2])

# Create two lists of numbers and concatenate them into a single list.
List1 = [1,2,3,4,7,10]
List2 = [2,3,4,11,9,10]
print(List1 + List2)

# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
List = [1,2,3,8,10,13]
Listnew = List[0], List[2], List[-1]
print(Listnew)

# Create a list of your five favorite movies and convert it into a tuple.

favorite_movies = ["Catch me if you can", "The Great Gatsby", "The Wall of the street"
"The Inception", "Titanic"]
tuple = tuple(favorite_movies)
print(tuple)

# Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["New York", "Tashkent", "Paris", "Moscow", "LA"]
if "Paris" in cities:
    print("Paris is in the cities")
else:
    print("Paris is not in the cities")
    
# Create a list of numbers and duplicate it without using loops.
numbers = [1,2,4,6,7,8,10,13]
numbers1 = numbers
print (numbers1 + numbers)

# Given a list of numbers, swap the first and last elements.
numbers = [1,2,3,5,8,11]
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[3:7])

# Create a list of colors and count how many times "blue" appears in the list.
blue = "blue"
colours = ['blue', 'orange', 'blue', 'red', 'green', 'yellow']
print(colours.count(blue))

##Given a tuple of animals, find the index of "lion".
lion = "lion"
animals = ('wolfe', 'dog', 'elephant', 'lion', 'crocodile')
print(animals.index(lion))

# Create two tuples of numbers and merge them into a single tuple.
numbers = (1,2,3,4)
numbers1 = (1,3,4,6,7)
merged = numbers + numbers1
print(merged)

# Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3)

print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

# Create a tuple of five numbers and convert it into a list.
numbers_tuple = (5, 10, 15, 20, 25)
numbers_list = list(numbers_tuple)

print(numbers_list)

# Given a tuple of numbers, find and print the maximum and minimum values.

numbers = (1,2,3,5,8,9,13)
print(max(numbers))
print(min(numbers))

# Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "cherry", "date", "fig")
reversed_words = words[::-1]

print(reversed_words)
