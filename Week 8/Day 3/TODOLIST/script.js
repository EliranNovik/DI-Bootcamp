// We'll store tasks as objects in this array
const tasks = [];

const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");
const listTasks = document.getElementById("listTasks");
const clearAllBtn = document.getElementById("clearAllBtn");

taskForm.addEventListener("submit", (e) => {
  e.preventDefault(); // Prevents page from reloading

  const text = taskInput.value.trim();
  if (!text) {
    alert("Please enter a task.");
    return;
  }

  const taskObj = {
    id: Date.now(),       // unique ID
    text,                 // the task text
    isCompleted: false    // by default, it's not completed
  };

  tasks.push(taskObj);

  addTaskToDOM(taskObj);

  taskInput.value = "";
});

/**
 * Adds a task item to the DOM
 * @param {object} task - { id, text, isCompleted }
 */
function addTaskToDOM(task) {
  const taskItem = document.createElement("div");
  taskItem.classList.add("taskItem");
  taskItem.dataset.id = task.id; // store ID for reference

  const taskContent = document.createElement("div");
  taskContent.classList.add("taskContent");

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = task.isCompleted; // reflect current state

  const label = document.createElement("label");
  label.classList.add("taskLabel");
  label.textContent = task.text;

  if (task.isCompleted) {
    label.classList.add("completed");
  }

  checkbox.addEventListener("change", () => {
    task.isCompleted = checkbox.checked;
    if (task.isCompleted) {
      label.classList.add("completed");
    } else {
      label.classList.remove("completed");
    }
  });

  const removeBtn = document.createElement("button");
  removeBtn.classList.add("removeBtn");
  removeBtn.innerText = "X";

  removeBtn.addEventListener("click", () => {
    removeTask(task.id);
  });

  // Assemble
  taskContent.appendChild(checkbox);
  taskContent.appendChild(label);

  taskItem.appendChild(taskContent);
  taskItem.appendChild(removeBtn);

  listTasks.appendChild(taskItem);
}

/**
 * Remove a task from the array and from the DOM
 * @param {number} taskId - the unique ID of the task
 */
function removeTask(taskId) {
  const index = tasks.findIndex((t) => t.id === taskId);
  if (index !== -1) {
    tasks.splice(index, 1);
  }

  const item = document.querySelector(`.taskItem[data-id="${taskId}"]`);
  if (item) {
    listTasks.removeChild(item);
  }
}

clearAllBtn.addEventListener("click", () => {
  tasks.length = 0;
  listTasks.innerHTML = "";   // clear the DOM
});
