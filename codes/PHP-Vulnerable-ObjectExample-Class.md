---
id: d1e24215-3996-4664-8f91-7e0478a69a5c
name: PHP-Vulnerable-ObjectExample-Class
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:55:59.357350+00:00'
updated_at: '2023-04-06T03:55:59.362541+00:00'
platforms:
  - Web
  - PHP
tags:
  - vulnerable
  - deserialization
  - example
validated: true
---

# PHP-Vulnerable-ObjectExample-Class

## Code

```php
<?php
class ObjectExample
{
  var $guess;
  var $secretCode;
}

$obj = unserialize($_GET['input']);

if($obj) {
    $obj->secretCode = rand(500000,999999);
    if($obj->guess === $obj->secretCode) {
        echo "Win";
    }
}
?>
```

## Description

This code demonstrates a vulnerable PHP class and deserialization routine. It unserializes user input directly from $_GET['input'] without validation, allowing object injection to manipulate $guess and $secretCode properties during property access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | This is static vulnerable code; no runtime variables. | N/A |

## Usage

Deploy this as vuln.php on a PHP server for testing object injection. Access via ?input=<serialized_payload> to trigger deserialization and observe property manipulation or method invocation.

## Detection

- Static code scans for unserialize(user_input).
- Web logs showing suspicious query params with 'O:' or 's:' patterns.
- Runtime errors from invalid property access during deserialization.

## Related

- [[procedures/Exploit-PHP-Object-Injection-for-Arbitrary-Code-Execution]]
