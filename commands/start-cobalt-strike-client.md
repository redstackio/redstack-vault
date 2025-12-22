---
type: command
executor: bash
data: ./cobaltstrike
output: null
created_at: '2023-04-06T03:56:16.220810+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - c2
  - cobalt-strike
  - execution
verified: true
validated: true
---

# start-cobalt-strike-client

## Command

```bash
./cobaltstrike
```

## Description

Launches the Cobalt Strike client GUI, prompting for connection to a team server to manage beacons and operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Interactive launch | Yes |

## Examples

### Basic Usage

```bash
./cobaltstrike
```

## Expected Output

Cobalt Strike Client v4.X.X
Enter Team Server: <IP:port> <user> <pass>
(Connects and opens GUI)

## Related

- [[commands/start-cobalt-strike-teamserver]]
- [[procedures/Cobalt-Strike-Team-Server-Installation-and-Execution]]
