# Age Calculator & Future Age Predictor

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
future_year = int(input("Enter a future year you'd like to check: "))

current_year = 2025
current_age = current_year - birth_year
future_age = future_year - birth_year

print("\nHi " + name + "!")
print("You are currently", current_age, "years old.")
print("In the year", future_year, "you will be", future_age, "years old.")
