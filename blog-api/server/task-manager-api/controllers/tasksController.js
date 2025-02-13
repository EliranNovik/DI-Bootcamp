const fs = require("fs");
const path = require("path");

const tasksFilePath = path.join(__dirname, "../tasks.json");

// Utility function to read tasks from JSON
const readTasks = () => {
  try {
    const data = fs.readFileSync(tasksFilePath, "utf8");
    return JSON.parse(data);
  } catch (error) {
    return [];
  }
};

// Utility function to write tasks to JSON
const writeTasks = (tasks) => {
  fs.writeFileSync(tasksFilePath, JSON.stringify(tasks, null, 2));
};

// ✅ GET all tasks
const getTasks = (req, res) => {
  const tasks = readTasks();
  res.json(tasks);
};

// ✅ GET a single task by ID
const getTaskById = (req, res) => {
  const tasks = readTasks();
  const task = tasks.find((t) => t.id === parseInt(req.params.id));

  if (!task) {
    return res.status(404).json({ error: "Task not found" });
  }
  res.json(task);
};

// ✅ POST create a new task
const createTask = (req, res) => {
  const { title, description } = req.body;

  if (!title || !description) {
    return res.status(400).json({ error: "Title and description are required" });
  }

  const tasks = readTasks();
  const newTask = { id: tasks.length + 1, title, description };
  tasks.push(newTask);
  writeTasks(tasks);

  res.status(201).json(newTask);
};

// ✅ PUT update a task
const updateTask = (req, res) => {
  const tasks = readTasks();
  const taskIndex = tasks.findIndex((t) => t.id === parseInt(req.params.id));

  if (taskIndex === -1) {
    return res.status(404).json({ error: "Task not found" });
  }

  const { title, description } = req.body;
  if (title) tasks[taskIndex].title = title;
  if (description) tasks[taskIndex].description = description;

  writeTasks(tasks);
  res.json(tasks[taskIndex]);
};

// ✅ DELETE a task
const deleteTask = (req, res) => {
  let tasks = readTasks();
  const taskIndex = tasks.findIndex((t) => t.id === parseInt(req.params.id));

  if (taskIndex === -1) {
    return res.status(404).json({ error: "Task not found" });
  }

  tasks = tasks.filter((t) => t.id !== parseInt(req.params.id));
  writeTasks(tasks);

  res.json({ message: "Task deleted" });
};

module.exports = {
  getTasks,
  getTaskById,
  createTask,
  updateTask,
  deleteTask,
};
