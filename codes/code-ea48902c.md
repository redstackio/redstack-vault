---
id: ea48902c-a822-4290-8c5f-3aba9e040771
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:56:40.699017+00:00'
updated_at: '2023-04-06T03:56:40.708394+00:00'
---

# Code Snippet ea48902c

**Language**: PHP

```php
function validate_cookie($cookie, $key) {
    $hash = hash_hmac('md5', $cookie['username'] . '|' . $cookie['$expiration'], $key);
    if ($cookie['hmac'] != $hash) { // loose comparison
        return false;
    }
    $expiration = intval($cookie['$expiration']);
    if ($expiration < time()) {
        return false;
    }
    return true;
}
```
