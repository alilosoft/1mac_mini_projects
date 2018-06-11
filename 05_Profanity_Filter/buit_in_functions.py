import random
# Example of using the built-in function sorted(iterable)
# Return a new sorted list from the items in iterable.
numbers = []
for i in range(10):
    numbers.append(random.randint(0, 100))

print numbers
print sorted(numbers)
# This program print out a sorted list from randomly generated list