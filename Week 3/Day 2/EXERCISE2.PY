#Exercise 3 : Dogs Domesticated
#Instructions
#Create a new python file and import your Dog class from the previous exercise.

from EXERCISE_DOG import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def bark(self):
        return f'{self.name} says woof!'

    def train(self):
        print(self.bark())
        self.trained = True
        print(f'{self.name} is now trained!')

    def play(self, *other_dogs):
        dog_names = [self.name]
        for dog in other_dogs:
            dog_names.append(dog.name)
        
        play_message = ""
        for i, dog_name in enumerate(dog_names):
            if i == len(dog_names) - 1 and len(dog_names) > 1:
                play_message += f"and {dog_name} "
            elif i == len(dog_names) - 1:
                play_message += f"{dog_name} "
            else:
                play_message += f"{dog_name}, "

        print(f'{play_message}all play together.')

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f'{self.name} does a barrel roll.',
                f'{self.name} stands on his back legs.',
                f'{self.name} shakes your hand.',
                f'{self.name} plays dead.'
            ]
            trick_index = self.age % len(tricks)
            print(tricks[trick_index])
        else:
            print(f'{self.name} is not trained yet!')

    def get_age_in_human_years(self):
        return self.age * 7

    def __repr__(self):
        return f'PetDog(name={self.name}, age={self.age}, weight={self.weight}, trained={self.trained})'


if __name__ == "__main__":
    dog1 = PetDog("Lola", 3, 25)
    dog2 = PetDog("Rico", 2, 20)
    dog3 = PetDog("Henry", 4, 30)

    dog1.train()

    dog1.do_a_trick()

    dog1.play(dog2, dog3)

    dog2.do_a_trick()

#In the new python file, create a class named PetDog that inherits from Dog.
#Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
#Add the following methods:

#train: prints the output of bark and switches the trained boolean to True

#play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

#do_a_trick: If the dog is trained the method should print one of the following sentences at random:
###“dog_name does a barrel roll”.
#“dog_name stands on his back legs”.
#“dog_name shakes your hand”.
#“dog_name plays dead”.





#Exercise 4 : Family
#Instructions
#Create a class called Family and implement the following attributes:

#members: list of dictionaries
#last_name : (string)

#Implement the following methods:

#born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
#is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
#family_presentation: a method that prints the family’s last name and all the members’ details.

#Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

    #[
       # {'name':'Michael','age':35,'gender':'Male','is_child':False},
     #   {'name':'Sarah','age':32,'gender':'Female','is_child':False}
   # ]


class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **new_member):
        self.members.append(new_member)
        print(f"Congratulations! {new_member['name']} has been born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Meet the {self.last_name} family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {'Yes' if member['is_child'] else 'No'}")

family_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family("Johnson", family_members)

my_family.family_presentation()  

my_family.born(name="Anna", age=0, gender="Female", is_child=True)

print(my_family.is_18("Michael"))
print(my_family.is_18("Sarah"))
print(my_family.is_18("Anna"))


#Exercise 5 : TheIncredibles Family
#Instructions
#Create a class called TheIncredibles. This class should inherit from the Family class:
#This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)


#Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


#Add a method called incredible_presentation which :

#Print a sentence like “*Here is our powerful family **”
#Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)


#Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

   #[
       # {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        #{'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
   # ]


#Call the incredible_presentation method.


#Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


#Call the incredible_presentation method again.


class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **new_member):
        self.members.append(new_member)
        print(f"Congratulations! {new_member['name']} has been born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Meet the {self.last_name} family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {'Yes' if member['is_child'] else 'No'}")


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} uses their power to {member['power']}!")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power.")
    
    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()

incredible_family_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredible_family = TheIncredibles("Incredibles", incredible_family_members)

incredible_family.incredible_presentation()

incredible_family.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")

incredible_family.incredible_presentation()

try:
    incredible_family.use_power("Michael")
    incredible_family.use_power("Jack")
except Exception as e:
    print(e)





