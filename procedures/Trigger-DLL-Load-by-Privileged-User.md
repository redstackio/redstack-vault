---
id: proc-trigger-load
tags:
  - privilege-escalation
  - execution
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:30:27.109Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[PowerShell]]'
---
# Trigger-DLL-Load-by-Privileged-User

## Summary

This procedure simulates or performs the launch of Burp Suite under a high-privileged user context, triggering the load of the malicious DLL from the attacker-controlled path and achieving code execution with elevated privileges.

## Description

Switch to an admin user (or social engineer one to run Burp), then start the application. Burp's Java runtime attempts to load sunec.dll from the hijacked path, executing the payload. Use Process Monitor to confirm the load. Impact: Breaks privilege separation, allowing low-priv user to run code as admin, potentially compromising the system.

## Requirements

1. Access to privileged user credentials or session
2. Malicious DLL in place
3. Burp Suite executable path known

## Defense

Defensive measures and detection strategies:

- Run applications as low-priv users
- Enable DLL enforcement policies (e.g., via registry: HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel\DllVerification)
- Monitor process creation and DLL loads with Sysmon (Event ID 7)

## Objectives

1. Initiate Burp startup in privileged context
2. Confirm DLL hijack and payload execution
3. Validate escalation success

## Instructions

### Step 1: Switch to Privileged Context

**Context**: Log in or elevate to admin user.

Use Windows switch user or RDP as admin.

> Expected: Admin session active, confirmed with `whoami /groups` showing Administrators.

### Step 2: Launch Burp Suite

**Context**: Start Burp to trigger the load.

Run Burp executable (e.g., from Start Menu or `"C:\Program Files\Burp Suite\burpsuite.exe"`).

> Monitor with [[tools/Process-Monitor]] for successful DLL load from custom path. Expected: Payload executes (e.g., popup "Hijacked!") as admin.

### Step 3: Validate Escalation

**Context**: Confirm code ran with privileges.

If payload spawns cmd, check `whoami` in it.

> Expected: Admin output, proving escalation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]
- [[PowerShell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Process-Monitor]]

## Tags

- privilege-escalation
- execution

