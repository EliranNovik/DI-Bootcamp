(function (userName) {
    // Create a div for user info
    const userDiv = document.createElement("div");

    // Add the user's profile picture
    const userImage = document.createElement("img");
    userImage.src = "https://via.placeholder.com/40"; // Placeholder profile picture
    userImage.alt = "User Profile Picture";

    // Add the user's name
    const userNameSpan = document.createElement("span");
    userNameSpan.textContent = userName;

    // Append elements to the userDiv
    userDiv.appendChild(userImage);
    userDiv.appendChild(userNameSpan);

    // Add the userDiv to the navbar
    document.getElementById("user-info-container").appendChild(userDiv);
})("John"); // Replace "John Doe" with the signed-in user's name
