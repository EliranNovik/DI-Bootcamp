//Exercise 1 : Scope
//Instructions
//1. Analyse the code below, and predict what will be the value of a in all the following functions.
//2. Write your prediction as comments in a js file. Explain your predictions.


// #1
function funcOne() {
    let a = 5; // 'a' is declared and initialized with 5
    if (a > 1) { // condition is true
        a = 3; // 'a' is reassigned to 3
    }
    alert(`inside the funcOne function ${a}`); // Alerts 3
}

// #1.1 - run in the console:
funcOne(); // Prediction: Alerts "inside the funcOne function 3"

// #1.2 What will happen if the variable is declared with const instead of let ?
// If 'a' is declared with const, reassigning 'a' to 3 will throw a TypeError because const variables cannot be reassigned.

// #2
let a = 0; // 'a' is declared globally and initialized with 0
function funcTwo() {
    a = 5; // Updates the global variable 'a' to 5
}

function funcThree() {
    alert(`inside the funcThree function ${a}`); // Alerts the current value of the global 'a'
}

// #2.1 - run in the console:
funcThree(); // Prediction: Alerts "inside the funcThree function 0" (before funcTwo is called)
funcTwo();
funcThree(); // Prediction: Alerts "inside the funcThree function 5" (after funcTwo is called)

// #2.2 What will happen if the variable is declared with const instead of let ?
// If 'a' is declared with const, funcTwo will throw a TypeError because you cannot reassign a value to a const variable.

// #3
function funcFour() {
    window.a = "hello"; // Sets a global variable 'a' on the window object
}

function funcFive() {
    alert(`inside the funcFive function ${a}`); // Alerts the value of window.a if defined, otherwise the global 'a'
}

// #3.1 - run in the console:
funcFour();
funcFive(); // Prediction: Alerts "inside the funcFive function hello"

// #4
let a = 1; // Global 'a' is initialized with 1
function funcSix() {
    let a = "test"; // A new local 'a' is declared and initialized with "test"
    alert(`inside the funcSix function ${a}`); // Alerts the local 'a' value ("test")
}

// #4.1 - run in the console:
funcSix(); // Prediction: Alerts "inside the funcSix function test"

// #4.2 What will happen if the variable is declared with const instead of let ?
// If 'a' is declared with const, the behavior is the same since it is a new local variable scoped to funcSix. 

// #5
let a = 2; // Global 'a' initialized with 2
if (true) {
    let a = 5; // A new block-scoped 'a' is declared and initialized with 5
    alert(`in the if block ${a}`); // Alerts the block-scoped 'a' value (5)
}
alert(`outside of the if block ${a}`); // Alerts the global 'a' value (2)

// #5.1 - run the code in the console
// Prediction: 
// Alerts "in the if block 5"
// Alerts "outside of the if block 2"

// #5.2 What will happen if the variable is declared with const instead of let ?
// The behavior remains the same because const also respects block scope. The only difference is that the block-scoped variable cannot be reassigned within the block.





//Exercise 2 : Ternary operator
//Instructions
//Using the code below:

function winBattle(){
    return true;
}
//1. Transform the winBattle() function to an arrow function.


const winBattle = () => true;


//2. Create a variable called experiencePoints.


let experiencePoints;


//3. Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.

let winBattle = true;
experiencePoints = winBattle ? 10: 1;


//4. Console.log the experiencePoints variable.

console.log(experiencePoints)




//Exercise 3 : Is it a string ?

//Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
//Check out the example below to see the expected output
//Example:

//console.log(isString('hello')); 
//true
//console.log(isString([1, 2, 4, 0]));
//false

const isString = (value) => typeof value === 'string';

console.log(isString('hello')); 
console.log(isString([1, 2, 4, 0]));




//Exercise 4 : Find the sum


//1. Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.


const sumtwo = (a,b) => a + b;




//Exercise 5 : Kg and grams
//Instructions
//Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

//1. First, use function declaration and invoke it.

function convertKG(Kg) {

    return Kg * 1000;
};

console.log(convertKG);

//2. Then, use function expression and invoke it.

const convertKg = function (kg) {
    return kg * 1000;
};



//3. Write in a one line comment, the difference between function declaration and function expression.
// Function declarations are hoisted and can be called before they are defined, while function expressions are not hoisted and can only be used after they are defined.


//4. Finally, use a one line arrow function and invoke it.

const convertKg = (kg) => kg * 1000;
console.log(convertKG);


//Exercise 7 : Welcome

//1. Create a Navbar in your HTML file.
//2. In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
//3. The function should add a div in the nabvar, displaying the name of the user and his profile picture.



//Exercise 8 : Juice Bar
//Instructions
//You will use nested functions, to open a new juice bar.

//Part I:
//1. The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.

//2. The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

//3. Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.

function makeJuice(size) {
    // Inner function to add ingredients
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        // Log the sentence to the console
        console.log(`The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, and ${ingredient3}.`);
    }

    // Invoke the inner function with sample ingredients
    addIngredients("mango", "banana", "kiwi");
}

// Invoke the outer function in the global scope
makeJuice("large");




//Part II:
//1. In the makeJuice function, create an empty array named ingredients.

//2. The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.

//3. Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

//4. The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.


function makeJuice(size) {
    // Create an empty array to store ingredients
    const ingredients = [];

    // Inner function to add ingredients
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }

    // Inner function to display the juice order
    function displayJuice() {
        const ingredientList = ingredients.join(", ");
        console.log(`The client wants a ${size} juice, containing ${ingredientList}.`);
    }

    // Invoke addIngredients twice to get 6 ingredients
    addIngredients("apple", "banana", "strawberry");
    addIngredients("mango", "pineapple", "orange");

    // Invoke displayJuice to display the final order
    displayJuice();
}

// Invoke makeJuice in the global scope
makeJuice("large");

