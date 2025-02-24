import React from "react";
import UserFavoriteAnimals from "./UserFavoriteAnimals"; // Task 2
import Exercise from "./Exercise3"; // Task 3

// Task 1: JSX Variables
const myelement = <h1>I Love JSX!</h1>;
const sum = 5 + 5;

// Task 2: User Object
const user = {
  firstName: "Bob",
  lastName: "Dylan",
  favAnimals: ["Horse", "Turtle", "Elephant", "Monkey"],
};

function App() {
  return (
    <div>
      {/* Task 1: JSX */}
      <p>Hello World!</p>
      {myelement}
      <p>React is {sum} times better with JSX</p>

      {/* Task 2: User Data */}
      <h3>First Name: {user.firstName}</h3>
      <h3>Last Name: {user.lastName}</h3>
      <UserFavoriteAnimals favAnimals={user.favAnimals} />

      {/* Task 3: Exercise3 Component */}
      <Exercise />
    </div>
  );
}

export default App;
