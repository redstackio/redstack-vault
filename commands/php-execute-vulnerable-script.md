---
id: cmd-php-execute-vuln
data: php vulnerable_script.php
tags:
  - exploitation
  - php
type: command
output: AddressSanitizer error report and PHP crash
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.630Z'
verified: false
validated: true
submitted: true
---
# php-execute-vulnerable-script

## Command

```bash
php vulnerable_script.php
```

## Description

Executes a PHP script designed to trigger the openssl_pbkdf2 vulnerability by calling the function with an oversized key_length, leading to memory corruption detection and crash when run in an AddressSanitizer-enabled PHP build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `vulnerable_script.php` | Path to the PHP script containing the malicious openssl_pbkdf2 call | Yes |

## Examples

### Basic Usage

```bash
php vulnerable_script.php
```

### Advanced Usage

```bash
php -d memory_limit=512M vulnerable_script.php
```

## Expected Output

Runtime error from AddressSanitizer: "negative-size-param" in memcpy, followed by stack trace pointing to OpenSSL's PKCS5_PBKDF2_HMAC, and PHP process termination (e.g., "Aborted (core dumped)").

## Related

- [[Related Procedure|procedures/Trigger-Memory-Corruption-with-AddressSanitizer]]
