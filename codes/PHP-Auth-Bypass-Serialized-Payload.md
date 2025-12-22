---
id: 6c3691ec-467f-4a8d-b2ed-e3caaef673f8
name: PHP-Auth-Bypass-Serialized-Payload
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:55:59.332817+00:00'
updated_at: '2023-04-06T03:55:59.339478+00:00'
platforms:
  - Web
  - PHP
tags:
  - payload
  - deserialization
  - type-juggling
validated: true
---

# PHP-Auth-Bypass-Serialized-Payload

## Code

```php
a:2:{s:8:"username";b:1;s:8:"password";b:1;}
```

## Description

This serialized PHP array payload sets 'username' and 'password' to boolean true (b:1). When unserialized in a vulnerable application, it exploits PHP's loose equality (==) and type juggling to bypass authentication checks, as true coerces to a value that may match expected strings like 'admin'.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| s:8:"username" | String key for username (length 8 for 'username') | N/A |
| b:1 | Boolean true value for username | N/A |
| s:8:"password" | String key for password (length 8 for 'password') | N/A |
| b:1 | Boolean true value for password | N/A |

Note: Adjust string lengths (s:N) if the application expects different key names or values.

## Usage

Encode this payload (URL-encode if needed) and set it as the 'auth' cookie in HTTP requests to the target PHP application. Use tools like curl or Burp Suite to inject it during login or direct access to protected pages. Test against endpoints that deserialize the cookie for auth validation.

## Detection

- Inspect cookies for serialized PHP data (starts with 'a:', 's:', 'b:') using WAF or proxy logs.
- Monitor for unserialize() calls on user input in application logs.
- Anomaly detection: Unusual admin access without login attempts.
- PHP error logs showing deserialization warnings.

## Related

- [[procedures/Authentication-Bypass-via-PHP-Deserialization-and-Type-Juggling]]
- [[commands/curl-send-php-serialized-cookie]]
