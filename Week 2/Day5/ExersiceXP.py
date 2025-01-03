#Exercise 1: Cats
#Instructions
#Using this class

#class Cat:
 #   def __init__(self, cat_name, cat_age):
 #       self.name = cat_name
 #       self.age = cat_age

#Instantiate three Cat objects using the code provided above.
#Outside of the class, create a function that finds the oldest cat and returns the cat.
#Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Lori", 10)
cat2 = Cat("Rico", 5)
cat3 = Cat("Nico", 7)


def find_oldest_cat(*cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

#Exercise 2 : Dogs
#Instructions
#Create a class called Dog.
#In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
#Create a method called bark that prints the following string “<dog_name> goes woof!”.
#Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
#Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
#Print the details of his dog (ie. name and height) and call the methods bark and jump.
#Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
#Print the details of her dog (ie. name and height) and call the methods bark and jump.
#Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = int(height)
        self.jump_height = self.height * 2

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.jump_height} cm high')

davids_dog = Dog('Rex', '50')

print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")

davids_dog.bark() 
davids_dog.jump()

sarahs_dog = Dog('Teacup', '20')

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")

sarahs_dog.bark() 
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger.")






#Exercise 3 : Who’s the song producer?


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()






#Exercise 4 : Afternoon at the Zoo


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        self.animals.sort()
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)
        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Animal groups:")
        for group, animals in sorted_animals.items():
            print(f"{group}: {animals}")

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Cat")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Baboon")

ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()

