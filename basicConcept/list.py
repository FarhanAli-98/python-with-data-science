# Creating a list
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

# List slicing
print(f"First three elements: {numbers[:3]}")
print(f"Elements from index 2 to 4: {numbers[2:5]}")

# Adding elements
numbers.append(6)
print(f"After appending 6: {numbers}")

# Removing elements
numbers.remove(3)
print(f"After removing 3: {numbers}")

# List length
print(f"Length of list: {len(numbers)}")

#############################################

# List of squares
squares = [x ** 2 for x in range(10)]
print(f"Squares: {squares}")

# List of even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")
