// Exercise 1 : Colors
// Instructions
// Using this array :

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// 1. Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…

colors.forEach((color, index) => {
    console.log(`${index + 1}# choice is ${color}`);
    } 
);

// 2. Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
// Hint : Use the array methods taught in class. Look at the lesson Array Methods.

const isViolet = colors.some(color => color === "Violet");
console.log(isViolet ? "Yeah" : "No...");

// Exercise 2 : Colors #2
// Instructions
// Using these arrays :

const colorss = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

// Write a JavaScript program that displays the colors in the following order:
// “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” etc…
// Hint : Use the array methods taught in class and ternary operator.

colorss.forEach((color, index) => {
    console.log(`${index + 1}${ordinal[index + 1] ? ordinal[index + 1] : ordinal[0]} choice is ${color}`);
    }
);



//Exercise 3 : Analyzing
//Instructions

//------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);

//------2------
const country = "USA";
console.log([...country]);

//Analyze these pieces of code before executing them. What will be the outputs ?

// 1 - The result will be ['bread', 'carrot', 'potato', 'chicken', 'apple', 'orange']
// 2 - The result will be ['U', 'S', 'A']


//Exercise 4 : Employees
//Instructions

//Using this array:

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

//1. Using the map() method, push into a new array the firstname of the user and a welcome message. You should get an array that looks like this :
//const welcomeStudents = ["Hello Bradley", "Hello Chloe", "Hello Jonathan", "Hello Michael", "Hello Robert", "Hello Wes", "Hello Zach"]


const welcomeStudents = users.map(user => `Hello ${user.firstName}`);
console.log(welcomeStudents);

//2. Using the filter() method, create a new array, containing only the Full Stack Residents.

let fullstackResidents = users.filter(user => user.role === "Full Stack Resident");

console.log(fullstackResidents);


//Exercise 5 : Star Wars
//Instructions
//Using this array:

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

//1. Use the reduce() method to combine all of these into a single string. 

const reducer = (accumulator, currentValue) => accumulator + " " + currentValue;

let onePhrase = epic.reduce(reducer);

console.log(onePhrase);


//Exercise 6 : Employees #2
//Instructions
//Using this object:

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];


//1. Using the filter() method, create a new array, containing the students that passed the course.

let passedStudents = students.filter(students => students.isPassed === true);

console.log(passedStudents);