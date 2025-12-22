---
id: 2784dfcb-ff7c-4587-b07d-6d357e51ecdf
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.663592+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/System-Service-Discovery|T1007 - System Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Unquoted Service Paths]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/wmic-enumerate-auto-unquoted-service-paths]]'
  - '[[commands/wmic-enumerate-unquoted-service-paths]]'
  - '[[commands/powershell-gwmi-enumerate-unquoted-service-paths]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-Windows-Unquoted-Service-Paths

## Summary

This procedure enumerates Windows services that have unquoted paths in their binary configuration, a common misconfiguration that can lead to privilege escalation by allowing attackers to place malicious executables in intermediate directories. It uses WMIC and PowerShell to query services, filtering for those not starting with the Windows system path and lacking quotes around the executable path, focusing on auto-start services to identify high-impact targets.

## Description

Unquoted service paths occur when the ImagePath registry value for a Windows service does not enclose the executable path in double quotes, particularly problematic if the path contains spaces. Windows parses such paths by attempting to execute files in sequential directory segments, enabling an attacker with write access to an intermediate directory to replace the legitimate executable with a malicious one, potentially gaining SYSTEM privileges if the service runs elevated. This procedure discovers such vulnerable services on a compromised Windows host, providing the service name, display name, and path for further analysis or exploitation. It is typically used during post-exploitation reconnaissance to identify privilege escalation vectors in environments with legacy or poorly configured services.

## Requirements

1. Local access to a Windows host (e.g., via initial foothold like a user shell).
2. Administrative privileges not required for enumeration, but write access to intermediate directories needed for exploitation.
3. WMIC or PowerShell available (standard on Windows Vista and later).
4. Command prompt or PowerShell execution permitted (may require bypassing execution policies if restricted).

## Defense

- Ensure all service binaries are installed with quoted paths in the registry (HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>\ImagePath).
- Apply least-privilege principles: Restrict write access to directories in service paths using ACLs.
- Regularly audit services with tools like PowerShell scripts or Sysinternals Autoruns to detect unquoted paths.
- Enable Windows Defender or EDR solutions to monitor service modifications and unexpected executable launches from non-standard paths.

## Objectives

1. Identify services with unquoted binary paths that could be hijacked for privilege escalation.
2. Gather details on auto-start services to prioritize those running with elevated privileges.
3. Provide actionable intelligence for subsequent exploitation steps, such as placing a malicious DLL or EXE.

## Instructions

### Step 1: Enumerate Auto-Start Services with Unquoted Paths Using WMIC

**Context**: This step uses WMIC to query all services, filtering for auto-start ones (StartMode=Auto) that do not start with the Windows directory and lack surrounding quotes, revealing potential privilege escalation targets quickly without PowerShell.

**Command** ([[commands/wmic-enumerate-auto-unquoted-service-paths]]):

```cmd
wmic service get name,displayname,pathname,startmode | findstr /i "Auto" | findstr /i /v "C:\Windows\\" | findstr /i /v """"
```

> This command retrieves service details and pipes the output through findstr filters: first for 'Auto' start mode, then excluding Windows system paths, and finally excluding lines with quotes. It identifies services vulnerable to path hijacking. If successful, it lists services like 'ServiceName DisplayName C:\Program Files\Vulnerable App\app.exe' without quotes.

### Step 2: Enumerate All Services with Unquoted Paths Using WMIC

**Context**: Broaden the search beyond auto-start services to catch manually triggered or delayed-start services that might still be exploitable, providing a comprehensive view of potential vulnerabilities.

**Command** ([[commands/wmic-enumerate-unquoted-service-paths]]):

```cmd
wmic service get name,displayname,startmode,pathname | findstr /i /v "C:\Windows\\" | findstr /i /v """"
```

> Similar to Step 1 but without the 'Auto' filter, this captures all non-Windows services without quotes. Review the output for paths with spaces (e.g., 'C:\Program Files\App\service.exe') where intermediate directories like 'C:\Program' could be targeted if writable.

### Step 3: Enumerate Auto-Start Unquoted Services Using PowerShell

**Context**: For environments where PowerShell is preferred or WMIC is unavailable, use Get-WmiObject to perform the same enumeration with more precise filtering, outputting structured results for easier parsing or scripting.

**Command** ([[commands/powershell-gwmi-enumerate-unquoted-service-paths]]):

```powershell
gwmi -class Win32_Service -Property Name, DisplayName, PathName, StartMode | Where {$_.StartMode -eq "Auto" -and $_.PathName -notlike "C:\Windows*" -and $_.PathName -notlike '"*'} | select PathName,DisplayName,Name
```

> This PowerShell one-liner queries the Win32_Service WMI class, filters for Auto start mode, non-Windows paths, and unquoted PathName, then selects key properties. Success yields a table like:

> Name                DisplayName            PathName
> ----                -----------            --------
> VulnService         Vulnerable Service     C:\Program Files\App\service.exe

> Use this to verify findings from WMIC and export to CSV if needed (add | Export-Csv vulnerable_services.csv).
