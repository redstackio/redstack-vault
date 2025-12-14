---
id: cmd-nc-listener
data: nc -vlp ATTACKER_PORT
tags:
  - reverse-shell
  - listener
type: command
output: |-
  Listening on [0.0.0.0] (family 0, port ATTACKER_PORT)
  Connection from [target_ip] ATTACKER_PORT received!
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.732Z'
verified: false
validated: true
submitted: true
---
---
# netcat-listener

## Command

```bash
nc -vlp ATTACKER_PORT
```

## Description

Sets up a netcat listener to receive incoming reverse shell connections from exploited environments like the LGTM container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `-v` | Verbose output | Yes |
| `-p ATTACKER_PORT` | Port to listen on (e.g., 4444) | Yes |

## Examples

### Basic Usage

```bash
nc -vlp 4444
```

### Advanced Usage

```bash
nc -vlp 4444 -k  # Keep open after connection
```

## Expected Output

Verbose listening message followed by connection details and shell prompt upon successful reverse shell.

## Related

- [[commands/ssh-remote-forward]]
- [[procedures/Set-Up-Netcat-Listener]]

---
