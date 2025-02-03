const products = require("./products.js"); 

function findProduct(productName) {
    return products.find(product => product.name === productName);
}

console.log(findProduct("Wireless Mouse"));
console.log(findProduct("Mechanical Keyboard"));
console.log(findProduct("Bluetooth Speaker"));
console.log(findProduct("Gaming Chair"));
console.log(findProduct("Smartphone Stand"));
