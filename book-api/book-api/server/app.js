const express = require("express");

const app = express();
const PORT = process.env.PORT || 5040;

// Middleware to parse JSON
app.use(express.json());

// Sample data: Books array
let books = [
    { id: 1, title: "Book One", author: "Author A", publishedYear: 2000 },
    { id: 2, title: "Book Two", author: "Author B", publishedYear: 2010 },
    { id: 3, title: "Book Three", author: "Author C", publishedYear: 2020 }
];

// 📌 GET all books (Read all)
app.get("/api/books", (req, res) => {
    res.json(books);
});

// 📌 GET a book by ID (Read)
app.get("/api/books/:bookId", (req, res) => {
    const bookId = parseInt(req.params.bookId);
    const book = books.find(b => b.id === bookId);

    if (!book) {
        return res.status(404).json({ message: "Book not found" });
    }

    res.json(book);
});

// 📌 POST a new book (Create)
app.post("/api/books", (req, res) => {
    const { title, author, publishedYear } = req.body;

    if (!title || !author || !publishedYear) {
        return res.status(400).json({ message: "All fields are required" });
    }

    const newBook = {
        id: books.length + 1,
        title,
        author,
        publishedYear
    };

    books.push(newBook);
    res.status(201).json(newBook);
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
