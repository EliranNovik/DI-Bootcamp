const express = require("express");
const tasksRouter = require("./routes/tasksRouter");

const app = express();
const PORT = process.env.PORT || 5080;

app.use(express.json()); // Middleware to parse JSON
app.use("/tasks", tasksRouter);

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
