# Essay Buddy - A Smart Sentence Checker

while True:
    # Ask for user's name
    name = input("What's your name? ").capitalize()

    # Greet the user
    print(f"Hello, {name}! Welcome to Essay Buddy.\n")

    # Ask for a sentence from the user's homework
    sentence = input("Enter a sentence from your homework: ").strip()

    # Check if sentence starts with a capital letter
    if sentence[0].isupper():
        print("✅ Good start!")
    else:
        print("⚠️ Your sentence should start with a capital letter.")

    # Check if sentence ends with a full stop
    if sentence.endswith('.'):
        print("✅ Nice! You ended your sentence properly.")
    else:
        print("⚠️ Don't forget to end your sentence with a full stop.")

    # Count the usage of specific words
    lower_sentence = sentence.lower()
    for word in ["and", "but", "because"]:
        count = lower_sentence.count(word)
        print(f"You used '{word}' {count} time(s).")

    # Count how many words in the sentence
    word_count = len(sentence.split())
    print(f"Your sentence has {word_count} word(s).")

    # Check for only letters and spaces
    clean_check = sentence.replace(" ", "").isalpha()
    if clean_check:
        print("✅ Your sentence is clean. No strange characters.")
    else:
        print("⚠️ Your sentence has some special characters. Clean it up!")

    # Show a success message nicely centered
    print("\n" + "✅ Essay Checked Successfully ✅".center(50, "⭐") + "\n")

    # Ask if user wants to try again
    retry = input("Do you want to check another sentence? (yes/no): ").strip().lower()
    if retry != "yes":
        print("Thanks for using Essay Buddy. Goodbye!")
        break
