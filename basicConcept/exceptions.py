try:
    # Division by zero error
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    # File not found error
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

# General exception handling
try:
    x = int("abc")
except Exception as e:
    print(f"Error: {e}")
