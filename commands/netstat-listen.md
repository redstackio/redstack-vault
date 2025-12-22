---
id: cmd-netstat-7440
data: 'netstat -ano | findstr :7440'
tags:
  - recon
  - network
type: command
output: 'TCP    127.0.0.1:7440           0.0.0.0:0              LISTENING       1234'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.555Z'
verified: false
validated: true
submitted: true
---
# netstat-listen

## Command

```cmd
netstat -ano | findstr :7440
```

## Description

Lists network connections and listening ports, filtering for port 7440 to identify the EvoStream service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ano | Displays PID and details | Yes |
| findstr :7440 | Filters for port 7440 | Yes |

## Examples

### Basic Usage

```cmd
netstat -ano | findstr :7440
```

### Advanced Usage

```cmd
netstat -ano | findstr :7440 > ports.txt
```

## Expected Output

TCP    127.0.0.1:7440           0.0.0.0:0              LISTENING       1234 (evostream PID)

## Related

- [[Related Procedure]]
