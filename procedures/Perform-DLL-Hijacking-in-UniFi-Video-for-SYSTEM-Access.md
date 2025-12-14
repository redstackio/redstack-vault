---
id: 6b93fb3d-60fc-4dd2-9c0d-3c57a3174a53
name: Perform DLL Hijacking in UniFi Video for SYSTEM Access
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.219Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[DLL Search Order Hijacking]]'
sub_techniques: []
tags:
  - dll-hijacking
  - privilege-escalation
  - windows
commands:
  - '[[commands/query-safe-dll-search-mode]]'
  - '[[commands/copy-malicious-dll]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---

# Perform DLL Hijacking in UniFi Video for SYSTEM Access

## Summary

This procedure hijacks DLL loading in UniFi Video v3.10.1 by exploiting disabled SafeDllSearchMode and prior file deletion, allowing execution of malicious code as SYSTEM when the service loads the hijacked module.

## Description

Due to installation misconfiguration, SafeDllSearchMode is set to 0 in the registry, enabling DLL search order hijacking where the system checks current directory and PATH before safe locations. After deleting a legitimate DLL via the .tsExport weakness, an attacker places a malicious DLL (e.g., one that spawns a reverse shell) in a prioritized search path. When the UniFi Video service (running as SYSTEM) restarts, it loads the malicious DLL, granting elevated access. This targets Windows environments with local access; outcomes include arbitrary code execution at SYSTEM level.

## Requirements

1. Prior successful file deletion (e.g., from companion procedure)
2. Malicious DLL prepared (e.g., PoC DLL exporting functions like the original, with payload in DllMain)
3. Local access to copy files and manage services
4. Administrative service restart capability or scheduled reload trigger

## Defense

Defensive measures and detection strategies:

- Enable SafeDllSearchMode (set registry value to 1) and verify during installation
- Implement DLL signing enforcement via policies (e.g., Windows Defender Application Control)
- Audit service restarts and DLL loads via Sysmon (Event ID 7 for image loads)
- Restrict write access to application directories and PATH entries

## Objectives

1. Confirm vulnerable DLL search configuration
2. Stage malicious DLL to intercept legitimate loads
3. Execute payload as SYSTEM for full compromise

## Instructions

### Step 1: Verify SafeDllSearchMode

**Context**: Check the registry to confirm the system is vulnerable to search order hijacking.

**Command** ([[commands/query-safe-dll-search-mode]]):
```cmd
reg query "HKLM\System\CurrentControlSet\Control\Session Manager" /v SafeDllSearchMode
```

> Expected output: SafeDllSearchMode    REG_DWORD    0x0; if 1, the hijack may fail without PATH manipulation.

### Step 2: Stage the Malicious DLL

**Context**: Copy the prepared malicious DLL to the hijack location (e.g., the deleted DLL's path or a dir in the process's working directory).

**Command** ([[commands/copy-malicious-dll]]):
```cmd
copy /y "C:\temp\malicious.dll" "C:\Program Files\Ubiquiti UniFi Video\example.dll"
```

> The /y suppresses prompts; success shows "1 file(s) copied". The DLL should match the expected name and export required functions.

### Step 3: Trigger DLL Load

**Context**: Restart the service to force reloading of modules, executing the hijacked DLL as SYSTEM.

```cmd
net stop "UniFi Video"
net start "UniFi Video"
```

> Monitor with whoami /priv or a listener for shell; success indicated by elevated execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/query-safe-dll-search-mode]]
- [[commands/copy-malicious-dll]]

## Tools Used


## Tags

- [[dll-hijacking]]
- [[privilege-escalation]]
