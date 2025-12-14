---
data: >-
  openssl x509 -req -in server.csr -CA legit_ca.crt -CAkey legit_ca.key
  -CAcreateserial -out server.crt -days 365 -sha256
tags:
  - openssl
  - sign-cert
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.052Z'
id: abf272a1-2609-42f5-9b15-73336fd8faf9
verified: false
validated: true
submitted: true
---
# openssl-x509-sign-server

## Command

```bash
openssl x509 -req -in server.csr -CA legit_ca.crt -CAkey legit_ca.key -CAcreateserial -out server.crt -days 365 -sha256
```

## Description

Signs the server CSR with the legitimate CA to produce a trusted server certificate.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-req` | Sign from CSR | Yes |
| `-in server.csr` | Input CSR | Yes |
| `-CA legit_ca.crt` | CA certificate | Yes |
| `-CAkey legit_ca.key` | CA private key | Yes |
| `-CAcreateserial` | Create serial file | Yes |
| `-out server.crt` | Output signed cert | Yes |
| `-days 365` | Validity | Yes |
| `-sha256` | Hash algorithm | Yes |

## Examples

### Basic Usage

```bash
openssl x509 -req -in server.csr -CA legit_ca.crt -CAkey legit_ca.key -CAcreateserial -out server.crt -days 365 -sha256
```

### Advanced Usage

```bash
openssl x509 -req -in server.csr -CA legit_ca.crt -CAkey legit_ca.key -CAcreateserial -out server.crt -days 730 -sha256 -extensions v3_req
```

## Expected Output

Server certificate file created, signed by CA.

## Related

- [[commands/openssl-req-server-csr]]
