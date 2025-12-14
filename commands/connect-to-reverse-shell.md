---
data: nc 127.0.0.1 8080
tags:
  - shell-access
  - netcat
type: command
output: Interactive root shell session
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.997Z'
id: 5e6d919f-e025-4365-a1fc-1b353f6bc031
verified: false
validated: true
submitted: true
---
# connect-to-reverse-shell

## Command

```bash
nc 127.0.0.1 8080
```

## Description

Connects to a netcat listener on localhost port 8080 to interact with a reverse bash shell, typically used post-exploitation to access elevated privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `127.0.0.1` | Target IP (localhost) | Yes |
| `8080` | Port to connect to | Yes |

## Examples

### Basic Usage

```bash
nc 127.0.0.1 8080
```

### Advanced Usage

Timeout: `nc -w 10 127.0.0.1 8080`

## Expected Output

Interactive shell prompt; commands like `id` show root privileges.

## Related

- [[commands/create-reverse-shell-script]]
- [[procedures/Access-Root-Shell]]
