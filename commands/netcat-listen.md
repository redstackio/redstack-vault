---
data: nc -lvnp 80
tags:
  - network
  - listen
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: b27557d8-bb5e-433a-897d-ba036270093d
created_at: '2025-12-13T09:01:17.262Z'
updated_at: '2025-12-13T09:01:17.262Z'
verified: false
validated: true
submitted: true
---
# Netcat Listen

## Command

```bash
nc -lvnp 80
```

## Description
Listens on a port for incoming connections, useful for capturing exfiltrated data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `-v` | Verbose | No |
| `-n` | No DNS | No |
| `-p` | Port | Yes |

## Examples

### Basic Usage

```bash
nc -lvnp 80
```

## Expected Output
Incoming connection data displayed.

## Related
- [[procedures/Exploit-for-Cache-Poisoning-or-Bypass]]
