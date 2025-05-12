def welcome_screen():
    # Greet the player and get their name and age
    name = input("What is your name? ")
    age = input(f"Hi {name}, how old are you? ")
    print(f"\nWelcome to the Math Challenge Game, {name}!\n")
    return name

def level_1():
    # Level 1: Number Casting Challenge
    number = input("Enter a number between 10 and 99: ")
    
    try:
        number = int(number)  # Convert to integer
        if 10 <= number <= 99:
            result = number + 5
            print(f"Adding 5 to your number: {result}\n")
            return True
        else:
            print("Please enter a number between 10 and 99.")
            return False
    except ValueError:
        print("That's not a valid number!")
        return False

def level_2():
    # Level 2: Math Puzzle
    score = 0
    for _ in range(3):
        num1 = (1, 10)
        num2 = (1, 10)
    
        correct_answer = num1 - num2
        question = f"What is {num1} * {num2}?"
        
        # Get player answer
        try:
            player_answer = int(input(question + " → User: "))
            if player_answer == correct_answer:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. The answer was {correct_answer}\n")
        except ValueError:
            print("Invalid input, please enter a number.")
    
    return score

def level_3():
    # Level 3: Mystery Type Guesser
    # Define variables
    age = 15
    height = 163.5
    is_winner = True
    
    # Ask the user to guess data types
    guesses = {
        'age': input(f"What data type is the variable 'age' (int, float, bool)? ").strip().lower(),
        'height': input(f"What data type is the variable 'height' (int, float, bool)? ").strip().lower(),
        'is_winner': input(f"What data type is the variable 'is_winner' (int, float, bool)? ").strip().lower()
    }
    
    # Check if the guesses are correct
    score = 0
    if guesses['age'] == 'int' and type(age) == int:
        score += 1
    if guesses['height'] == 'float' and type(height) == float:
        score += 1
    if guesses['is_winner'] == 'bool' and type(is_winner) == bool:
        score += 1

    return score

def final_score_report(name, score, bonus_points):
    # Final score report
    total_score = score + bonus_points
    print(f"\nGreat job, {name}! You got {score} out of 3 math questions right and earned {bonus_points} bonus point(s) for guessing the data types correctly. Total Score: {total_score}/4.")

def main():
    # Start the game
    name = welcome_screen()
    
    # Level 1: Number Casting Challenge
    if not level_1():
        print("You failed Level 1. Game Over!")
        return
    
    # Level 2: Math Puzzle
    math_score = level_2()

    # Level 3: Mystery Type Guesser
    type_score = level_3()

    # Final Score
    final_score_report(name, math_score, type_score)

# Run the game
if __name__ == "__main__":
    main()