#Exercise 1: Currencies
#Instructions


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s" if self.amount > 1 else f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        return Currency(self.currency, self.amount + other)

    def __iadd__(self, other):
        self = self + other  # Reuse the __add__ method
        return self

    def __repr__(self):
        return str(self)

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)

print(c1)      
print(int(c1))         
print(repr(c1))       

print(c1 + 5)          
print(c1 + c2)         

c1 += 5
print(c1)            

try:
    print(c1 + c3)     
except TypeError as e:
    print(e)        





#Exercise 2: Import
#Instructions
#In a file named func.py create a function that sum 2 numbers, and prints the result
#In a file named exercise_one.py import the function and call it to print the result
#Hint: You can use the the following syntaxes:



#Exercise 3: String module
#Instructions
#Generate random String of length 5
#Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
#Hint: use the string modu5) 

import string

import random

def generate_random_string(length=5):

    characters = string.ascii_letters
    random_string = random.choices(characters, k=length)

    return random_string

print(generate_random_string())


#Exercise 4 : Current Date
#Instructions
#Create a function that displays the current date.
#Hint : Use the datetime module.

from datetime import date

def display_current_date():
    current_date = date.today()
    print(current_date)

display_current_date()



#Exercise 5 : Amount of time left until January 1st
#Instructions
#Create a function that displays the amount of time left from now until January 1st.
#(Example: the 1st of January is in 10 days and 10:34:01hours).

from datetime import datetime

def time_until_new_year():

    now = datetime.now()

    next_year = now.year + 1 if now.month == 12 and now.day > 31 else now.year
    new_year = datetime(next_year, 1, 1)

    time_remaining = new_year - now

    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Time left until New Year: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

time_until_new_year()



#Exercise 6 : Birthday and minutes
#Instructions
#Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.



from datetime import datetime

def minutes_lived(birthday: str):
    """
    Calculate how many minutes a user has lived based on their birthday.
    
    Args:
        birthday (str): The user's birthday in the format 'YYYY-MM-DD'.
    """
    try:
        # Convert the birthday string to a datetime object
        birth_date = datetime.strptime(birthday, '%Y-%m-%d')
        
        now = datetime.now()
        
        time_lived = now - birth_date
        
        minutes = time_lived.total_seconds() // 60
        
        print(f"You have lived approximately {int(minutes):,} minutes.")
    except ValueError:
        print("Please provide the birthday in the format 'YYYY-MM-DD'.")

minutes_lived('1995-07-02')


#Exercise 7 : Faker Module
#Instructions
#Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
#Create an empty list called users. Tip: It should be a list of dictionaries.
#Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.



from faker import Faker

fake = Faker()

users = []

def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

for _ in range(5):
    add_user()

for user in users:
    print(user)

