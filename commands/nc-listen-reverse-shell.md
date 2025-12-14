---
id: cmd-nc-listen-001
data: nc -nvlp 1337
tags:
  - listener
  - reverse-shell
  - nc
type: command
output: |-
  Listening on [0.0.0.0] (family 0, port 1337)
  Connection from target_ip port xxxx received!
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.257Z'
verified: false
validated: true
submitted: true
---
# nc-listen-reverse-shell

## Command

```bash
nc -nvlp 1337
```

## Description

Netcat command to listen on port 1337 for incoming reverse shell connections, with verbose output and no DNS resolution. Used to receive shells from exploited targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No DNS resolution | Yes |
| -v | Verbose output | Yes |
| -l | Listen mode | Yes |
| -p | Port to bind (1337) | Yes |

## Examples

### Basic Usage

```bash
nc -nvlp 1337
```

### Advanced Usage

Different port:
```bash
nc -nvlp 4444
```

## Expected Output

Listening confirmation, then connection details and shell prompt upon receipt.

## Related

- [[Related Procedure|procedures/Set-Up-Netcat-Listener-for-Reverse-Shell]]
