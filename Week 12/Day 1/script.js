const getCharacterBtn = document.getElementById("getCharacterBtn");
const loading = document.getElementById("loading");
const characterInfo = document.getElementById("characterInfo");
const error = document.getElementById("error");

const nameEl = document.getElementById("name");
const heightEl = document.getElementById("height");
const genderEl = document.getElementById("gender");
const birthYearEl = document.getElementById("birthYear");
const homeWorldEl = document.getElementById("homeWorld");

async function fetchCharacter() {
  loading.classList.remove("hidden");
  characterInfo.classList.add("hidden");
  error.classList.add("hidden");

  try {
    const randomId = Math.floor(Math.random() * 83) + 1;

    const response = await fetch(`https://www.swapi.tech/api/people/${randomId}`);
    if (!response.ok) throw new Error("Character not found");

    const data = await response.json();
    const character = data.result.properties;

    const homeWorldResponse = await fetch(character.homeworld);
    const homeWorldData = await homeWorldResponse.json();
    const homeWorld = homeWorldData.result.properties.name;

    nameEl.textContent = character.name;
    heightEl.textContent = `${character.height} cm`;
    genderEl.textContent = character.gender;
    birthYearEl.textContent = character.birth_year;
    homeWorldEl.textContent = homeWorld;

    characterInfo.classList.remove("hidden");
    loading.classList.add("hidden");
  } catch (err) {
    error.classList.remove("hidden");
    loading.classList.add("hidden");
  }
}

getCharacterBtn.addEventListener("click", fetchCharacter);
