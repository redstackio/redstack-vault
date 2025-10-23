---
id: 6de858e1-e49c-4a71-85a0-d25f0f0c96dc
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:55:59.332760+00:00'
updated_at: '2023-04-06T03:55:59.339403+00:00'
---

# Code Snippet 6de858e1

**Language**: PHP

```php
<?php
$data = unserialize($_COOKIE['auth']);

if ($data['username'] == $adminName && $data['password'] == $adminPassword) {
    $admin = true;
} else {
    $admin = false;
}
```


