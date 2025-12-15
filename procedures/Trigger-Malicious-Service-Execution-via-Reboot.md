---
id: proc-004
tags:
  - reboot
  - trigger
  - service-execution
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/system-reboot]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:07.223Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Unix Shell]]'
---
# Trigger-Malicious-Service-Execution-via-Reboot

## Summary

This procedure reboots the Linux system to force systemd to reload the modified NordVPN service file, executing the injected payload as root and creating the SUID binary.

## Description

After overwriting the service file, a reboot causes systemd to parse and start the nordvpnd.service, running the malicious ExecStart command with root privileges. This creates /tmp/evilbash with SUID set. The reboot can be initiated with sudo or physical access; no direct privileged command is needed if access allows.

## Requirements

1. Modified service file in place
2. Sudo access or physical console access for reboot
3. systemd as init system

## Defense

Defensive measures and detection strategies:

- Disable automatic service starts for third-party packages
- Validate unit files on boot with systemd-analyze verify
- Log boot events and service starts via journalctl -b
- Restrict reboot privileges with sudoers or polkit

## Objectives

1. Reload modified systemd configuration
2. Execute payload as root during boot
3. Deploy SUID backdoor for escalation

## Instructions

### Step 1: Initiate Reboot

**Context**: Restart the system to trigger service loading and payload execution.

**Command** ([[commands/system-reboot]]):
```bash
sudo reboot
```

> System shuts down and restarts; payload runs on service init.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Sub-Techniques

-

## Commands Used

- [[commands/system-reboot]]

## Tools Used

-

## Tags

- [[reboot]]
- [[trigger]]
- [[service-execution]]
