---
data: nc -nlvp 1234
tags:
  - listener
  - reverse-shell
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: 21a04e9b-9b1f-4308-b960-0ff1c9cee730
created_at: '2025-12-14T17:24:08.438Z'
updated_at: '2025-12-14T17:24:08.438Z'
verified: false
validated: true
submitted: true
---
# nc-tcp-listener

## Command

```bash
nc -nlvp 1234
```

## Description

This netcat command sets up a TCP listener on port 1234 in non-forking, no-DNS, verbose mode, waiting for incoming connections like those from a reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Avoids DNS lookups for faster operation | Yes |
| `-l` | Listen mode for incoming connections | Yes |
| `-v` | Enables verbose output for connection details | Yes |
| `-p` | Specifies the local port (1234) | Yes |

## Examples

### Basic Usage

```bash
nc -nlvp 4444
```

### Advanced Usage

```bash
nc -nlvp 1234 -s 0.0.0.0
```

## Expected Output

Displays 'listening on [any] 1234 ...' and waits. Upon connection, shows remote IP/port and provides an interactive shell prompt for command input/output.

## Related

- [[commands/msfvenom-php-reverse-shell]]
- [[procedures/Setup-Reverse-Shell-Listener]]
