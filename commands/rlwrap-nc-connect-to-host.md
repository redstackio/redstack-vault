---
id: f1877b31-e28c-48d6-8f02-243b98c33920
name: rlwrap-nc-connect-to-host
type: command
executor: bash
data: rlwrap nc -nlvp $_PORT
output: null
created_at: '2023-04-06T03:56:24.983284+00:00'
updated_at: '2023-04-10T20:25:31.247390+00:00'
platforms:
  - Linux
tags:
  - netcat
  - listener
  - reverse-shell
verified: true
validated: true
---

# rlwrap-nc-connect-to-host

## Command

```bash
rlwrap nc -nlvp $_PORT
```

## Description

Sets up a netcat listener with rlwrap for interactive reverse shell handling, specifying a port for incoming connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rlwrap | Adds readline support | Yes |
| nc | Netcat tool | Yes |
| -n | No DNS resolution | Built-in |
| -l | Listen mode | Yes |
| -v | Verbose output | Yes |
| -p | Specify port | Yes |
| $_PORT | Listening port (e.g., 4242) | Yes |

## Examples

### Basic Listener on Port 4242

```bash
rlwrap nc -nlvp 4242
```

### With Specific Host Binding

```bash
rlwrap nc -nlvp 0.0.0.0 4242
```

## Expected Output

listening on [any] 4242 ...
connect to [$_HOST] from (target-ip) [$_PORT] by ($_PROTO) [pid]

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
- [[commands/rlwrap-nc-with-history-completion]]
