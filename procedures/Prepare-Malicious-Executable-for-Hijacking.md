---
id: prepare-malicious-exe-acronis
tags:
  - exe-hijacking
  - malware-placement
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/copy-malicious-exe]]'
  - '[[commands/dir-c-drive]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:28:58.412Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Prepare-Malicious-Executable-for-Hijacking

## Summary

This procedure involves creating or obtaining a malicious executable and placing it as 'program.exe' in the C:\ root directory to exploit the Acronis Scheduler2 Service's insecure path lookup, setting up for privilege escalation upon service startup.

## Description

In the context of the Acronis True Image 2021 vulnerability, the service attempts to execute 'C:\program.exe' without validation. By placing a custom malicious EXE there beforehand, an attacker can hijack this execution flow. The EXE should include a detectable payload like a message box to confirm execution. This requires write access to C:\, typically needing admin privileges, but can chain with other vulns for lower-priv users. Expected outcome: The file is positioned for SYSTEM-level execution during installation.

## Requirements

1. Admin-level access to write to C:\
2. Compiler or pre-built EXE (e.g., via Visual Studio or msfvenom for payload)
3. Target Windows machine with C: as system drive

## Defense

Defensive measures and detection strategies:

- Restrict write access to C:\ root via GPO or filesystem permissions
- Monitor file creation in C:\ with Sysmon or EDR tools
- Audit service binaries for hardcoded insecure paths

## Objectives

1. Position malicious payload in hijackable location
2. Ensure EXE is executable by SYSTEM
3. Verify placement without triggering alerts

## Instructions

### Step 1: Create Malicious EXE

**Context**: Compile a simple EXE that pops a message box 'EXE Loaded' to demonstrate execution.

Use a tool like Visual Studio to build a C++ console app with MessageBoxA call, or msfvenom for a basic payload.

**Command** ([[commands/compile-simple-exe]]):
```bash
# Example using cl.exe (Visual Studio tools)
cl /Fe:malicious.exe simple_payload.cpp
```

> This compiles the EXE; replace with actual payload code showing MessageBox.

### Step 2: Place EXE in C:\

**Context**: Copy the EXE to the vulnerable path before triggering the service.

Execute [[commands/copy-malicious-exe]] to place it:

```bash
copy malicious.exe C:\program.exe
```

> Copies the file; ensure no AV interference.

### Step 3: Verify Placement

**Context**: Confirm the file is in place and accessible.

Run [[commands/dir-c-drive]]:

```bash
dir C:\ /b | findstr program.exe
```

> Outputs 'program.exe' if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used

- [[commands/copy-malicious-exe]]
- [[commands/dir-c-drive]]

## Tools Used


## Tags

- [[exe-hijacking]]
- [[lpe]]
