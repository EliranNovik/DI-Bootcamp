from anagram_checker import AnagramChecker

def get_user_input():
    while True:
        user_input = input("Enter a single word, or type 'exit' to quit: ").strip()
        if user_input.lower() == "exit":
            return None
        if not user_input.isalpha():
            print("Error: Input must only contain alphabetic characters.")
        elif len(user_input.split()) > 1:
            print("Error: Input must be a single word.")
        else:
            return user_input

def display_results(word, anagrams):
    print(f"\nYOUR WORD: \"{word.upper()}\"")
    print("This is a valid English word.")
    if anagrams:
        print(f"Anagrams for your word: {', '.join(anagrams)}")
    else:
        print("No anagrams found for your word.")

def main():
    anagram_checker = AnagramChecker()

    while True:
        user_word = get_user_input()
        if user_word is None:
            print("Goodbye!")
            break

        if not anagram_checker.is_valid_word(user_word):
            print("Error: This is not a valid English word.")
            continue

        anagrams = anagram_checker.get_anagrams(user_word)
        display_results(user_word, anagrams)

if __name__ == "__main__":
    main()


            
