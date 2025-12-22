---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - backgrounding
  - evasion
  - command-injection
validated: true
---

# Bash-Nohup-Sleep-Background

## Code

```bash
nohup sleep 120 > /dev/null &
```

## Description

This bash snippet backgrounds a sleep command for 120 seconds (2 minutes) using nohup to make it immune to hangups, with output redirected to null for stealth. It serves as an example payload in command injection to test evasion of process timeouts, simulating a long-running operation without visible traces.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 120 | Sleep duration in seconds; replace with actual command for real use | 300 (5 minutes) |

## Usage

Inject this into a vulnerable command execution point, such as a web app's input field allowing shell commands. It starts the process detached, allowing the attacker to disconnect while it runs. Useful in red team exercises to establish persistence or run delayed payloads.

## Detection

- Monitor for nohup processes via `ps aux | grep nohup` or audit logs showing background jobs.
- Check for orphaned processes with unusual PIDs or sleep commands in process lists.
- Enable shell history logging and process creation events (e.g., via Sysmon on Linux equivalents) to detect injection patterns.

## Related

- [[procedures/Background-Long-Running-Commands]]
- [[commands/bash-nohup-background-sleep]]
