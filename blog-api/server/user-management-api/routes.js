const express = require("express");
const bcrypt = require("bcryptjs");
const fs = require("fs");
const path = require("path");

const router = express.Router();
const usersFile = path.join(__dirname, "users.json");

// Load users from JSON
const loadUsers = () => {
  if (!fs.existsSync(usersFile)) return [];
  const data = fs.readFileSync(usersFile, "utf-8");
  return JSON.parse(data);
};

// Save users to JSON
const saveUsers = (users) => {
  fs.writeFileSync(usersFile, JSON.stringify(users, null, 2), "utf-8");
};

// 🔹 Register a new user
router.post("/register", async (req, res) => {
  const { name, lastName, email, username, password } = req.body;
  if (!name || !lastName || !email || !username || !password) {
    return res.status(400).json({ message: "All fields are required" });
  }

  let users = loadUsers();
  const existingUser = users.find((user) => user.username === username);
  if (existingUser) {
    return res.status(400).json({ message: "Username already exists" });
  }

  const hashedPassword = await bcrypt.hash(password, 10);
  const newUser = { id: users.length + 1, name, lastName, email, username, password: hashedPassword };
  users.push(newUser);
  saveUsers(users);

  res.json({ message: `Hello ${name}, your account is now created!` });
});

// 🔹 Login user
router.post("/login", async (req, res) => {
  const { username, password } = req.body;
  let users = loadUsers();

  const user = users.find((user) => user.username === username);
  if (!user) {
    return res.status(404).json({ message: "Username is not registered" });
  }

  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) {
    return res.status(400).json({ message: "Invalid password" });
  }

  res.json({ message: `Hi ${user.name}, welcome back again!` });
});

// 🔹 Get all users
router.get("/users", (req, res) => {
  let users = loadUsers();
  res.json(users);
});

// 🔹 Get a user by ID
router.get("/users/:id", (req, res) => {
  let users = loadUsers();
  const user = users.find((u) => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: "User not found" });

  res.json(user);
});

// 🔹 Update user by ID
router.put("/users/:id", (req, res) => {
  let users = loadUsers();
  const index = users.findIndex((u) => u.id === parseInt(req.params.id));

  if (index === -1) return res.status(404).json({ message: "User not found" });

  users[index] = { ...users[index], ...req.body };
  saveUsers(users);

  res.json({ message: "User updated successfully" });
});

module.exports = router;
