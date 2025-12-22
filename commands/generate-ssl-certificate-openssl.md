---
id: 89c73a99-5700-4058-b92c-868883111c66
name: generate-ssl-certificate-openssl
type: command
executor: bash
data: >-
  openssl req -subj '/CN=$_TARGET_DOMAIN' -batch -new -x509 -days 365 -nodes
  -out server.pem -keyout server.pem
output: null
created_at: '2023-04-06T03:56:22.335940+00:00'
updated_at: '2023-04-10T20:25:09.843906+00:00'
platforms:
  - Linux
tags:
  - ssl
  - certificate-generation
verified: true
validated: true
---

# generate-ssl-certificate-openssl

## Command

```bash
openssl req -subj '/CN=$_TARGET_DOMAIN' -batch -new -x509 -days 365 -nodes -out server.pem -keyout server.pem
```

## Description

Generates a self-signed SSL/TLS certificate and private key for use in MITM attacks. The certificate's Common Name matches the target domain, allowing impersonation during handshakes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | Domain to set as CN (e.g., example.com) | Yes |
| -days 365 | Certificate validity in days | No (default 30) |
| -nodes | No DES encryption (no passphrase) | Built-in |
| server.pem | Output file for cert and key | Built-in |

## Examples

### Basic Usage

```bash
openssl req -subj '/CN=example.com' -batch -new -x509 -days 365 -nodes -out server.pem -keyout server.pem
```

## Expected Output

```
Generating a 2048 bit RSA private key
...+++
...+++
writing new private key to 'server.pem'
-----
Signature ok
subject=/CN=example.com
Getting CA Private Key
```
Files server.pem (cert) and server.pem (key, overwritten) are created.

## Related

- [[procedures/SSL-MITM-Network-Discovery-with-OpenSSL]]
- [[tools/openssl]]
