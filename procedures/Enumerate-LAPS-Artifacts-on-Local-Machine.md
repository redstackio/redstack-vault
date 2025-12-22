---
id: 5130d68f-3348-474b-a11b-b76a9425c400
name: Enumerate-LAPS-Artifacts-on-Local-Machine
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T19:12:06.996469+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - laps
commands:
  - '[[commands/powershell-get-childitem-laps-dll]]'
  - '[[commands/cmd-dir-laps-dll]]'
  - '[[commands/reg-query-laps-enabled]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-LAPS-Artifacts-on-Local-Machine

## Summary

This procedure checks for Local Administrator Password Solution (LAPS) artifacts on a local Windows machine, including registry keys and filesystem files, to determine if LAPS is deployed without querying domain controllers for Group Policy Objects (GPOs) or Organizational Units (OUs). This is useful in reconnaissance to identify password management configurations.

## Description

LAPS is a Microsoft solution that automates the management of local administrator account passwords in Active Directory environments. Artifacts of LAPS deployment can be found locally on endpoints, allowing attackers or testers to detect its presence stealthily. The procedure focuses on two key indicators: the AdmPwd registry value indicating LAPS policy enablement and the presence of the Admpwd.dll file in the LAPS installation directory. This approach avoids noisy domain queries that could trigger alerts. It applies to Windows systems in enterprise environments where LAPS might be enforced via GPO.

## Requirements

1. Local administrator access or equivalent privileges to query the registry and filesystem.
2. Windows operating system (Windows 7 or later, typically in domain-joined setups).
3. PowerShell or Command Prompt available (standard on Windows).

## Defense

Defensive measures and detection strategies:

- Monitor registry access to HKLM\Software\Policies\Microsoft Services\AdmPwd using Windows Event ID 4657 (registry value modification) or Sysmon Event ID 13 (registry events).
- File access monitoring for C:\Program Files\LAPS\CSE\Admpwd.dll via Sysmon Event ID 11 (file creation) or Windows Defender scans.
- Implement least privilege to restrict registry and filesystem enumeration on sensitive paths.
- Use application whitelisting to block unauthorized PowerShell or cmd executions.

## Objectives

1. Identify if LAPS policy is enabled via registry check.
2. Confirm LAPS deployment by verifying the Admpwd.dll file existence.
3. Gather evidence of LAPS usage for further privilege escalation planning.

## Instructions

### Step 1: Query Registry for LAPS Policy Enablement

**Context**: This step checks the registry for the AdmPwdEnabled value under the LAPS policy key. A value of 1 indicates LAPS is enabled; absence or 0 means it's not. This provides quick confirmation without filesystem access.

**Command** ([[commands/reg-query-laps-enabled]]):
```cmd
reg query "HKLM\Software\Policies\Microsoft Services\AdmPwd" /v AdmPwdEnabled
```

> This command queries the specific registry key. If the key exists and the value is 1, LAPS is active. If the key is missing, LAPS is likely not deployed. Run this in Command Prompt for native Windows compatibility.

### Step 2: Enumerate LAPS DLL File Using PowerShell

**Context**: This step searches for the Admpwd.dll file in the LAPS CSE directory, which is installed if LAPS Client Side Extension is present. Existence of the file confirms LAPS installation.

**Command** ([[commands/powershell-get-childitem-laps-dll]]):
```powershell
Get-ChildItem 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

> Execute in PowerShell. Successful output lists the file details (size, timestamp). If the file is not found, an error or empty result indicates no LAPS deployment. This is preferred for scripting and automation.

### Step 3: Enumerate LAPS DLL File Using Command Prompt (Alternative)

**Context**: As an alternative to PowerShell, use native cmd to list the Admpwd.dll file. This is useful if PowerShell is restricted or for compatibility in older environments.

**Command** ([[commands/cmd-dir-laps-dll]]):
```cmd
dir "C:\Program Files\LAPS\CSE\Admpwd.dll"
```

> Run in Command Prompt. Output shows file metadata if present. Use this if PowerShell execution policy blocks the previous step.
