// 1. Create a variable called 'sentence' containing 'not' and 'bad'
let sentence = "The movie is not that bad, I like it";

// 2. Create variables for the positions of 'not' and 'bad'
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

// 3. Check if 'bad' comes after 'not'
if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
  let firstPart = sentence.slice(0, wordNot);
  let secondPart = sentence.slice(wordBad + 3);
  let newSentence = firstPart + "good" + secondPart;

  console.log(newSentence);
} else {
  console.log(sentence);
}
