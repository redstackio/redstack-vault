---
data: openssl genrsa -out fake_ca.key 2048
tags:
  - openssl
  - keygen
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.080Z'
id: c7a33a5f-6445-46f2-9ba2-4858e4799f64
verified: false
validated: true
submitted: true
---
# openssl-genrsa-fake-ca

## Command

```bash
openssl genrsa -out fake_ca.key 2048
```

## Description

Generates a 2048-bit RSA private key for the fake CA used in spoofing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-out fake_ca.key` | Output file for key | Yes |
| `2048` | Key size in bits | Yes |

## Examples

### Basic Usage

```bash
openssl genrsa -out fake_ca.key 2048
```

### Advanced Usage

```bash
openssl genrsa -out fake_ca.key 2048 -3des
```

## Expected Output

Private key file created.

## Related

- [[commands/openssl-req-fake-ca]]
