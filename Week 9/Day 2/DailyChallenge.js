//Instructions
//Using this object :

//let client = "John";

//const groceries = {
 //   fruits : ["pear", "apple", "banana"],
   // vegetables: ["tomatoes", "cucumber", "salad"],
  //  totalPrice : "20$",
  //  other : {
   //     paid : true,
  //      meansOfPayment : ["cash", "creditCard"]
 //   }
//}
//Hint: To do this daily challenge, take a look at today’s lesson Pass By Value & Pass By Reference

//1. Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.

//2.Create another arrow function named cloneGroceries.


//In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)}
//Change the client variable to “Betty”. Will we also see this modification in the user variable ? Why ?
//In the function, create a variable named shopping that is equal to the groceries variable.
//Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ?
//Change the value of the paid key to false. Will we also see this modification in the shopping object ? Why ?
//3. Invoke the cloneGroceries function.



let client = "John";

const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        paid: true,
        meansOfPayment: ["cash", "creditCard"]
    }
};

// Arrow function to display the fruits using forEach
const displayGroceries = () => {
    groceries.fruits.forEach((fruit) => console.log(fruit));
};

// Arrow function to clone and test pass by value/reference
const cloneGroceries = () => {
    // Create a copy of the client variable
    let user = client;

    // Change the client variable
    client = "Betty";

    // Check if the change is reflected in the user variable
    console.log(`User: ${user}`); // Will print "John"
    console.log(`Client: ${client}`); // Will print "Betty"
    // Explanation: Primitive types (like strings) are passed by value, so `user` holds a copy of the original value of `client` and is not affected by changes to `client`.

    // Create a reference to the groceries object
    let shopping = groceries;

    // Change the value of the totalPrice key
    shopping.totalPrice = "35$";
    console.log(`Groceries totalPrice: ${groceries.totalPrice}`); // Will print "35$"
    // Explanation: Objects are passed by reference, so modifying `shopping` affects `groceries` since both variables point to the same memory location.

    // Change the value of the paid key
    shopping.other.paid = false;
    console.log(`Groceries paid: ${groceries.other.paid}`); // Will print "false"
    // Explanation: The `other` object inside `groceries` is also passed by reference. Changing `paid` in `shopping` updates the same reference in `groceries`.
};

// Invoke the functions
displayGroceries(); // Logs "pear", "apple", "banana"
cloneGroceries();


