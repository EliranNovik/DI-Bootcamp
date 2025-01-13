/**
 * Checks if two strings are anagrams of each other.
 * @param {string} str1 - First string
 * @param {string} str2 - Second string
 * @return {boolean} - True if str1 is an anagram of str2, otherwise false.
 */
function isAnagram(str1, str2) {
    // Remove any non-alphabetic characters (e.g., spaces, punctuation) and convert to lowercase
    const normalize = (str) =>
      str.toLowerCase().replace(/[^a-z0-9]/g, "");
  
    const normalizedStr1 = normalize(str1);
    const normalizedStr2 = normalize(str2);
  
    // If lengths differ after normalization, they can't be anagrams
    if (normalizedStr1.length !== normalizedStr2.length) {
      return false;
    }
  
    // Sort the letters of each string and compare
    const sortedStr1 = normalizedStr1.split("").sort().join("");
    const sortedStr2 = normalizedStr2.split("").sort().join("");
  
    return sortedStr1 === sortedStr2;
  }
  
  // DOM Elements
  const string1Input = document.getElementById("string1");
  const string2Input = document.getElementById("string2");
  const checkBtn = document.getElementById("checkBtn");
  const resultP = document.getElementById("result");
  
  // Event Listener
  checkBtn.addEventListener("click", () => {
    const str1 = string1Input.value.trim();
    const str2 = string2Input.value.trim();
  
    if (!str1 || !str2) {
      resultP.textContent = "Please enter text in both fields.";
      return;
    }
  
    const answer = isAnagram(str1, str2);
    resultP.textContent = answer
      ? `"${str1}" is an anagram of "${str2}."`
      : `"${str1}" is NOT an anagram of "${str2}."`;
  });
  