---
tags:
  - privilege-escalation
  - rce
  - ssh-shell
type: procedure
tools:
  - '[[tools/openssh-client]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/ssh-execute-arbitrary]]'
verified: false
platforms:
  - Embedded Linux
  - Network Device
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:35.659Z'
sub_techniques: []
id: 6a527dc8-fa04-4cc9-b95d-80ca8503d6fe
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-Arbitrary-Shell-Commands-via-SSH-for-Root-Escalation

## Summary

This procedure exploits the lack of restrictions in the SSH interface of Ubiquiti EdgeSwitch X v1.1.0 and prior to execute arbitrary shell commands, bypassing CLI limits and escalating from privilege-0 to root for full administrative control.

## Description

The vulnerability stems from the SSH daemon permitting direct shell command execution without enforcing CLI privilege checks, allowing authenticated users to run system-level commands. In an Embedded Linux environment, this leads to root escalation via commands that exploit misconfigurations or directly invoke elevated shells. The attack scenario involves remote command injection post-authentication, resulting in outcomes like accessing restricted files or modifying configurations.

## Requirements

1. Authenticated SSH session as privilege-0 user
2. Knowledge of target IP and shell paths (e.g., /bin/sh)
3. SSH client with command execution capability

## Defense

Defensive measures and detection strategies:

- Patch to v1.1.1 or later firmware to restrict SSH to CLI-only
- Implement privilege separation and input sanitization in SSH handling
- Monitor SSH logs for anomalous command executions (e.g., shell invocations)
- Use IDS to detect unusual shell activity on management interfaces

## Objectives

1. Bypass CLI restrictions via SSH shell access
2. Escalate privileges to root
3. Achieve full device control, including config changes

## Instructions

### Step 1: Inject Shell Command

**Context**: From an authenticated session or directly via SSH, invoke a shell to run arbitrary commands, bypassing the restricted CLI.

**Command** ([[commands/ssh-execute-arbitrary]]):
```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "id"'
```

> This executes the 'id' command in a shell context. Expected output: "uid=0(root) gid=0(root)" if escalation succeeds, confirming root access. If limited, it may show privilege-0 uid.

### Step 2: Escalate and Verify Root Access

**Context**: Chain to a root-enabling command, such as spawning a root shell or exploiting a local escalation vector.

**Command** ([[commands/ssh-root-shell]]):
```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "sudo -i"'
```

> Assuming sudo misconfig allows it, this drops to root shell. Expected output: Root prompt or successful command execution (e.g., "#" prompt). Validate by running "whoami" showing "root".

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Unix Shell]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/ssh-execute-arbitrary]]
- [[commands/ssh-root-shell]]

## Tools Used

- [[tools/openssh-client]]

## Tags

- privilege-escalation
- rce
- ssh-shell
