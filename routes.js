const express = require("express");
const router = express.Router();

// Sample route
router.get("/", (req, res) => {
  res.send("Welcome to PharmReVise API 🚀");
});

// Add future API endpoints here

module.exports = router;
