---
id: 63d7f636-8076-471b-8f8a-34a998802de7
type: procedure
verified: true
submitted: true
created_at: '2020-01-27T20:41:03.462931+00:00'
updated_at: '2023-05-25T19:54:14.229283+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Path Interception|T1034 - Path Interception]]'
sub_techniques: []
tags:
  - '[[tags/Misconfiguration]]'
commands:
  - '[[commands/wmic-query-system-for-unquoted-service-paths]]'
platforms:
  - Windows
tools: []
validated: true
---

# Query-Windows-for-Unquoted-Service-Paths

## Summary

This procedure queries a Windows system to identify services with unquoted paths in their executable configurations, a common misconfiguration that can allow attackers to perform path interception by placing malicious executables in intermediate directories. It filters for auto-starting services outside the Windows directory, helping to spot potential privilege escalation or persistence opportunities.

## Description

Unquoted service paths occur when a Windows service's ImagePath registry value contains spaces but lacks surrounding quotation marks. During service startup, Windows parses the path from left to right, attempting to execute the first matching .exe file it encounters. If an attacker can write to an intermediate directory in the path (e.g., creating C:\Program.exe for a service path like C:\Program Files\App\app.exe), they can hijack the service execution. This procedure uses WMIC to enumerate services and applies filters to highlight vulnerable auto-starting services not in protected system paths. It is typically used during post-exploitation reconnaissance on compromised Windows hosts to identify exploitable misconfigurations for further attacks like privilege escalation.

## Requirements

1. Local or remote access to a Windows system with administrative privileges (or sufficient rights to query services via WMIC).
2. Command Prompt (cmd.exe) or PowerShell environment on the target.
3. No additional tools required; WMIC is built into Windows.

## Defense

Defensive measures and detection strategies:

- Ensure all service ImagePath values in the registry (HKLM\SYSTEM\CurrentControlSet\Services) are quoted properly during software installation and updates.
- Use tools like PowerShell scripts or Group Policy to audit and remediate unquoted paths regularly.
- Monitor for unexpected file creations in program directories via file integrity monitoring (e.g., Sysmon Event ID 11) or EDR solutions.
- Enable Windows Defender Application Control (WDAC) or AppLocker to restrict executable paths for services.

## Objectives

1. Identify auto-starting Windows services with unquoted executable paths.
2. Filter out benign system services to focus on potentially exploitable third-party services.
3. Provide output suitable for manual review or scripting to check writability in vulnerable paths.

## Instructions

### Step 1: Enumerate and Filter Services

**Context**: This step uses WMIC to retrieve service details including the executable path and filters for auto-starting services that are not in the Windows directory and lack quotes, revealing potential unquoted path vulnerabilities. Run this from Command Prompt to avoid PowerShell's quote handling issues; if using PowerShell, prefix with 'cmd.exe /C'.

**Command** ([[commands/wmic-query-system-for-unquoted-service-paths]]):
```command_prompt
wmic.exe service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """"
```

> This command queries all services, selects those with 'Auto' start mode, excludes paths starting with 'c:\windows\', and removes lines containing quotes. Review the output paths manually; for each unquoted path with spaces (e.g., C:\Program Files\App\app.exe), check if intermediate directories like C:\Program are writable to assess exploitability. If no output appears, the system has no obvious unquoted auto-start services.
