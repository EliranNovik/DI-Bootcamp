class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
#Create another cat breed named Siamese which inherits from the Cat class.

class Siamese(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)

bengal_cat = Bengal('Leo', 2)
chartreux_cat = Chartreux('Max', 3)
siamese_cat = Siamese('Luna', 1)

#Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

#Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.

sara_pets = Pets(all_cats)

#Take all the cats for a walk, use the walk method.

sara_pets.walk()






#Exercise 2 : Dogs
#Instructions

#Create a class called Dog with the following attributes name, age, weight.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

#Implement the following methods in the Dog class:
#bark: returns a string which states: “<dog_name> is barking”.
#run_speed: returns the dogs running speed (weight/age*10).
#fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        
        self_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        
        if self_strength > other_strength:
            return f'{self.name} wins the fight!'
        elif self_strength < other_strength:
            return f'{other_dog.name} wins the fight!'
        else:
            return "It's a tie!"

    def __repr__(self):
        return f'Dog(name={self.name}, age={self.age}, weight={self.weight})'

#Create 3 dogs and run them through your class.

dog1 = Dog('Lola', 4, 25)
dog2 = Dog('Rico', 2, 20)
dog3 = Dog('Henry', 5, 30)

print(f'{dog1.name} run speed: {dog1.run_speed()}')  
print(f'{dog2.name} run speed: {dog2.run_speed()}') 
print(f'{dog3.name} run speed: {dog3.run_speed()}') 








