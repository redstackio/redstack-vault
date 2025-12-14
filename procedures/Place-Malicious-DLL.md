---
id: proc-place-dll
tags:
  - dll-hijacking
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/copy-malicious-dll]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:30:27.114Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Place-Malicious-DLL

## Summary

This procedure deploys a custom malicious DLL, such as sunec.dll, into the prepared hijackable directory path, setting up Burp Suite to load and execute arbitrary code upon startup.

## Description

The malicious DLL must export the necessary functions (e.g., matching sunec.dll's interface) and include payload like a MessageBox or shell execution. Placed in the amd64 subpath, it exploits Burp's lack of path validation. Prerequisites include compiling the DLL with tools like Visual Studio. Outcome: DLL ready for privileged load, enabling code execution as the Burp runner.

## Requirements

1. Compiled malicious DLL (e.g., sunec.dll with payload)
2. Created directory structure from prior procedure
3. Write access to the target path

## Defense

Defensive measures and detection strategies:

- DLL search order hardening: Use safe DLL loading APIs in apps
- Scan for unsigned DLLs in unexpected paths with antivirus
- Monitor file copies to system directories via EDR tools

## Objectives

1. Position payload in load path
2. Ensure DLL compatibility with Burp's expectations
3. Test load without full execution if possible

## Instructions

### Step 1: Prepare Malicious DLL

**Context**: Ensure the DLL is built to mimic the target (e.g., sunec.dll for elliptic curve crypto, but with added exec code).

Use a DLL template and add payload like `MessageBoxA(NULL, "Hijacked!", "Alert", MB_OK);` in DllMain.

> Compile with Visual Studio: cl /LD malicious.c. Expected: sunec.dll binary.

### Step 2: Copy to Path

**Context**: Transfer the DLL to the hijack directory.

Execute [[commands/copy-malicious-dll]]:

```cmd
copy sunec.dll "C:\Program Files\Java\jre1.8.0_xxx\bin\server\amd64\sunec.dll"
```

> Expected output: 1 file(s) copied. Verify with `dir "C:\Program Files\Java\jre1.8.0_xxx\bin\server\amd64"` showing sunec.dll.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/copy-malicious-dll]]

## Tools Used


## Tags

- dll-hijacking
- execution

