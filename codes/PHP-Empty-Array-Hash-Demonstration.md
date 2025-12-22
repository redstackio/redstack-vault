---
id: 62936542-d94a-4525-b865-7f1e39c011a9
name: PHP-Empty-Array-Hash-Demonstration
type: code
language: php
verified: true
created_at: '2023-04-06T03:56:40.673432+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - PHP
tags:
  - php
  - hashing
  - type-juggling
  - 'null'
validated: true
---

# PHP-Empty-Array-Hash-Demonstration

## Code

```php
var_dump(sha1([])); # NULL
var_dump(md5([]));  # NULL
```

## Description

This PHP code snippet demonstrates hashing an empty array with sha1() and md5(), both of which return NULL because arrays are not valid string inputs for these functions. This is key to understanding type juggling exploits where NULL loosely equals other values in authentication comparisons.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The code uses a fixed empty array []; no variables to substitute | N/A |

## Usage

Embed this snippet in a PHP script or execute via command line (php -r) during vulnerability assessment of PHP web apps. Use it to test if auth logic vulnerable to inputs that coerce to NULL, such as form fields with array notation (e.g., password[]=).

## Detection

- Review PHP source code for loose comparisons (==) on hash outputs.
- Log hashing function calls with non-string inputs.
- Web application firewall (WAF) rules for array-like payloads in auth fields.
- Runtime errors or warnings for invalid hash inputs in PHP error logs.

## Related

- [[procedures/Demonstrate-PHP-Type-Juggling-with-Empty-Array-Hashing]]
- [[commands/php-execute-empty-array-hash]]
