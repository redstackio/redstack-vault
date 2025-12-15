---
tags:
  - authentication
  - ssh
  - ubiquiti
type: procedure
tools:
  - '[[tools/openssh-client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ssh-authenticate]]'
verified: false
platforms:
  - Embedded Linux
  - Network Device
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.663Z'
sub_techniques: []
id: 32c664dc-33f8-4cd0-9da5-7d462ea1a446
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Privilege-0-User-on-Ubiquiti-EdgeSwitch

## Summary

This procedure establishes an authenticated SSH session to a Ubiquiti EdgeSwitch X device using privilege-0 credentials, setting the stage for further exploitation of the SSH interface.

## Description

In the context of the Ubiquiti EdgeSwitch vulnerability, privilege-0 users have limited CLI access, but the SSH interface allows bypassing these restrictions. This procedure focuses on initial authentication, which is a prerequisite for executing arbitrary commands. The target environment is an Embedded Linux-based network device running v1.1.0 or prior firmware. Successful authentication provides a foothold for privilege escalation.

## Requirements

1. Valid privilege-0 username and password for the EdgeSwitch
2. Network access to the device's SSH port (default 22)
3. SSH client installed on the attacker's machine

## Defense

Defensive measures and detection strategies:

- Enforce strong privilege-0 passwords and monitor failed login attempts
- Disable SSH access for low-privilege users or restrict to CLI-only mode
- Use network segmentation to limit management interface exposure
- Log and alert on SSH connections from unauthorized IPs

## Objectives

1. Gain authenticated access to the SSH interface
2. Verify privilege level as privilege-0
3. Prepare for command injection without triggering restrictions

## Instructions

### Step 1: Connect via SSH

**Context**: Initiate an SSH connection to the target device using privilege-0 credentials to establish a session.

**Command** ([[commands/ssh-authenticate]]):
```bash
ssh privilege0_user@192.168.1.1
```

> This command prompts for the password. Upon success, you enter the device's CLI or shell prompt. Expected output includes a login banner and user prompt like "EdgeSwitch>". If authentication fails, check credentials and network connectivity.

### Step 2: Verify Access Level

**Context**: Confirm the session is limited to privilege-0 by attempting a basic command.

**Command** ([[commands/ssh-execute-basic]]):
```bash
ssh privilege0_user@192.168.1.1 'show version'
```

> This runs a safe CLI command to verify access. Expected output shows device version and confirms privilege-0 limitations (e.g., no access to sensitive configs).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/ssh-authenticate]]
- [[commands/ssh-execute-basic]]

## Tools Used

- [[tools/openssh-client]]

## Tags

- authentication
- ssh
- privilege-0
