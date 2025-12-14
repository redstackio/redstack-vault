---
data: >-
  openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername
  hostA.example.com -sess_in session_A.pem -sess_out resumed_B.pem
tags:
  - tls-resumption
  - session
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.096Z'
id: 5e3ec0ad-6aa4-4d0b-bcf6-034f62ae48d5
verified: false
validated: true
submitted: true
---
# openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem -sess_out resumed_B.pem

## Command

```bash
openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem -sess_out resumed_B.pem
```

## Description

Resumes a TLS 1.3 session using a saved ticket to bypass authentication on a different virtual host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-connect` | Shared IP and port | Yes |
| `-tls1_3` | Force TLS 1.3 | Yes |
| `-servername` | SNI for host A | Yes |
| `-sess_in` | Input session file | Yes |
| `-sess_out` | Output resumed session | No |

## Examples

### Basic Usage

```bash
openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem
```

### Advanced Usage

```bash
openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem -quiet
```

## Expected Output

Abbreviated handshake output with "Reused, TLSv1.3" and no certificate prompt.

## Related

- [[Related Procedure]]
