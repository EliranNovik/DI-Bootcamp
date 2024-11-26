#Exercise 1 : What are you learning ?

#Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
#Call the function, and make sure the message displays correctly.


def display():
   print('We are learning to create functions in python.')

display() 


#Exercise 2: What’s your favorite book ?
#Instructions
#Write a function called favorite_book() that accepts one parameter called title.
#The function should print a message, such as "One of my favorite books is <title>".
#For example: “One of my favorite books is Alice in Wonderland”
#Call the function, make sure to include a book title as an argument when calling the function.


def favorite_book(title):
   print('One of my favorite books is' + title)

favorite_book('Harry Potter')


#Exercise 3 : Some Geography
#Instructions
#Write a function called describe_city() that accepts the name of a city and its country as parameters.
#The function should print a simple sentence, such as "<city> is in <country>".
#For example “Reykjavik is in Iceland”
#Give the country parameter a default value.
#Call your function.

def decribe_city(city_name, country):
    print(city_name, "is in", country)

decribe_city("Basel", "Switzerland")   


#Exercise 4 : Random
#Instructions
#Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
#Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.


import random

def compare_numbers(user_number):
    if not (1 <= user_number <= 100):
        print("Please enter a number between 1 and 100.")
        return

    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100

    if user_number == random_number:
        print(f"Success! Both numbers are {user_number}.")
    else:
        print(f"Fail! Your number was {user_number}, but the random number was {random_number}.")




#Exercise 5 : Let’s create some personalized shirts !
#Instructions
#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
#Call the function make_shirt().

#Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
#Call the function, in order to make a large shirt with the default message
#Make medium shirt with the default message
#Make a shirt of any size with a different message.

#Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size="Large", text="I love Python"):
    """Summarize the shirt size and text."""
    print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt()

make_shirt(size="Medium")

make_shirt(size="Small", text="Code is life!")

make_shirt(text="Stay curious!", size="Extra Large")



#Exercise 6 : Magicians …
#Instructions
#Using this list of magician’s names

#magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

#Create a function called show_magicians(), which prints the name of each magician in the list.
#Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
#Call the function make_great().
#Call the function show_magicians() to see that the list has actually been modified.



magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} the Great"

make_great(magician_names)
show_magicians(magician_names)



#Exercise 7 : Temperature Advice
#Instructions
#Create a function called get_random_temp().
#This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#Test your function to make sure it generates expected results.



import random

def get_random_temp(season):
    if season == 'winter':
        return round(random.uniform(-10, 16), 1) 
    elif season == 'spring':
        return round(random.uniform(0, 23), 1)
    elif season == 'summer':
        return round(random.uniform(16, 40), 1)
    elif season == 'autumn' or season == 'fall':
        return round(random.uniform(5, 24), 1)
    else:
        raise ValueError("Invalid season provided.")

def main():
    month = int(input("Enter the number of the month (1 for January, 12 for December): "))
    if month in [12, 1, 2]:
        season = 'winter'
    elif month in [3, 4, 5]:
        season = 'spring'
    elif month in [6, 7, 8]:
        season = 'summer'
    elif month in [9, 10, 11]:
        season = 'autumn'
    else:
        print("Invalid month. Defaulting to 'summer'.")
        season = 'summer'

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("The weather is pleasant. Enjoy your day!")
    elif 23 <= temp < 32:
        print("It's warm outside. Stay hydrated!")
    elif temp >= 32:
        print("It's really hot! Don't forget sunscreen and water.")

main()







#Exercise 8 : Star Wars Quiz
#Instructions
#This project allows users to take a quiz to test their Star Wars knowledge.
#The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.


data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def conduct_quiz(data):
    correct_count = 0
    wrong_count = 0
    wrong_answers = []

    print("Welcome to the Star Wars Quiz!")
    print("Answer the questions below:\n")

    for item in data:
        user_answer = input(f"{item['question']} ").strip()
        if user_answer.lower() == item["answer"].lower():
            correct_count += 1
        else:
            wrong_count += 1
            wrong_answers.append({
                "question": item["question"],
                "user_answer": user_answer,
                "correct_answer": item["answer"]
            })

    return correct_count, wrong_count, wrong_answers

def display_results(correct_count, wrong_count, wrong_answers):
    print("\nQuiz Results:")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {wrong_count}")

    if wrong_answers:
        print("\nYou answered the following questions incorrectly:")
        for item in wrong_answers:
            print(f"Question: {item['question']}")
            print(f"Your answer: {item['user_answer']}")
            print(f"Correct answer: {item['correct_answer']}\n")

    if wrong_count > 3:
        print("You had more than 3 incorrect answers. Would you like to try again?")
        retry = input("Type 'yes' to play again or 'no' to exit: ").strip().lower()
        if retry == "yes":
            start_quiz()
        else:
            print("Thanks for playing! May the Force be with you!")
    else:
        print("Great job! Thanks for playing the Star Wars Quiz!")

def start_quiz():
    correct_count, wrong_count, wrong_answers = conduct_quiz(data)
    display_results(correct_count, wrong_count, wrong_answers)

start_quiz()
