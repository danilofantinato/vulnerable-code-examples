<?php

// Whitelist allowed class names
$allowedClasses = ['AllowedClass1', 'AllowedClass2', 'AllowedClass3'];

$input = $_GET["input"];

// Validate input against whitelist
if (in_array($input, $allowedClasses)) {
    call_user_func($input, "abc");
    $input();
    $o = new $input();
} else {
    // Handle invalid input
    echo "Invalid input";
    // Log the attempt or take appropriate action
}

?>