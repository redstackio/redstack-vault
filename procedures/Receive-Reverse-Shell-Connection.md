---
id: proc-receive-reverse-shell
tags:
  - reverse-shell
  - command-execution
  - pivoting
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:32:48.421Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Receive-Reverse-Shell-Connection

## Summary

This procedure captures the incoming reverse shell from the Flink RCE exploitation using the netcat listener, allowing command execution and potential network pivoting on the server.

## Description

Post-PoC execution, the JavaScript gadget on the Flink server initiates a connection back to the listener, providing a shell. Use this for reconnaissance (e.g., ls, whoami) or pivoting. The shell is limited and crashes the instance after use. Prerequisites: Active netcat listener and successful RCE.

## Requirements

1. Active netcat listener on port 8888
2. Firewall allows inbound on 8888
3. Awareness of Flink server context (Java user, limited perms)

## Defense

Defensive measures and detection strategies:

- Block outbound connections from Flink to untrusted IPs/ports
- Monitor process creation on Flink nodes for shell spawns
- Use EDR to detect reverse shell patterns (e.g., nc invocations)

## Objectives

1. Receive and interact with reverse shell
2. Execute commands for pivoting/data exfil
3. Validate RCE success

## Instructions

### Step 1: Monitor Netcat for Connection

**Context**: Await and accept the incoming shell.

No new command; observe the running [[commands/nc-reverse-shell-listener]] for connection (e.g., 'Connection from [flink_ip] 12345 received!').

> Shell prompt appears; type commands like 'id' to test.

### Step 2: Execute Commands on Shell

**Context**: Use the shell for post-exploitation.

No command; in the netcat session, run bash commands (e.g., 'whoami', 'ls /', 'curl internal-resource').

> Output from target server; e.g., 'uid=1000(flink) gid=1000(flink)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/netcat]]

## Tags

- reverse-shell
- command-execution
- pivoting
