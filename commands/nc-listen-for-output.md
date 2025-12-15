---
id: cmd-nc-listen
name: nc-listen-for-output
type: command
executor: bash
data: nc -vlkp 11211
output: Ping messages from GitLab Redis
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.289Z'
platforms:
  - Linux
tags:
  - nc
  - listener
  - verification
verified: false
validated: true
submitted: true
---

# nc-listen-for-output

## Command

```bash
nc -vlkp 11211
```

## Description

Listens on port 11211 for TCP connections to capture Redis pings or RCE output pipes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Verbose | No |
| -l | Listen mode | Yes |
| -k | Keep open after connection | No |
| -p 11211 | Port | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Incoming data streams from target, e.g., replication pings or command results.

## Related

- [[procedures/Verify-Exploitation-and-Capture-Output]]
