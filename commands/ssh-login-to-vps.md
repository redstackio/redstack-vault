---
id: ssh-login-001
data: ssh ████
tags:
  - ssh
  - access
type: command
output: Interactive shell on VPS
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.291Z'
verified: false
validated: true
submitted: true
---
# SSH Login to VPS

## Command

```bash
ssh ████
```

## Description

Initiates a secure shell session to a remote VPS instance, redacted as ████ for the hostname/IP. Used to prepare external listener environments in exploit chains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ████ | VPS hostname or IP (redacted) | Yes |

## Examples

### Basic Usage

```bash
ssh user@192.168.1.100
```

### Advanced Usage

```bash
ssh -i key.pem user@████ -p 22
```

## Expected Output

Interactive shell prompt on the VPS, e.g., "user@vps:~$". Errors if auth fails.

## Related

- [[Related Procedure: Setup-VPS-Listener-for-Reverse-Shell]]
