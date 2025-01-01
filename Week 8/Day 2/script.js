//Exercise 1 : Change the article

//Using a DOM property, retrieve the h1 and console.log it.
const h1Element = document.querySelector('h1');
console.log(h1Element);

//Using DOM methods, remove the last paragraph in the <article> tag.

const article = document.querySelector("article");

article.removeChild(article.lastElementChild);

//Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

const h2Element = document.querySelector('h2');
h2Element.addEventListener('click', () => {
    h2Element.style.backgroundColor = 'red';
});

//Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

const h3Element = document.querySelector("h3");
h3Element.addEventListener("click", function() {
  h3Element.style.display = "none";
});

//Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

const boldButton = document.getElementById("mybtn");
const paragraphs = document.querySelectorAll("p");

boldButton.addEventListener("click", function() {
  paragraphs.forEach(function(paragraph) {
    paragraph.style.fontWeight = "bold";
  });
});

//Exercise 2 : Work with forms

