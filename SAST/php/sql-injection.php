<?php

if (PHP_SAPI === 'cli') {
    parse_str(implode('&', array_slice($argv, 1)), $_GET);
}

$file_db = new PDO('sqlite:../database/database.sqlite');

$id = isset($_GET['id']) ? (int) $_GET['id'] : 1;

$stmt = $file_db->prepare('SELECT * FROM employees WHERE employeeId = :id');
$stmt->bindParam(':id', $id, PDO::PARAM_INT);
$stmt->execute();

foreach ($stmt as $row) {
    $employee = $row['LastName'] . " - " . $row['Email'] . "\n";

    echo $employee;
}

?>