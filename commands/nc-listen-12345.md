---
id: cmd-uuid-004
name: nc-listen-12345
type: command
executor: bash
data: nc -llvp 12345
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.854Z'
platforms:
  - Linux
tags:
  - netcat
  - listener
verified: false
validated: true
submitted: true
---

# nc-listen-12345

## Command

```bash
nc -llvp 12345
```

## Description

Starts a verbose TCP listener on port 12345 using netcat to capture SSRF connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `-lv` | Verbose output | Yes |
| `-p 12345` | Port to bind | Yes |

## Examples

### Basic Usage

```bash
nc -llvp 12345
```

### Advanced Usage

Listen on specific interface:
```bash
nc -llvp 127.0.0.1 12345
```

## Expected Output

"Listening on [0.0.0.0] (family 0, port 12345)" followed by connection details on hit.

## Related

- [[commands/apt-install-netcat]]
- [[procedures/Start-Netcat-Listener-in-Container]]
