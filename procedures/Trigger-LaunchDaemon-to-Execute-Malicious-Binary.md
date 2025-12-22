---
id: proc-trigger-acronis-daemon-001
name: Trigger-LaunchDaemon-to-Execute-Malicious-Binary
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.033Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - macos
  - privilege-escalation
  - launchdaemons
commands: []
platforms:
  - macOS
tools: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---

# Trigger-LaunchDaemon-to-Execute-Malicious-Binary

## Summary

This procedure triggers an Acronis LaunchDaemon to execute the replaced malicious binary as root, resulting in privilege escalation to a root shell.

## Description

Following binary replacement, this step activates the daemon (e.g., com.acronis.mms) via its configured trigger, such as RunAtLoad on boot or StartInterval. On macOS, daemons like com.acronis.acep run every ~14 days, but manual reload or reboot forces execution. The malicious script runs with root privileges, spawning a shell. Expected outcome: Full root access without password.

## Requirements

1. Malicious binary in place
2. Identified daemon trigger from plists
3. Admin access to launchctl

## Defense

Defensive measures and detection strategies:

- Disable unnecessary LaunchDaemons with launchctl unload
- Monitor launchd logs for unexpected executions (/var/log/system.log)
- Implement SIP (System Integrity Protection) to protect system paths

## Objectives

1. Execute malicious code as root
2. Obtain persistent root shell
3. Validate escalation success

## Instructions

### Step 1: Identify Daemon Trigger

**Context**: Determine activation method from plist.

Review the relevant plist for keys like <RunAtLoad> or <StartInterval>.

> E.g., RunAtLoad requires reboot or load.

### Step 2: Manually Load or Trigger Daemon

**Context**: Force execution of the daemon.

For immediate trigger, unload and reload:

```bash
sudo launchctl unload /Library/LaunchDaemons/com.acronis.mms.plist
sudo launchctl load /Library/LaunchDaemons/com.acronis.mms.plist
```

> Alternatively, reboot for RunAtLoad daemons.

### Step 3: Validate Escalation

**Context**: Confirm root access from malicious payload.

Check for spawned shell, e.g., if payload copies /bin/sh to /tmp/rootsh:

```bash
/tmp/rootsh
whoami
```

> Output: root, with full privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- macos
- privilege-escalation
- launchdaemons
