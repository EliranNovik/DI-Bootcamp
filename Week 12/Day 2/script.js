const API_KEY = "3026e64c7dfda0f4c2f5b562";
const BASE_URL = `https://v6.exchangerate-api.com/v6/${API_KEY}`;

// DOM Elements
const fromCurrency = document.getElementById("fromCurrency");
const toCurrency = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");
const convertButton = document.getElementById("convert");
const switchButton = document.getElementById("switch");
const result = document.getElementById("result");

// Fetch supported currencies and populate dropdowns
async function fetchCurrencies() {
  try {
    const response = await fetch(`${BASE_URL}/codes`);
    const data = await response.json();

    if (data.result === "success") {
      populateDropdowns(data.supported_codes);
    } else {
      throw new Error("Failed to fetch supported currencies.");
    }
  } catch (error) {
    console.error("Error fetching currencies:", error);
  }
}

// Populate currency dropdowns
function populateDropdowns(codes) {
  codes.forEach(([code, name]) => {
    const option = document.createElement("option");
    option.value = code;
    option.textContent = `${code} - ${name}`;
    fromCurrency.appendChild(option.cloneNode(true));
    toCurrency.appendChild(option);
  });

  // Set default values
  fromCurrency.value = "USD";
  toCurrency.value = "EUR";
}

// Convert currency
async function convertCurrency() {
  const from = fromCurrency.value;
  const to = toCurrency.value;
  const amount = parseFloat(amountInput.value);

  if (!amount || amount <= 0) {
    result.textContent = "Please enter a valid amount.";
    return;
  }

  try {
    const response = await fetch(`${BASE_URL}/pair/${from}/${to}/${amount}`);
    const data = await response.json();

    if (data.result === "success") {
      result.textContent = `${amount} ${from} = ${data.conversion_result.toFixed(2)} ${to}`;
    } else {
      throw new Error("Conversion failed.");
    }
  } catch (error) {
    console.error("Error converting currency:", error);
    result.textContent = "Error converting currency. Try again later.";
  }
}

// Switch currencies
function switchCurrencies() {
  const temp = fromCurrency.value;
  fromCurrency.value = toCurrency.value;
  toCurrency.value = temp;
  result.textContent = ""; // Clear the result after switching
}

// Event Listeners
convertButton.addEventListener("click", convertCurrency);
switchButton.addEventListener("click", switchCurrencies);

// Fetch currencies on page load
fetchCurrencies();
