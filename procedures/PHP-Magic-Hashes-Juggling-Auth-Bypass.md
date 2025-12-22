---
id: da62c60d-16b3-4608-a9b5-1fcf574415ab
name: PHP-Magic-Hashes-Juggling-Auth-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.736533+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - php
  - type-juggling
  - magic-hashes
  - auth-bypass
  - '[[tags/Example vulnerable code]]'
  - '[[tags/PHP Juggling type and magic hashes]]'
  - '[[tags/Type Juggling]]'
commands:
  - '[[commands/generate-php-hmac-hash]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
---

# PHP-Magic-Hashes-Juggling-Auth-Bypass

## Summary

This procedure exploits PHP's loose type comparison (== operator) in authentication mechanisms by using 'magic hashes'—specially crafted MD5 HMAC hashes starting with '0e' that PHP interprets as scientific notation for zero (0.0). This allows bypassing login checks where the application compares a generated HMAC hash against a user-provided value, as both resolve to 0 in loose comparison, granting unauthorized access without knowing the correct password.

## Description

PHP's type juggling feature attempts to convert operands to compatible types during loose comparisons (==), leading to vulnerabilities in authentication logic that relies on hashing user input like passwords or tokens. In vulnerable applications, login might validate if (hash_hmac('md5', $timestamp . '|' . $username, $secret) == $provided_hash), but if the secret is predictable (e.g., the username 'admin') and timestamps are sequential, an attacker can precompute HMAC values for various timestamps until finding one that starts with '0e' followed by digits (e.g., '0e12345678901234567890'), which equals 0.0. Submitting this as the password bypasses the check since the legitimate hash for the current timestamp might also resolve to 0 in comparison.

This technique targets web applications using outdated PHP practices, common in legacy systems or poorly coded auth endpoints. It requires no privileges beyond network access to the login form and can lead to full account takeover. Detection is challenging without strict typing or logging of failed comparisons.

## Requirements

1. Network access to the vulnerable PHP application's login endpoint (e.g., via browser or proxy like Burp Suite).
2. Knowledge of the HMAC algorithm (typically MD5), key (often the username like 'admin'), and data format (e.g., timestamp prefixed to username).
3. A tool or environment to compute PHP hashes (PHP interpreter installed locally).
4. The application must use loose == for hash comparison and generate dynamic data like timestamps server-side.

## Defense

- Use strict comparison operators (=== and !==) for all authentication checks to prevent type coercion.
- Validate and sanitize all user inputs, treating hashes as strings without implicit conversion.
- Implement rate limiting on login attempts and monitor for unusual hash patterns in logs.
- Upgrade to modern PHP versions with better type handling and use secure libraries like Sodium for hashing.
- Employ web application firewalls (WAFs) to detect anomalous input patterns like '0e' prefixed strings.

## Objectives

1. Identify vulnerable authentication endpoints using loose PHP type comparisons.
2. Generate magic HMAC hashes that bypass hash validation via type juggling.
3. Achieve unauthorized access to the target account (e.g., admin privileges).
4. Access sensitive data or perform actions post-login.

## Instructions

### Step 1: Identify Vulnerable Authentication Logic

**Context**: Analyze the login form to confirm it uses HMAC-MD5 with a predictable key (e.g., username) and dynamic data like timestamps. Use browser dev tools or a proxy to inspect requests and responses for hash-related parameters.

If the key and data format are unknown, assume common patterns like key='admin', data=$timestamp (Unix epoch). Test by submitting known values and observing errors.

**Success Criteria**: Confirmation of loose comparison vulnerability, e.g., via error messages or source code review if available.

### Step 2: Generate Magic HMAC Hashes

**Context**: Precompute HMAC-MD5 hashes for sequential timestamps using the assumed key and data format until finding one starting with '0e' followed by 26 digits (MD5 length). This hash will equal 0 in loose PHP comparison.

Use the [[commands/generate-php-hmac-hash]] command to compute individual hashes, scripting a loop if needed to test multiple timestamps (e.g., from 1424869663 to 1835970773 as in examples).

**Command** ([[commands/generate-php-hmac-hash]]):
```php
php -r "echo hash_hmac('md5', '$_TIMESTAMP', '$_KEY');"
```

> Replace $_TIMESTAMP with a Unix epoch value (e.g., 1424869663) and $_KEY with the secret (e.g., 'admin'). Expected output: A 32-character hex MD5 hash. Repeat until output starts with '0e' and consists of digits (e.g., '0e174892301580325162390102935332'). Reference [[codes/HMAC-Magic-Hash-Examples]] for sample vulnerable hashes.

**Success Criteria**: At least one magic hash identified that PHP will treat as 0.0.

### Step 3: Submit Magic Hash for Authentication Bypass

**Context**: Intercept the login request using a proxy (e.g., Burp Suite) and replace the password field with the magic hash. Ensure the timestamp in the request matches one used for hash generation, or adjust if the app includes it client-side.

Submit the form with username='admin' and password='0e174892301580325162390102935332' (or your found hash).

**Success Criteria**: Successful login redirect or session token issued, indicating bypass achieved.

### Step 4: Verify Access and Exfiltrate Data

**Context**: Post-login, navigate to sensitive areas (e.g., admin dashboard) to confirm elevated access. Capture any tokens or data for further exploitation.

Use browser tools to inspect session cookies and extract valuables.

**Success Criteria**: Access to restricted resources without valid credentials.
