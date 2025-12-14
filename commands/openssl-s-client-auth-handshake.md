---
data: >-
  openssl s_client -connect hostA.example.com:443 -cert client.crt -key
  client.key -tls1_3 -servername hostA.example.com
tags:
  - tls
  - handshake
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.100Z'
id: c64f4716-6da4-427a-88d6-104b8265fd14
verified: false
validated: true
submitted: true
---
# openssl s_client -connect hostA.example.com:443 -cert client.crt -key client.key -tls1_3 -servername hostA.example.com

## Command

```bash
openssl s_client -connect hostA.example.com:443 -cert client.crt -key client.key -tls1_3 -servername hostA.example.com
```

## Description

Performs a full TLS 1.3 handshake with client certificate authentication to establish a session with NGINX virtual host A.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-connect` | Target host and port | Yes |
| `-cert` | Client certificate file | Yes |
| `-key` | Client private key file | Yes |
| `-tls1_3` | Force TLS 1.3 | Yes |
| `-servername` | SNI value | Yes |

## Examples

### Basic Usage

```bash
openssl s_client -connect hostA.example.com:443 -cert client.crt -key client.key -tls1_3 -servername hostA.example.com
```

### Advanced Usage

```bash
openssl s_client -connect hostA.example.com:443 -cert client.crt -key client.key -tls1_3 -servername hostA.example.com -sess_out session.pem
```

## Expected Output

TLS handshake details, including certificate chain, session ticket, and "Verify return code: 0 (ok)".

## Related

- [[Related Procedure]]
