import random

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 14:
    print("Sorry, you must be 14 or older to play!")
    exit()
else:
    print(f"Welcome, {name}! Let's start the game!")

score = 0

# Level 1: Lucky Guess
lucky_number = random.randint(1, 5)
player_guess = int(input("Guess a number between 1 and 5: "))

if player_guess == lucky_number:
    print("🎉 You guessed correctly!")
else:
    print("😢 Incorrect, but here's another try!")
    player_guess = int(input("Guess again: "))
    if player_guess == lucky_number:
        print("🎉 You guessed correctly!")
    else:
        print("😢 Sorry, that's wrong again!")

# Level 2: Smart Math
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
multiplication_answer = int(input(f"What is {num1} * {num2}? "))
if multiplication_answer == num1 * num2:
    print("🧠 Correct!")
    score += 1
else:
    print("🧠 Incorrect!")

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
subtraction_answer = int(input(f"What is {num1} - {num2}? "))
if subtraction_answer == num1 - num2:
    print("🧠 Correct!")
    score += 1
else:
    print("🧠 Incorrect!")

# Level 3: Type Detective
x = 10
y = 12.5
z = True

guess_x = input("What is the type of x (int, float, bool)? ")
if guess_x.lower() == "int":
    print("🧠 Correct!")
    score += 1
else:
    print("🧠 Incorrect!")

guess_y = input("What is the type of y (int, float, bool)? ")
if guess_y.lower() == "float":
    print("🧠 Correct!")
    score += 1
else:
    print("🧠 Incorrect!")

guess_z = input("What is the type of z (int, float, bool)? ")
if guess_z.lower() == "bool":
    print("🧠 Correct!")
    score += 1
else:
    print("🧠 Incorrect!")

# Final Score
print(f"Great job, {name}! You scored {score}/5.")
