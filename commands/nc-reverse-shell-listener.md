---
id: cmd-nc-listener
data: nc -n -lvp 8888
tags:
  - reverse-shell
  - listener
type: command
output: |-
  Listening on [0.0.0.0] (family 0, port 8888)
  Connection from [target_ip] [port] received!
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.417Z'
verified: false
validated: true
submitted: true
---
# nc-reverse-shell-listener

## Command

```bash
nc -n -lvp 8888
```

## Description

Sets up a netcat listener in verbose mode to receive reverse shell connections from exploited targets like the Flink RCE, avoiding DNS lookups for speed and security.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Do not resolve DNS for hosts | Yes |
| `-l` | Listen mode for incoming connections | Yes |
| `-v` | Verbose output to show connection details | Yes |
| `-p 8888` | Specify port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -n -lvp 8888
```

### Advanced Usage

```bash
nc -n -lvp 4444 -s 0.0.0.0
```
(Add -s for source IP binding if needed.)

## Expected Output

Listener starts with 'Listening on [0.0.0.0] (family 0, port 8888)'. Upon connection: 'Connection from [target_ip] [port] received!' followed by interactive shell.

## Related

- [[Related Procedure: Setup-Netcat-Reverse-Shell-Listener]]
- [[Related Command: python-poc-execution]]
