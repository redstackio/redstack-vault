---
data: 'openssl s_client -connect apps.owncloud.com:465 -cipher aNULL'
tags:
  - ssl-test
  - mitm
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.048Z'
id: 2c44e597-f7de-4ab7-b97f-7b43457176f8
verified: false
validated: true
submitted: true
---
# openssl-anonymous-connect-port465

## Command

```bash
openssl s_client -connect apps.owncloud.com:465 -cipher aNULL
```

## Description

Attempts SSL/TLS connection to SMTPS port using only anonymous ciphers to test for unauthenticated handshakes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -connect | Host:port to connect | Yes |
| -cipher | Cipher list (aNULL for anonymous) | Yes |

## Examples

### Basic Usage

```bash
openssl s_client -connect target.com:465 -cipher aNULL
```

### Advanced Usage

```bash
openssl s_client -connect target.com:465 -cipher aNULL -debug
```

## Expected Output

Successful: "CONNECTED", no cert, "Cipher is AECDH-AES256-SHA", ESMTP banner; failure: handshake error.

## Related

- [[commands/openssl-anonymous-connect-port587]]
- [[procedures/Test-Anonymous-Cipher-Handshake-with-OpenSSL]]
