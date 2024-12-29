//Part I - Review about arrays

//1.Write code to remove “Greg” from the people array.

const people = ["Greg", "Mary", "Devon", "James"];
const deletedItem =people.splice(0,1);

console.log(people);

//2.Write code to replace “James” to “Jason”

people[2] = 'Jason';

console.log(people);

//3.Write code to add your name to the end of the people array.

people.push("Eliran");
console.log(people);

//4.Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

const maryIndex = people.indexOf("Mary");
console.log(maryIndex); 

//5.Write code to make a copy of the people array using the slice method.
//The copy should NOT include “Mary” or your name.
//Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
//Hint: Check out the documentation for the slice method

const people = ["Mary", "Devon", "Jason", "Eliran"];
const copy = people.slice(1, 3);
console.log(copy); 

//6.Write code that gives the index of “Foo”. Why does it return -1 ?

const people = ["Mary", "Devon", "Jason", "Eliran"];
const fooIndex = people.indexOf("Foo");
console.log(fooIndex); 

//It returns -1 because "Foo" does not exist in the people array. In JavaScript, when an element isn’t found, indexOf will return -1.

//Create a variable called last which value is the last element of the array.
//Hint: What is the relationship between the index of the last element in the array and the length of the array?

const people = ["Mary", "Devon", "Jason", "Eliran"];
const last = people[people.length - 1];

console.log(last); 



//Part II - Loops

const people = ["Mary", "Devon", "Jason", "Eliran"];

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}

//Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
//Hint: take a look at the break statement in the lesson.


const people = ["Mary", "Devon", "Jason", "Eliran"];

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
        break;
    }
}


//Exercise 2 : Your favorite colors

//Create an array called colors where the value is a list of your five favorite colors.

let colors = ['Yellow', 'Blue', 'Green', 'Black', 'Red'];

//Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .

for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i + 1} choice is ${colors[i]}`);}


//    Exercise 3 : Repeat the question

//Prompt the user for a number.
//Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

//let userNumber = prompt("Please enter a number:");

console.log("Value received:", userNumber);
console.log("Type of userNumber:", typeof userNumber);


//While the number is smaller than 10 continue asking the user for a new number.
//Tip : Which while loop is more relevant for this situation?

let userNumber = parseInt(prompt("Please enter a number:"));

while (userNumber < 10) {
  userNumber = parseInt(prompt("The number is smaller than 10. Please enter a new number:"));
}

console.log("Thank you! Your number is:", userNumber);


//Exercise 4 : Building Management

// Review about objects
//1. Copy and paste the above object to your Javascript file.

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}


//2. Console.log the number of floors in the building.

console.log(building.numberOfFloors);

//3. Console.log how many apartments are on the floors 1 and 3.

console.log(building.numberOfAptByFloor.firstFloor);
console.log(building.numberOfAptByFloor.thirdFloor);

//4. Console.log the name of the second tenant and the number of rooms he has in his apartment.

const secondTenant = building.nameOfTenants[1];  
const secondTenantRooms = building.numberOfRoomsAndRent[secondTenant.toLowerCase()][0];

console.log(`Second tenant: ${secondTenant}, Number of rooms: ${secondTenantRooms}`);

//5. Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent   = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
  console.log("Dan's rent has been updated to:", building.numberOfRoomsAndRent.dan[1]);
} else {
  console.log("Dan's rent remains:", danRent);
}


//Exercise 5 : Family
//Instructions

//1. Create an object called family with a few key value pairs.

const family = {
    father: "Baruch",
    mother: "Chana",
    son: "Joel",
    daughter: "Sarah",
  };
  

//2. Using a for in loop, console.log the keys of the object.

  
  for (let key in family) {
    console.log(key);
  }
  

//3.Using a for in loop, console.log the values of the object.


  for (let key in family) {
    console.log(family[key]); 
  }
  

//Exercise 6 : Rudolf
//Instructions

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'reindeer'
  }


//1. Given the object above and using a for loop, console.log “my name is Rudolf the reindeer”


let sentence = "";

for (let key in details) {
  sentence += key + " " + details[key] + " ";
}

console.log(sentence.trim()); 


//Exercise 7 : Secret Group
//Instructions

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const societyName = names
  .map(name => name[0])
  .sort()
  .join('');



//2. Console.log the name of their secret society. The output should be “ABJKPS”

console.log(societyName); 
