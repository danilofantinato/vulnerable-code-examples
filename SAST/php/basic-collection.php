<?php

// Cross-Site Scripting (XSS)
$name = htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8');
echo('Hello ' . $name);

// SQL Injection
$id = (int) $_POST['id'];
$conn = new mysqli($servername, $username, $password, $dbname);
$stmt = $conn->prepare("SELECT user FROM users WHERE id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
$result = $stmt->get_result();
$stmt->close();
$conn->close();

// Command Injection
// Avoid executing external commands from user input

// Deprecated Function
$words = explode(":", "split:this");

?>