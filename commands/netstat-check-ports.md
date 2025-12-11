---
data: netstat -anb
tags:
  - discovery
type: command
executor: cmd
platforms:
  - Windows
id: 68e844fe-0e9f-4d50-8340-548fe21b815c
created_at: '2025-12-11T06:10:30.651Z'
updated_at: '2025-12-11T06:10:30.651Z'
verified: false
validated: true
submitted: true
---
# netstat-check-ports

## Command

```cmd
netstat -anb
```

## Description

Checks active network connections and listening ports, including the process names associated with them. Useful for discovering local servers like the PlayStation Now WebSocket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Displays all connections and listening ports | Yes |
| `-n` | Displays addresses and port numbers in numerical form | Yes |
| `-b` | Displays the executable involved in creating each connection or listening port | Yes |

## Examples

### Basic Usage

```cmd
netstat -anb
```

## Expected Output

A list of active connections, e.g., TCP 127.0.0.1:1235 LISTENING [psnowlauncher.exe]

## Related
- [[procedures/Discover-Local-WebSocket-Server]]
