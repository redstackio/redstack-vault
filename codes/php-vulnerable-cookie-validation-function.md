---
id: ea48902c-a822-4290-8c5f-3aba9e040771
name: php-vulnerable-cookie-validation-function
type: code
language: php
verified: true
created_at: '2023-04-06T03:56:40.699017+00:00'
updated_at: '2023-04-06T03:56:40.708394+00:00'
platforms:
  - Web
  - PHP
tags:
  - vulnerable-code
  - type-juggling
validated: true
---

# php-vulnerable-cookie-validation-function

## Code

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

## Description

This PHP function validates a cookie's HMAC using loose comparison (!=), making it vulnerable to type juggling attacks where magic hashes coerce equality. It checks username|expiration HMAC against provided 'hmac' and ensures expiration hasn't passed.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $cookie | Associative array with 'username', 'hmac', '$expiration' | ['username' => 'user', 'hmac' => 'hash', '$expiration' => '1234567890'] |
| $key | Secret key for HMAC computation | 'secretkey123' |

## Usage

Embed in a PHP web app's auth handler. Call as validate_cookie($_COOKIE, $secret_key) before granting session access. Exploit by setting cookies with magic usernames to bypass HMAC check via loose comparison.

## Detection

- Static code analysis for == or != in hash comparisons.
- Runtime monitoring for MD5 usage or anomalous cookie values (e.g., usernames like '240610708').
- WAF rules blocking requests with known magic hash inputs.

## Related

- [[procedures/Bypass-PHP-Authentication-with-Type-Juggling-and-Magic-Hashes]]
