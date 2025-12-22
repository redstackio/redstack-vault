---
data: nc -lvp 8080
tags:
  - listener
  - reverse-shell
type: command
output: 'Listening on [0.0.0.0] (family 0, port 8080)'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.360Z'
id: ce0697af-6927-4d0c-867a-042618312b09
verified: false
validated: true
submitted: true
---
# netcat-listen-8080

## Command

```bash
nc -lvp 8080
```

## Description

Starts a netcat listener on port 8080 to receive the reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| -v | Verbose | Yes |
| -p 8080 | Port | Yes |

## Examples

### Basic Usage

```bash
nc -lvp 8080
```

## Expected Output

Listening confirmation, then incoming connection.

## Related

- [[tools/netcat]]
