//Exercise 2 : Work with forms

//Retrieve the form and console.log it.

const formElement = document.querySelector('form');
console.log(formElement);

//Retrieve the inputs by their id and console.log them.

const inputElement1 = document.getElementById('fname');
console.log(inputElement1)

const inputElement2 = document.getElementById('lname');
console.log(inputElement2);

//Retrieve the inputs by their name attribute and console.log them.

const inputLastName = document.getElementsByName('lastname');
const inputFirstName = document.getElementsByName('firstname');
console.log(inputLastName);
console.log(inputFirstName);


//When the user submits the form (ie. submit event listener)
//use event.preventDefault(), why ?
//get the values of the input tags,
//make sure that they are not empty,
//create an li per input value,
//then append them to a the <ul class="usersAnswer"></ul>, below the form.
//The output should be :

//<ul class="usersAnswer">
//    <li>first name of the user</li>
//    <li>last name of the user</li>
//</ul>

    // 1. Select the form and the <ul> element
    const form = document.querySelector("#userForm");
    const usersAnswerList = document.querySelector(".usersAnswer");

    // 2. Add a 'submit' event listener on the form
    form.addEventListener("submit", function(event) {
      // Prevent the default form submission behavior (page refresh)
      event.preventDefault();

      // 3. Get the values from the input fields
      const firstName = document.getElementById("fname").value.trim();
      const lastName = document.getElementById("lname").value.trim();

      // 4. Validate input: Ensure both fields are not empty
      if (firstName === "" || lastName === "") {
        alert("Please fill out both the first and last names.");
        return; // Stop if either field is empty
      }

      // 5. Create an <li> for each value and append it to the <ul>
      const liFirstName = document.createElement("li");
      liFirstName.textContent = firstName;
      usersAnswerList.appendChild(liFirstName);

      const liLastName = document.createElement("li");
      liLastName.textContent = lastName;
      usersAnswerList.appendChild(liLastName);

      // 6. Reset the form after successful submission
      form.reset();
    });



//Exercise 3 : Transform the sentence
//Instructions
//Add this sentence to your HTML file then follow the steps :


//1.Declare a global variable named allBoldItems.

let allBoldItems;


function getBoldItems(){

allBoldItems = document.querySelectorAll('p strong');}

getBoldItems();
//Create a function called highlight() that changes the color of all the bold text to blue.

function highlight() {
    // This will fail if allBoldItems is still undefined
    allBoldItems.forEach(item => {
      item.style.color = "blue";
    });
  }


//Create a function called returnItemsToDefault() that changes the color of all the bold text back to black.

function returnItemsToDefault() {
    allBoldItems.forEach(function(item) {
        item.style.color = "black";
      });
    }


//Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function returnItemsToDefault() on mouseout (ie. when the mouse pointer is moved out of the paragraph).  
   
getBoldItems();

const paragraph = document.querySelector("p");
paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", returnItemsToDefault);
