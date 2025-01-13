const robots = [
    {
      id: 1,
      name: 'Luka Doncic',
      username: 'Luka',
      email: 'Ldoncic@mavericks.nba',
      image: 'https://robohash.org/Luka%20Doncic'
    },
    {
      id: 2,
      name: 'Kyrie Irving',
      username: 'Kyrie',
      email: 'Kirving@mavericks.nba',
      image: 'https://robohash.org/Kyrie%20Irving'
    },
    {
      id: 3,
      name: 'Klay Thompson',
      username: 'Klay',
      email: 'Kthompson@mavericks.nba',
      image: 'https://robohash.org/Klay%20Thompson'
    },
    {
      id: 4,
      name: 'Daniel Gafford',
      username: 'Daniel',
      email: 'Dgafford@mavericks.nba',
      image: 'https://robohash.org/Daniel%20Gafford'
    },
    {
      id: 5,
      name: 'Spencer Dinwiddie',
      username: 'Spencer',
      email: 'Sdinwiddie@mavericks.nba',
      image: 'https://robohash.org/Spencer%20Dinwiddie'
    },
    {
      id: 6,
      name: 'Maxi Kleber',
      username: 'Maxi',
      email: 'Mkleber@mavericks.nba',
      image: 'https://robohash.org/Maxi%20Kleber'
    },
    {
      id: 7,
      name: 'Derick Lively II',
      username: 'Derick',
      email: 'Dliveley@mavericks.nba',
      image: 'https://robohash.org/Derick%20Lively%20II'
    },
    {
      id: 8,
      name: 'Dwight Powell',
      username: 'Dwight',
      email: 'Dpowell@mavericks.nba',
      image: 'https://robohash.org/Dwight%20Powell'
    },
    {
      id: 9,
      name: 'P.J. Washington',
      username: 'P.J.',
      email: 'PJwashington@mavericks.nba',
      image:'https://robohash.org/P.J.%20Washington'
    },
    {
      id: 10,
      name: 'Markieff Morris',
      username: 'Markieff',
      email: 'Mmorris@mavericks.nba',
      image:'https://robohash.org/Markieff%20Morris'
    }
];

const robotsContainer = document.getElementById("robotsContainer");
const searchInput = document.getElementById("searchInput");

/**
 * @param {Array} robotsArray 
 */
function displayRobots(robotsArray) {
  robotsContainer.innerHTML = "";

  robotsArray.forEach(robot => {
    const card = document.createElement("div");
    card.classList.add("robot-card");

    card.innerHTML = `
      <img src="${robot.image}" alt="${robot.name}" />
      <h2>${robot.name}</h2>
      <p>${robot.email}</p>
    `;

    robotsContainer.appendChild(card);
  });
}

displayRobots(robots);

searchInput.addEventListener("keyup", () => {
  const query = searchInput.value.toLowerCase();
  const filtered = robots.filter(robot => {
    return (
      robot.name.toLowerCase().includes(query) ||
      robot.username.toLowerCase().includes(query) ||
      robot.email.toLowerCase().includes(query)
    );
  });
  displayRobots(filtered);
});