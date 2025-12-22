---
id: 418f4c26-f22f-4506-af46-018857482c6f
name: Demonstrate-PHP-Type-Juggling-with-Empty-Array-Hashing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.678011+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - php
  - type-juggling
  - magic-hashes
  - auth-bypass
  - null-statements
commands:
  - '[[commands/php-execute-empty-array-hash]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
---

# Demonstrate-PHP-Type-Juggling-with-Empty-Array-Hashing

## Summary

This procedure demonstrates how PHP's type juggling feature can be exploited in authentication mechanisms by hashing an empty array, which results in a NULL value for both SHA1 and MD5 functions. This behavior can lead to authentication bypasses if the application uses loose comparisons (e.g., ==) where NULL is treated as equivalent to other falsy values like 0 or empty strings, allowing attackers to craft inputs that match stored hashes without knowing the password.

## Description

PHP type juggling allows automatic type conversions during comparisons, which can be abused to bypass authentication checks that compare hashed inputs loosely. In vulnerable applications, providing an empty array as input to hash functions like sha1() or md5() returns NULL. Due to loose equality (==), this NULL can match certain stored values, enabling unauthorized access. This technique is particularly relevant for web applications using PHP for user authentication, such as login forms that hash passwords without strict type checking. Attackers can test this by injecting array-like inputs or exploiting deserialization flaws. The procedure focuses on replicating this hashing behavior to understand and test for the vulnerability in a controlled environment, such as a local PHP setup or a vulnerable app like DVWA.

## Requirements

1. A PHP environment (version 5.x or later, where type juggling is prominent) installed on the testing machine.
2. Access to a vulnerable PHP application or a local script for testing authentication logic.
3. Basic knowledge of PHP syntax and web application testing tools like Burp Suite for intercepting requests.
4. No elevated privileges required, but shell access to run PHP commands is needed.

## Defense

- Use strict type comparisons (===) in authentication logic to prevent type juggling exploits.
- Avoid hashing non-string inputs; validate and sanitize all user inputs before hashing.
- Implement proper password storage with algorithms like bcrypt or Argon2, and enforce multi-factor authentication (MFA).
- Monitor application logs for anomalous hashing attempts or failed logins with unusual inputs.

## Objectives

1. Demonstrate that hashing an empty array in PHP returns NULL for sha1 and md5.
2. Understand how this NULL value can be leveraged in type juggling for authentication bypass.
3. Test and verify the behavior in a PHP interpreter to identify vulnerable code patterns.

## Instructions

### Step 1: Set Up PHP Environment

**Context**: Ensure PHP is installed and accessible via command line to execute code snippets safely. This step verifies the environment supports the required functions.

Run the PHP version check using a basic command.

**Command** ([[commands/php-version-check]]):
```bash
php -v
```

> This command displays the installed PHP version. Expected output includes version details like "PHP 7.4.3" to confirm compatibility.

### Step 2: Execute Empty Array Hashing

**Context**: Run the core demonstration code to hash an empty array, showing that both sha1() and md5() return NULL. This illustrates the type juggling vulnerability point.

Use the PHP interactive mode or one-liner to execute the snippet. Reference the code snippet for the exact PHP logic.

**Command** ([[commands/php-execute-empty-array-hash]]):
```bash
php -r 'var_dump(sha1([])); var_dump(md5([]));'
```

> This executes the PHP code directly from the command line. The var_dump() function outputs the type and value, revealing NULL for both hashes. If the output shows NULL, the behavior is confirmed, indicating potential for type juggling exploits in auth checks.

### Step 3: Test in Authentication Context

**Context**: Apply the NULL hash in a simulated login to observe type juggling. Create a simple PHP script mimicking vulnerable auth (e.g., if (hash($input) == $stored_hash)).

Save the demonstration code to a file (e.g., test.php) and execute it, or inject via a web form if testing a vulnerable app.

**Command** ([[commands/php-run-auth-test-script]]):
```bash
php test.php
```

> Assuming test.php contains logic like $stored = '0'; if (sha1([]) == $stored) { echo 'Bypass successful'; }, the output should indicate a match due to NULL == 0. This validates the bypass potential.

If testing a web app, use a tool like curl to submit an array input (e.g., password[]=) and check for successful login.
