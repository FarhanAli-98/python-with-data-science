# Initial data
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}

# Function to create a new user
def create_user(user_id, name, email):
    if user_id in users:
        print(f"User with ID {user_id} already exists.")
    else:
        users[user_id] = {"name": name, "email": email}
        print(f"User {name} created successfully.")

# Function to read user information
def read_user(user_id):
    user = users.get(user_id)
    if user:
        print(f"User ID: {user_id}, Name: {user['name']}, Email: {user['email']}")
    else:
        print(f"User with ID {user_id} not found.")

# Function to update an existing user
def update_user(user_id, name=None, email=None):
    user = users.get(user_id)
    if user:
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        print(f"User ID {user_id} updated successfully.")
    else:
        print(f"User with ID {user_id} not found.")

# Function to delete a user
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        print(f"User ID {user_id} deleted successfully.")
    else:
        print(f"User with ID {user_id} not found.")

# Function to list all users
def list_users():
    if users:
        print("List of users:")
        for user_id, user_info in users.items():
            print(f"ID: {user_id}, Name: {user_info['name']}, Email: {user_info['email']}")
    else:
        print("No users found.")

# Demonstrating CRUD operations
print("Initial Users:")
list_users()

print("\nCreating new users:")
create_user(3, "Charlie", "charlie@example.com")
create_user(4, "David", "david@example.com")
list_users()

print("\nReading user information:")
read_user(3)
read_user(5)

print("\nUpdating user information:")
update_user(2, name="Bobby", email="bobby@example.com")
update_user(3, email="charlie_new@example.com")
list_users()

print("\nDeleting users:")
delete_user(1)
delete_user(5)
list_users()
