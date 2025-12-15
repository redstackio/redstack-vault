---
tags:
  - privilege-escalation
  - sudo
  - steam-deck
  - linux
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/sudo-elevate]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:23:36.543Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1e8c48f7-2b38-43f2-bfb2-cacab3b67e2a
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Steam-Deck-Privilege-Escalation-via-Bashrc-Modification

## Summary

This procedure chains from user-level RCE to root access on Steam Deck by modifying user-executable files like ~/.bashrc to bypass the 'no new privileges' flag in steamwebhelper, then leveraging the 'deck' user's passwordless sudo configuration for persistent elevation.

## Description

The steamwebhelper process sets the 'no new privileges' flag, preventing direct sudo calls from RCE. However, the 'deck' user has NOPASSWD sudo access. By injecting code into ~/.bashrc (executed outside the flagged process, e.g., on login/reboot), the attacker plants a payload that runs sudo without restrictions, granting a root shell. This achieves persistence and full system control, accessing all files and hardware.

## Requirements

1. Initial RCE as 'deck' user
2. Write access to user's home directory
3. Target with sudoers config allowing NOPASSWD for 'deck'
4. Trigger mechanism like reboot or shell invocation

## Defense

Defensive measures and detection strategies:

- Remove NOPASSWD from sudoers for 'deck' user
- Monitor file modifications in ~/.bashrc and similar
- Enable PR_SET_NO_NEW_PRIVS auditing
- Use immutable file attributes on critical configs

## Objectives

1. Bypass execution flags for privilege escalation
2. Gain root shell for persistence
3. Access system-wide resources

## Instructions

### Step 1: Inject Payload into Bashrc

**Context**: From RCE shell, modify ~/.bashrc to include malicious code executed on next shell start.

Append sudo elevation script:

```bash
echo 'sudo -i' >> ~/.bashrc
```

> This adds a line to run sudo on bash invocation. Expected output: File updated, no errors.

### Step 2: Trigger Execution

**Context**: Force execution outside steamwebhelper, e.g., by simulating logout or reboot.

From RCE, trigger a new shell or wait for reboot:

```bash
reboot
```

> Device restarts, loading modified bashrc. Expected output: New shell session starts.

### Step 3: Elevate to Root

**Context**: Use the injected command to call sudo.

Execute [[commands/sudo-elevate]]:

```bash
sudo -i
```

> Leverages NOPASSWD for root shell. Expected output: # prompt indicating root access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/sudo-elevate]]

## Tools Used


## Tags

- privilege-escalation
- sudo
- bashrc
