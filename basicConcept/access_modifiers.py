#Print Statement 


print("Hello, World!")


#Access Modifiers (variables)
integer = 10
floating_point = 20.5
character = 'A'
text = "Hello"
boolean = True



#if else

x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


 
    # Loops

#     # For loop
# for i in range(5):
#     print(i)

# # While loop
# i = 0
# while i < 5:
#     print(i)
#     i += 1




def greet():
    print("Hello!")

def add(a, b):
    return a + b

greet()
print("Sum:", add(3, 4))



#Arrays

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing elements
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding elements
person["email"] = "alice@example.com"
print(f"After adding email: {person}")

# Removing elements
del person["city"]
print(f"After removing city: {person}")

# Iterating over a dictionary
for key, value in person.items():
    print(f"{key}: {value}")



def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

def add(a, b):
    return a + b

result = add(10, 5)
print(f"Addition result: {result}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"Factorial of 5: {factorial(5)}")
