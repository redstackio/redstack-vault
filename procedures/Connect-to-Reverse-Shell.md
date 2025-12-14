---
tags:
  - reverse-shell
  - rce
  - netcat
type: procedure
tools:
  - '[[tools/ADB]]'
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/nc-reverse-shell-listener]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:42.962Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: c2b07afc-30ae-442f-ac07-4f480fa79acb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Connect-to-Reverse-Shell

## Summary

This procedure sets up a listener to capture the reverse shell connection from the executed malicious library on the victim's Android device.

## Description

Once the library loads, it initiates a connection to 127.0.0.1:6666. The attacker uses ADB to shell into the device and runs netcat as a listener. This provides command execution on the victim device, confirming RCE. Requires physical or debug-enabled access for ADB.

## Requirements

1. ADB enabled on device (USB debugging)
2. Netcat installed or available
3. Port 6666 free; payload configured for localhost bind
4. App restart completed

## Defense

Defensive measures and detection strategies:

- Disable USB debugging on production devices
- Monitor for netcat processes or unusual network binds in app sandboxes
- Use app shielding to prevent reverse connections from native libs

## Objectives

1. Receive and interact with the reverse shell
2. Validate RCE success
3. Escalate access if needed

## Instructions

### Step 1: Access Device Shell via ADB

**Context**: Bridge to the device for listener setup.

Connect device via USB and run:

```bash
adb shell
```

> Enters Android shell as root or app user.

### Step 2: Start Netcat Listener

**Context**: Bind to port for incoming payload connection.

Execute [[commands/nc-reverse-shell-listener]]:

```bash
nc 127.0.0.1 6666
```

> Listener waits; shell connects upon library execution, granting interactive access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/nc-reverse-shell-listener]]

## Tools Used

- [[tools/ADB]]
- [[tools/nc]]

## Tags

- shell-access
- listener
- android
