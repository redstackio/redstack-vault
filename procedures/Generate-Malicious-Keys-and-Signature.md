---
id: proc-generate-malicious-keys
name: Generate-Malicious-Keys-and-Signature
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.794Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - key-generation
  - signature-bypass
  - openssl
commands:
  - '[[commands/php-genkey1]]'
  - '[[commands/php-genkey2]]'
  - '[[commands/php-poc]]'
platforms:
  - PHP
tools:
  - '[[tools/PHP-CLI]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---

# Generate-Malicious-Keys-and-Signature

## Summary

This procedure uses PHP scripts to generate mismatched RSA key pairs and a signature that triggers an OpenSSL verification error (-1 return), exploiting the loose PHP comparison in Vaultpress.

## Description

By creating keys of different types (e.g., one for signing, mismatched for verification), openssl_verify returns -1 on error, which PHP treats as true in if(-1). This prepares the sslsig payload for bypass.

## Requirements

1. PHP CLI installed with OpenSSL extension
2. Custom PHP scripts (genkey1.php, genkey2.php, PoC.php) for key and signature generation
3. Local execution environment

## Defense

Defensive measures and detection strategies:

- Patch Vaultpress to use strict comparison (=== 1) for openssl_verify
- Monitor for unusual OpenSSL errors in plugin logs
- Disable plugin if not needed

## Objectives

1. Produce keys causing verification mismatch
2. Generate base64 sslsig for POST payload
3. Enable unauthenticated API access

## Instructions

### Step 1: Generate First Key Pair

**Context**: Create the initial key type for signing.

**Command** ([[commands/php-genkey1]]):
```bash
php genkey1.php
```

> Generates RSA private/public key pair. Expected output: Key files saved locally.

### Step 2: Generate Mismatched Key Pair

**Context**: Create a second key type incompatible with verification.

**Command** ([[commands/php-genkey2]]):
```bash
php genkey2.php
```

> Produces mismatched keys. Expected output: Additional key files for PoC use.

### Step 3: Craft Signature Payload

**Context**: Use keys to sign data, creating error-inducing signature.

**Command** ([[commands/php-poc]]):
```bash
php PoC.php
```

> Combines keys to output base64 sslsig. Expected output: Encoded signature string.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[PowerShell]] Command and Scripting Interpreter (PHP)

### Sub-Techniques


## Commands Used

- [[commands/php-genkey1]]
- [[commands/php-genkey2]]
- [[commands/php-poc]]

## Tools Used

- [[tools/PHP-CLI]]

## Tags

- key-generation
- signature-bypass
- openssl
