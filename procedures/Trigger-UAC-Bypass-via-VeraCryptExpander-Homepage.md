---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - uac-trigger
  - shellexecute-hijack
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/run-veracrypt-expander]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:29:44.572Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# Trigger-UAC-Bypass-via-VeraCryptExpander-Homepage

## Summary

This procedure executes VeraCryptExpander.exe with elevation and triggers the 'Homepage' button to invoke ShellExecute, hijacking the URL open via tampered HKCU keys to run the payload elevated.

## Description

VeraCryptExpander.exe runs elevated (UAC prompt) and uses ShellExecute(0, 0, L"http://www.test.com/", 0, 0, SW_SHOW) in WinMain.cpp for the Homepage button. This resolves HKCU handlers, executing malstaller.bat with admin privileges if hijacked. Impact: Full system compromise via binary replacement or other actions.

## Requirements

1. VeraCrypt installed with Expander.exe
2. Prior registry tampering completed
3. UAC enabled but bypassable

## Defense

Defensive measures and detection strategies:

- Patch VeraCrypt to use secure URL opening (e.g., system("explorer url"))
- Monitor ShellExecute calls in elevated processes
- Log UAC elevations and anomalous script executions

## Objectives

1. Achieve elevation without additional prompts
2. Execute payload in privileged context
3. Confirm compromise (e.g., file placement)

## Instructions

### Step 1: Launch Elevated Expander

**Context**: Start the process to gain elevation.

**Command** ([[commands/run-veracrypt-expander]]):

```bash
"C:\Program Files\VeraCrypt\VeraCryptExpander.exe"
```

> UAC prompts; approve. Expected output: GUI window opens.

### Step 2: Click Homepage Button

**Context**: Trigger the vulnerable ShellExecute.

**Instructions**: In the expander window, click the 'Homepage' button at the top.

> This calls the hijacked handler. Expected output: malstaller.bat runs elevated; payload actions complete (e.g., fake exe copied).
