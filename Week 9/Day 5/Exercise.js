//Exercise 1 : Location
//Instructions
//1. Analyze the code below. What will be the output?

// I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)
const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const {name, location: {country, city, coordinates: [lat, lng]}} = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);


//Exercise 2: Display Student Info
//Instructions

displayStudentInfo({first: 'Elie', last:'Schoppik'});

function displayStudentInfo(objUser){
    //destructuring
    console.log('Your full name is' + '', objUser.first + '',objUser.last)
}

//Using the code above, destructure the parameter inside the function and return a string as the example seen below:
//output : 'Your full name is Elie Schoppik'



//Exercise 3: User & id
//Instructions
//Using this object:

const users = { user1: 18273, user2: 92833, user3: 90315 }

//1. Using methods taught in class, turn the users object into an array:
//Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
//FYI : The number is their ID number.



const entries = Object.entries(users);
console.log(entries);



//2. Modify the outcome of part 1, by multipling the user’s ID by 2.
//Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]


const multiplied = entries.map(([key, value]) => [key, value * 2]);
console.log(multiplied);


//Exercise 4 : Person class
//Instructions
//Analyze the code below. What will be the output?

class Person {
  constructor(name) {
    this.name = name;
  }
}

const member = new Person('John');
console.log(typeof member);

//Object



//Exercise 5 : Dog class
//Instructions
//Using the Dog class below:

class Dog {
  constructor(name) {
    this.name = name;
  }
};
//Analyze the options below. Which constructor will successfully extend the Dog class?
  // 1
//class Labrador extends Dog {
 // constructor(name, size) {
 //   this.size = size;
 // }
//};


  // 2     // THIS ONE EXTENDS THE DOG CLASS SUCCESSFULLY
class Labrador extends Dog {
  constructor(name, size) {
    super(name);
    this.size = size;
  }
};


  // 3
//class Labrador extends Dog {
  //constructor(size) {
   // super(name);
  //  this.size = size;
 // }
//};


  // 4
//class Labrador extends Dog {
 // constructor(name, size) {
 //   this.name = name;
 //   this.size = size;
 // }
//};




//Exercise 6 : Challenges
//1. Evaluate these (ie True or False)

//[2] === [2] 
//{} === {}

function evaluateComparisons() {
    const arrayComparison = [2] === [2];
    const objectComparison = {} === {};
  
    console.log("[2] === [2] =>", arrayComparison);   // false
    console.log("{} === {} =>", objectComparison);    // false
  
    return {
      arrayComparison,
      objectComparison
    };
  }
  
  const results = evaluateComparisons();
  
  


//2. What is, for each object below, the value of the property number and why?

const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number) //4
console.log(object3.number) //4
console.log(object4.number) //5

//object2 = object1; and object3 = object2; means object2 and object3 reference the same object in memory as object1.
//When you do object1.number = 4;, you effectively change the number property on that single shared object. Hence, object2.number and object3.number also become 4 (they all point to the same place in memory).
//object4 is a different object (although it looks similar, it’s a separate literal). Therefore, its number property remains 5.




//1. Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin etc …


class Animal {
    constructor(name, type, color) {
      this.name = name;
      this.type = type;
      this.color = color;
    }
  }



//2. Create a class Mammal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes.


class Mammal extends Animal {
    sound(animalSound) {
      // Return a string that includes the animal's details + the sound
      return `${animalSound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`;
    }
  }
  


//3. Create a farmerCow object that is an instance of the class Mammal. The object accepts a name, a type and a color and calls the sound method that “moos” her information.
//For example: Moooo I'm a cow, named Lily and I'm brown and white

const farmerCow = new Mammal("Lily", "cow", "brown and white");
console.log(farmerCow.sound("Moooo"));