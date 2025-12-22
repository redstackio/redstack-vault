---
data: openssl genrsa -out legit_ca.key 2048
tags:
  - openssl
  - keygen
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.097Z'
id: d42a2a6e-66c5-4208-ae3e-18e7263b7c5c
verified: false
validated: true
submitted: true
---
# openssl-genrsa-legit-ca

## Command

```bash
openssl genrsa -out legit_ca.key 2048
```

## Description

Generates a 2048-bit RSA private key for the legitimate CA.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-out legit_ca.key` | Output file for key | Yes |
| `2048` | Key size in bits | Yes |

## Examples

### Basic Usage

```bash
openssl genrsa -out legit_ca.key 2048
```

### Advanced Usage

```bash
openssl genrsa -out legit_ca.key 4096 -aes256
```

## Expected Output

Private key file created; PEM-encoded RSA key.

## Related

- [[commands/openssl-req-legit-ca]]
