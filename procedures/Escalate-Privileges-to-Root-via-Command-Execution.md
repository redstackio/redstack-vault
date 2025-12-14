---
tags:
  - privilege-escalation
  - root-access
  - sudo
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Embedded Network Switch
  - Linux
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f88ec1d7-a736-441f-8e12-cd41b5552220
created_at: '2025-12-14T17:29:44.354Z'
updated_at: '2025-12-14T17:29:44.354Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Escalate-Privileges-to-Root-via-Command-Execution

## Summary

This procedure uses the established command injection to execute privilege-escalating commands, transitioning from operator (Privilege-1) to full administrator/root (Privilege-15) access on the EdgeSwitch device.

## Description

Once command injection is achieved, the attacker can run escalation payloads like spawning a root shell or modifying privilege configurations. The embedded Linux environment allows standard Unix commands for escalation, such as `sudo` if configured permissively or direct root command execution via the CGI's elevated context. This grants control over network settings, firmware, and connected infrastructure. Requires prior injection success.

## Requirements

1. Confirmed command injection capability
2. Knowledge of device-specific escalation paths (e.g., sudoers or setuid binaries)
3. Active session to chain injections

## Defense

Defensive measures and detection strategies:

- Apply least privilege to CGI processes; run as non-root user
- Enable privilege escalation logging and auditing on the device
- Regularly review and harden sudo configurations; use SELinux or AppArmor if supported

## Objectives

1. Execute commands with root privileges
2. Gain Privilege-15 access in the GUI
3. Maintain persistence or further compromise

## Instructions

### Step 1: Inject Escalation Command

**Context**: Use the CGI injection to run a privilege-escalating payload.

Craft a request appending `; sudo -i` or `; /bin/sh` to gain a shell.

> The CGI executes this as root, providing shell access or output confirming escalation.

### Step 2: Verify Root Access

**Context**: Test escalated privileges with root-only commands.

Inject `; whoami` or attempt admin GUI actions post-escalation.

> Output should show `root`; GUI may now allow Privilege-15 operations.

### Step 3: Leverage Access

**Context**: Perform admin tasks to solidify control.

Inject commands to add backdoor users or extract configs.

> Successful: Device configurations modifiable; full control achieved.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[root-access]]
- [[Sudo]]
