---
tags:
  - windows
  - registry
  - setup
type: procedure
tools:
  - '[[tools/regedit]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Modify Registry]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 379aab2a-dd76-44b6-8a7a-6d1dbf94d2b6
created_at: '2025-12-14T17:26:49.003Z'
updated_at: '2025-12-14T17:26:49.003Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Modify Registry]]'
---
# Setup Test Environment for Steam Registry Path Traversal

## Summary

This procedure sets up a controlled test environment by copying Steam binaries to a user-writable directory and modifying the InstallPath registry value to include path traversal sequences, preparing for vulnerability verification without affecting the production Steam installation.

## Description

In the context of exploiting the Steam Client Service's improper path handling, this initial setup isolates testing to a user-controlled folder. The registry key `HKLM\Software\wow6432node\valve\steam\InstallPath` is modified because it grants full control to the Users group, allowing non-admin users to alter it. This enables subsequent steps to test traversal and injection without requiring elevated privileges upfront. Expected outcomes include a ready-to-test setup where the service fails gracefully and logs errors to the controlled directory.

## Requirements

1. Local user access on Windows with write permissions to `C:\`
2. Steam Client installed at default path (`C:\Program Files (x86)\Steam`)
3. Ability to stop the Steam Client Service (via services.msc or sc.exe)
4. [[tools/regedit]] available (built-in Windows tool)

## Defense

Defensive measures and detection strategies:

- Monitor registry modifications to Steam-related keys using Windows Event Logs (Event ID 4657)
- Restrict Users group permissions on HKLM\Software\wow6432node\valve\steam if possible
- Use application whitelisting to prevent unauthorized Steam binary copies

## Objectives

1. Isolate testing to avoid disrupting live Steam installation
2. Introduce path traversal in InstallPath for log generation
3. Verify setup by ensuring service can start and log to controlled path

## Instructions

### Step 1: Prepare Directories and Copy Binaries

**Context**: Create a test directory and copy essential Steam files to simulate the installation path.

**Command** (Manual File Operations):
```cmd
mkdir C:\test
mkdir C:\test\logs
copy "C:\Program Files (x86)\Steam\Steam.exe" C:\test\
copy "C:\Program Files (x86)\Steam\bin\win64\steamservice.dll" C:\test\bin\win64\
```

> This copies Steam.exe and steamservice.dll to the test location. Expected output: Files copied successfully, no errors.

### Step 2: Modify InstallPath Registry

**Context**: Use regedit to set InstallPath to a traversable path like `C:\test\1..`.

**Command** (Using [[tools/regedit]]):
```reg
# Launch regedit.exe, navigate to HKLM\Software\wow6432node\valve\steam
# Right-click InstallPath > Modify > Set Value data to 'C:\test\1..'
```

> Registry updated. Expected output: No permission errors; value changes to include '..' sequence.

### Step 3: Stop Steam Service

**Context**: Ensure the service is stopped before testing.

**Command** (PowerShell):
```powershell
Stop-Service -Name "Steam Client Service" -Force
```

> Service stops cleanly. Expected output: Service status shows 'Stopped'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Modify Registry]] Modify Registry

### Sub-Techniques

- None

## Commands Used

- None (manual operations)

## Tools Used

- [[tools/regedit]]

## Tags

- [[windows]]
- [[registry]]
- [[setup]]
