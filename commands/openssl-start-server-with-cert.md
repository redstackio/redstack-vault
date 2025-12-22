---
type: command
executor: bash
data: openssl s_server -quiet -key key.pem -cert cert.pem -port $_PORT
output: null
platforms:
  - Linux
tags:
  - openssl
  - server
  - ssl
verified: true
validated: true
---

# openssl-start-server-with-cert

## Command

```bash
openssl s_server -quiet -key key.pem -cert cert.pem -port $_PORT
```

## Description

Starts an SSL/TLS server listener using a private key and certificate, forwarding connected client I/O (e.g., for reverse shells) over an encrypted channel.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -quiet | Suppress non-error output | No |
| -key key.pem | Path to private key file | Yes |
| -cert cert.pem | Path to certificate file | Yes |
| -port $_PORT | Listening port (e.g., 4242) | Yes |

## Examples

### Basic Usage

```bash
openssl s_server -quiet -key key.pem -cert cert.pem -port 4242
```

Listens on port 4242.

### Advanced Usage

```bash
openssl s_server -quiet -key key.pem -cert cert.pem -port 4242 -www
```

Adds HTTP-like responses for testing.

## Expected Output

Server starts with minimal output; on connection:

```
Using default temp DH parameters
SSL handshake has read 1563 bytes and written 433 bytes
Verification: OK
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
(... shell I/O ...)
```

Interactive shell appears upon client connect.

## Related

- [[commands/openssl-generate-self-signed-cert]]
- [[procedures/openssl-reverse-shell]]
