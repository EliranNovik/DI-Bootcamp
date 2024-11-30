def get_words_from_file():
    try:
        with open('sowpods.txt', 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("Error: The file 'sowpods.txt' was not found.")
        return []


import random

def get_random_sentence(length):
    words = get_words_from_file() 
    if not words:
        return "Error: No words available to create a sentence."
    
    random_words = random.choices(words, k=length)
    sentence = ' '.join(random_words).lower() 
    return sentence


def main():
    print("Welcome! This program generates a random sentence based on words from the SOWPODS word list.")
    
    try:
        length = int(input("How long do you want the sentence to be? (Enter a number between 2 and 20): "))
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("\nHere is your random sentence:")
            print(sentence)
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")



import random

def get_words_from_file():
    try:
        with open('sowpods.txt', 'r') as file:
            words = file.read().splitlines() 
        return words
    except FileNotFoundError:
        print("Error: The file 'sowpods.txt' was not found.")
        return []

def get_random_sentence(length):
    words = get_words_from_file()
    if not words:
        return "Error: No words available to create a sentence."
    
    random_words = random.choices(words, k=length)
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    print("Welcome! This program generates a random sentence based on words from the SOWPODS word list.")
    
    try:
        length = int(input("How long do you want the sentence to be? (Enter a number between 2 and 20): "))
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("\nHere is your random sentence:")
            print(sentence)
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()

