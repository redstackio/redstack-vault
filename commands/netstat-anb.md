---
data: netstat -anb
tags:
  - network
  - discovery
type: command
executor: bash
platforms:
  - Windows
id: 6798d0d3-8fef-4eab-a27b-ec57084b14c7
created_at: '2025-12-11T03:47:56.470Z'
updated_at: '2025-12-11T03:47:56.470Z'
verified: false
validated: true
submitted: true
---
# netstat-anb

## Command

```bash
netstat -anb
```

## Description

Displays active network connections, listening ports, and the executables associated with them, used to identify the WebSocket server on port 1235.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Display all connections and listening ports | Yes |
| `-n` | Display addresses and port numbers in numerical form | Yes |
| `-b` | Display the executable involved in creating each connection or listening port | Yes |

## Examples

### Basic Usage

```bash
netstat -anb
```

### Advanced Usage

```bash
netstat -anb | findstr :1235
```

## Expected Output

List of connections including the WebSocket server at localhost:1235 bound to psnowlauncher.exe.

## Related

- [[procedures/Launch-PlayStation-Now-Application]]
- #netstat
