import React from "react";
import "./Exercise.css"; // Import the CSS file

const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial",
};

function Exercise() {
  return (
    <div>
      {/* Styled h1 with inline styles */}
      <h1 style={style_header}>This is a header</h1>
      
      {/* Paragraph with CSS class */}
      <p className="para">This is a paragraph</p>
      
      {/* Other HTML elements */}
      <a href="https://www.google.com" target="_blank" rel="noreferrer">Google Link</a>
      <form>
        <input type="text" placeholder="Your name" />
        <button type="submit">Submit</button>
      </form>
      <img src="https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F096baapsqqt9fks0us99.png" alt="React-Logo" />
      
      {/* List of items */}
      <ul>
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
      </ul>
    </div>
  );
}

// ✅ Default Export
export default Exercise;
