---
data: 'openssl s_client -connect localhost:443'
tags:
  - trigger
  - tls
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.478Z'
id: d4362f31-03a9-4d2e-b3aa-97a7c003097b
verified: false
validated: true
submitted: true
---
# trigger-openssl-tls

## Command

```cmd
openssl s_client -connect localhost:443
```

## Description

Initiates a TLS connection using OpenSSL, triggering config load and potential malicious engine execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| s_client | SSL/TLS client | Yes |
| -connect | Host:port | Yes |

## Examples

### Basic Usage

```cmd
openssl s_client -connect localhost:443
```

### Advanced Usage

```cmd
openssl s_client -connect example.com:443 -quiet
```

## Expected Output

TLS handshake details; payload executes silently if injected.

## Related

- [[Related Procedure]]
