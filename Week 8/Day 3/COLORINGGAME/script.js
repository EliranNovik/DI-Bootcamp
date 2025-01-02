const palette = document.getElementById("palette");
const grid = document.getElementById("grid");
const clearBtn = document.getElementById("clear-btn");


function createGrid(rows, cols) {
  for (let i = 0; i < rows * cols; i++) {
    const cell = document.createElement("div");
    cell.classList.add("cell");

    cell.addEventListener("mousedown", colorCell);
    cell.addEventListener("mouseover", colorCellOnDrag);

    grid.appendChild(cell);
  }
}

function colorCell(e) {
  isMouseDown = true;
  e.target.style.backgroundColor = currentColor;
}

function colorCellOnDrag(e) {
  if (isMouseDown) {
    e.target.style.backgroundColor = currentColor;
  }
}

document.addEventListener("mouseup", () => {
  isMouseDown = false;
});

palette.addEventListener("click", (e) => {
  if (e.target.classList.contains("color")) {
    const colors = palette.querySelectorAll(".color");
    colors.forEach((col) => (col.style.border = "2px solid transparent"));

    currentColor = e.target.style.backgroundColor;

    e.target.style.border = "2px solid #333";
  }
});

clearBtn.addEventListener("click", () => {
  const cells = document.querySelectorAll(".cell");
  cells.forEach((cell) => {
    cell.style.backgroundColor = "white";
  });
});

createGrid(40, 40);
