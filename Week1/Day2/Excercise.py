#1.
#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = set()

my_fav_numbers.add(10)
my_fav_numbers.add(20)

print(my_fav_numbers)

my_fav_numbers.add(40)
my_fav_numbers.add(50)

print(my_fav_numbers)

my_fav_numbers.remove(50)
print(my_fav_numbers)

friend_fav_numbers = set()

friend_fav_numbers.add(3)
friend_fav_numbers.add(4)
friend_fav_numbers.add(5)
friend_fav_numbers.add(6)

print(friend_fav_numbers)

our_fav_numbers = (my_fav_numbers, friend_fav_numbers)
print(our_fav_numbers)

#2. Tuple
#Given a tuple which value is integers, is it possible to add more integers to the tuple?
#anwer: No, it's not possible to add more integers to a tuple. That's how Python is build.

#3.
#Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#Remove “Banana” from the list.
#Remove “Blueberries” from the list.
#Add “Kiwi” to the end of the list.
#Add “Apples” to the beginning of the list.
#Count how many apples are in the basket.
#Empty the basket.
#Print(basket)

my_basket = ["Banana", "Apples", "Oranges", "Blueberries"]

my_basket.remove('Banana')

my_basket.remove('Blueberries')

additional_item = ['Kiwi']

my_basket.insert(0,"Apples")

#2 apples

my_basket.clear()

print(my_basket)

#4
#Recap – What is a float? What is the difference between an integer and a float?
#Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#Can you think of another way to generate a sequence of floats?

#float = number with decimal point (2.5) ; the differnce between a float and an integer is that an integer shown exact values without a decimal point

sequence = [2.5 + 0.5 * i for i in range(4)]

sequence = []
num = 2.5
while num <= 5:
    sequence.append(num)
    num += 0.5

 #5
 #  Use a for loop to print all numbers from 1 to 20, inclusive.
#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.  

for it in range(1,21):
    print(it)

 for it in range(1, 21):
    if it % 2 == 0: 
        print(it)   

#6.
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "Eliran"

while True:
    user_name = input("What is your name? ")
    if user_name == my_name:
        print("Hello, " + my_name + "!")
        break 

 #7
 # Ask the user to input their favorite fruit(s) (one or several fruits).
#Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
#Store the favorite fruit(s) in a list (convert the string of words into a list of words).
#Now that we have a list of fruits, ask the user to input a name of any fruit.
#If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.  

fruits = input("Please enter your favorite fruit(s), don't forget to separate by a space!: ")

fruit_list = fruits.split()

chosen_fruit = input("Enter a fruit: ")

if chosen_fruit in fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. Enjoy.")


# 8
#Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

total_price = 10
toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    
    if topping == 'quit':
        break
    
    toppings.append(topping)
    total_price += 2.5
    print(f"Adding {topping} to your pizza.")

print("\nYour pizza toppings are:", ", ".join(toppings))
print(f"Total price: ${total_price}")

#9
#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

total_cost = 0
num_people = int(input("How many people are in your family? "))

for it in range(num_people):
    age = int(input(f"Enter the age of person {it + 1}: "))
    
    if age < 3:
        price = 0 
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    total_cost += price

print(f"The total cost of all tickets is: ${total_cost}")

#10 Using the list below :

#sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

#The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
#We need to prepare the orders of the clients:
#Create an empty list called finished_sandwiches.
#One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
#After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
#I made your tuna sandwich
#I made your avocado sandwich
#I made your egg sandwich
#I made your chicken sandwich


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")

#DONE


