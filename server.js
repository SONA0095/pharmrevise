const express = require("express");
const cors = require("cors");
require("dotenv").config();
const connectDB = require("./db");
const routes = require("./routes");

const app = express();
app.use(express.json());
app.use(cors());

connectDB(); // Connect to MongoDB

app.use("/api", routes); // Use API Routes

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
