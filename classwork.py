def word_wizard():
    print("Welcome to WordWizard!")

    #Get user input
    sentence = input("Enter a sentence you wrote for a school assignment:\n")
    old_word = input("Enter a word you want to replace:\n")
    new_word = input("Enter the new word to replace it with:\n")

    # Clean up sentence
    cleaned_sentence = ' '.join(sentence.strip().split())
    cleaned_sentence = cleaned_sentence.capitalize()

    #Replace the word
    updated_sentence = cleaned_sentence.replace(old_word, new_word)

    #Display different formats
    print("\n--- Cleaned and Formatted Versions ---")
    print(f"Original (Cleaned and Replaced): {updated_sentence}")
    print(f"Title Case: {updated_sentence.title()}")
    print(f"Upper Case: {updated_sentence.upper()}")
    print(f"Lower Case: {updated_sentence.lower()}")

    #Show only the first 5 words
    first_five_words = ' '.join(updated_sentence.split()[:5])
    print(f"\nFirst 5 Words: {first_five_words}")

word_wizard()