//import the array of person objects from the data.js module.

import people from "./Data.js";

//Write a function that calculates and prints the average age of all the persons in the array.

function averageAge(people) {
    const totalAge = people.reduce((acc, person) => acc + person.age, 0);
    console.log(totalAge / people.length);
}  

averageAge(people);

//Use the imported array and the average age function

//Expected output: 28


