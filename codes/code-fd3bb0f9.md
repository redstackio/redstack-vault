---
id: fd3bb0f9-3a2c-4239-aabd-4b9bf4a874d9
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:56:40.612692+00:00'
updated_at: '2023-04-06T03:56:40.632316+00:00'
---

# Code Snippet fd3bb0f9

**Language**: PHP

```php
var_dump('0010e2' == '1e3');           # true
var_dump('0xABCdef' == ' 0xABCdef');     # true PHP 5.0 / false PHP 7.0
var_dump('0xABCdef' == '     0xABCdef'); # true PHP 5.0 / false PHP 7.0
var_dump('0x01' == 1)                # true PHP 5.0 / false PHP 7.0
var_dump('0x1234Ab' == '1193131');
```
