#Exercise 1 : Convert lists into dictionaries

#Convert the two following lists, into dictionaries.
#Hint: Use the zip method
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
#Expected output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

answer = dict(zip(keys, values))
print(answer)


#Exercise 2 : Cinemax #2
#Instructions
#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

#Given the following object:

#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

#How much does each family member have to pay ?

#Print out the family’s total cost for the movies.
#Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total_cost = 0
for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} has to pay ${cost}.")
    total_cost += cost

print(f"Total cost for the family is ${total_cost}.")



#Exercise 3: Zara
#Instructions
#Here is some information about a brand.
#name: Zara 
#creation_date: 1975 
#creator_name: Amancio Ortega Gaona
#type_of_clothes: men, women, children, home 
#international_competitors: Gap, H&M, Benetton 
#number_stores: 7000 
#major_color: 
 #   France: blue, 
 #   Spain: red, 
  #  US: pink, green


#2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
#The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
#3. Change the number of stores to 2.
#4. Print a sentence that explains who Zaras clients are.
#5. Add a key called country_creation with a value of Spain.
#6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
#7. Delete the information about the date of creation.
#8. Print the last international competitor.
#9. Print the major clothes colors in the US.
#10. Print the amount of key value pairs (ie. length of the dictionary).
#11. Print the keys of the dictionary.
#12. Create another dictionary called more_on_zara with the following details:

#creation_date: 1975 
#number_stores: 10 000


#13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
#14. Print the value of the key number_stores. What just happened ?

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand['number_stores'] = 2

print(f' Zaras clients are men, women, children')

brand['county_creation'] = 'Spain'


