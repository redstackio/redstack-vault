---
data: openssl genrsa -out server.key 2048
tags:
  - openssl
  - keygen
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.058Z'
id: e14d4786-ff7f-413b-87e2-26b93685eef5
verified: false
validated: true
submitted: true
---
# openssl-genrsa-server

## Command

```bash
openssl genrsa -out server.key 2048
```

## Description

Generates a 2048-bit RSA private key for the test server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-out server.key` | Output file for key | Yes |
| `2048` | Key size in bits | Yes |

## Examples

### Basic Usage

```bash
openssl genrsa -out server.key 2048
```

### Advanced Usage

```bash
openssl genrsa -out server.key 2048
```

## Expected Output

Private key file created.

## Related

- [[commands/openssl-req-server-csr]]
