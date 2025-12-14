---
data: 'openssl s_client -connect 50.30.33.235:587 -cipher aNULL'
tags:
  - ssl-test
  - mitm
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.044Z'
id: d4727b11-e703-4bb5-9db8-a49edca7efc6
verified: false
validated: true
submitted: true
---
# openssl-anonymous-connect-port587

## Command

```bash
openssl s_client -connect 50.30.33.235:587 -cipher aNULL
```

## Description

Tests anonymous cipher acceptance on SMTP submission port with STARTTLS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -connect | IP:port | Yes |
| -cipher | aNULL | Yes |

## Examples

### Basic Usage

```bash
openssl s_client -connect ip:587 -cipher aNULL
```

### Advanced Usage

```bash
openssl s_client -connect ip:587 -cipher aNULL -starttls smtp
```

## Expected Output

Handshake success with anonymous cipher if vulnerable; error otherwise.

## Related

- [[commands/openssl-anonymous-connect-port465]]
- [[procedures/Test-Anonymous-Cipher-Handshake-with-OpenSSL]]
