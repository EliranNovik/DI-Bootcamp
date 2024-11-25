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


def ac_numbers range(1-100):
    print()