print("Welcome to the Secure Login System\n")

# --- Sign Up ---
print("--- Sign Up ---")
username = input("Enter your username: ")

# Password strength validation
while True:
    password = input("Create a password: ")
    confirm_password = input("Re-enter your password: ")

    if password != confirm_password:
        print(" Passwords do not match. Please try again.\n")
        continue

    if len(password) < 6:
        print(" Password too short! Must be at least 6 characters.\n")
        continue

    if not any(char.isdigit() for char in password):
        print(" Password must include numbers!\n")
        continue

    if ' ' in password:
        print(" Password should not contain spaces!\n")
        continue

    # If all checks pass
    break

print("\n Account created successfully!\n")

# --- Log In ---
print("--- Log In ---")
login_username = input("Enter username: ")
login_password = input("Enter password: ")

if login_username == username and login_password == password:
    print(f"\n Login successful! Welcome back, {username}!")
else:
    print("\n Incorrect username or password. Please try again.")