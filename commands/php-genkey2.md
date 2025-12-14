---
id: cmd-php-genkey2
name: php-genkey2
type: command
executor: bash
data: php genkey2.php
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.770Z'
platforms:
  - PHP
tags:
  - key-generation
verified: false
validated: true
submitted: true
---

# php-genkey2

## Command

```bash
php genkey2.php
```

## Description

Runs a PHP script to generate a second, mismatched key type for signature creation, ensuring openssl_verify fails with -1.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| genkey2.php | Script for mismatched key | Yes |

## Examples

### Basic Usage

```bash
php genkey2.php
```

## Expected Output

Mismatched key files (e.g., key2.pem) output for PoC integration.

## Related

- [[commands/php-genkey1]]
- [[procedures/Generate-Malicious-Keys-and-Signature]]
