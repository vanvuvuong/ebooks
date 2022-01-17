const express = require("express");
const app = express();
const hobbies = [
	"Swiming", "Diving", "Jogging", "Cooking", "Singing"
]

app.listen(3000, "0.0.0.0"), () => {
    console.log("Application is listening 0.0.0.0:3000");
}
app.get("/", (req, res) => {
	res.send("Sample Application: Hello World !");
})
app.get("/hobbies", (req, res) => {
	res.send(hobbies);
})
app.get("/status", (req, res) => {
	res.send("OK");
})
app.get("/color", (req, res) => {
	res.send("RED, GREEN, BLUE");
})

