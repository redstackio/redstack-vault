---
id: cmd-php-poc
name: php-poc
type: command
executor: bash
data: php PoC.php
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.760Z'
platforms:
  - PHP
tags:
  - poc
  - signature
verified: false
validated: true
submitted: true
---

# php-poc

## Command

```bash
php PoC.php
```

## Description

Executes the proof-of-concept PHP script using generated keys to create a base64-encoded sslsig that causes OpenSSL verification error in Vaultpress.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PoC.php | Script utilizing keys for signature | Yes |

## Examples

### Basic Usage

```bash
php PoC.php
```

## Expected Output

Base64-encoded sslsig string, e.g., "MEUCIQD...==", ready for POST request.

## Related

- [[commands/php-genkey1]]
- [[procedures/Generate-Malicious-Keys-and-Signature]]
