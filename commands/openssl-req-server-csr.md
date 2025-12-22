---
data: openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
tags:
  - openssl
  - csr
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.055Z'
id: d8399d73-16b7-40c3-89b7-344a045ec2eb
verified: false
validated: true
submitted: true
---
# openssl-req-server-csr

## Command

```bash
openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
```

## Description

Generates a certificate signing request (CSR) for the server using its private key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-new` | New request | Yes |
| `-key server.key` | Input private key | Yes |
| `-out server.csr` | Output CSR file | Yes |
| `-subj "/CN=localhost"` | Subject name | Yes |

## Examples

### Basic Usage

```bash
openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
```

### Advanced Usage

```bash
openssl req -new -key server.key -out server.csr -subj "/CN=localhost/O=Test"
```

## Expected Output

CSR file created in PEM format.

## Related

- [[commands/openssl-x509-sign-server]]
