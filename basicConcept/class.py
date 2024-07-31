class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
alice = Person("Alice", 30)
bob = Person("Bob", 25)

# Accessing object methods
alice.display()
bob.display()
