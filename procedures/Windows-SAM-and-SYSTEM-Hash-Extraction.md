---
id: edfd5c34-1644-474b-bb90-5db50f3d02fb
name: Windows-SAM-and-SYSTEM-Hash-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.814296+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/OS Credential Dumping|T1003.002 - Security Account Manager]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/SAM and SYSTEM files]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/john-convert-sam-to-nt-format]]'
  - '[[commands/pwdump-dump-hashes-from-system-and-sam]]'
  - '[[commands/samdump2-dump-sam-database]]'
  - '[[commands/samdump2-extract-hashes-from-system-and-sam]]'
platforms:
  - Windows
tools:
  - '[[tools/pwdump]]'
  - '[[tools/samdump2]]'
  - '[[tools/john-the-ripper]]'
validated: true
---

# Windows-SAM-and-SYSTEM-Hash-Extraction

## Summary

This procedure extracts password hashes from the Windows Security Account Manager (SAM) and SYSTEM registry hive files for offline cracking, enabling potential privilege escalation or credential access on compromised Windows systems.

## Description

The SAM database stores local user account hashes (LM/NTLM), while the SYSTEM hive contains encryption keys (e.g., BootKey) needed to decrypt them. Attackers with physical or administrative access to a Windows machine can copy these files from protected locations like C:\Windows\System32\config and use offline tools to dump usable hashes. These hashes can then be cracked using dictionary or brute-force attacks to recover plaintext passwords, allowing lateral movement or persistence. This technique is common in post-exploitation scenarios where direct LSASS dumping is blocked by EDR. It requires administrative privileges to access the files and is most effective on older Windows versions without full disk encryption.

## Requirements

1. Administrative access to the target Windows system (local or via remote shell) to read protected registry hives.
2. Ability to copy files from C:\Windows\System32\config (e.g., via PowerShell or CMD).
3. Offline cracking setup with tools like John the Ripper on a separate machine (Linux preferred for tool compatibility).
4. BootKey extraction capability, as SYSTEM file provides the necessary decryption keys.

## Defense

- Enable BitLocker or full disk encryption to protect registry hives at rest.
- Monitor file access to sensitive paths like %SystemRoot%\System32\config using Windows Audit Policy or EDR tools.
- Restrict administrative privileges and use LAPS (Local Administrator Password Solution) for unique local admin passwords.
- Implement application whitelisting to block unauthorized dumping tools and enable Credential Guard to protect LSASS.

## Objectives

1. Locate and copy SAM and SYSTEM registry hive files from the target system.
2. Extract NTLM hashes using offline dumping tools.
3. Crack recovered hashes to obtain plaintext credentials for privilege escalation.
4. Use cracked credentials for further access or persistence.

## Instructions

### Step 1: Locate SAM and SYSTEM Registry Hive Files

**Context**: Identify the locations of the SAM and SYSTEM files, which are protected and may have backups in repair or RegBack directories. Copy them to a working directory for offline processing. Note that direct access requires admin rights, and on modern Windows (post-2017), RegBack may be disabled.

**Code** ([[codes/Windows-SAM-and-SYSTEM-Hive-Locations]]):

```powershell
# Usually %SYSTEMROOT% = C:\Windows
%SYSTEMROOT%\repair\SAM
%SYSTEMROOT%\System32\config\RegBack\SAM
%SYSTEMROOT%\System32\config\SAM
%SYSTEMROOT%\repair\system
%SYSTEMROOT%\System32\config\SYSTEM
%SYSTEMROOT%\System32\config\RegBack\system
```

> Use PowerShell or CMD to navigate and copy files, e.g., `copy C:\Windows\System32\config\SAM C:\temp\SAM`. Expected output: Files copied without errors. If access denied, escalate privileges first.

### Step 2: Dump Hashes Using Pwdump (Offline Mode)

**Context**: Pwdump can process copied SYSTEM and SAM files offline to extract NTLM hashes. This step decrypts the hashes using the BootKey from SYSTEM.

**Command** ([[commands/pwdump-dump-hashes-from-system-and-sam]]):

```bash
pwdump SYSTEM SAM > /root/sam.txt
```

> Run on a Linux machine with the copied files in the current directory. Expected output: A text file (/root/sam.txt) containing username:hash pairs in pwdump format (e.g., Administrator:1000:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::). Success if no decryption errors.

### Step 3: Alternative Dump Using Samdump2 (Generic SAM File)

**Context**: If pwdump fails or for single-file processing, use samdump2 on a specific SAM file. This is useful for partial dumps or testing.

**Command** ([[commands/samdump2-dump-sam-database]]):

```bash
samdump2 /path/to/SAM/file > samdump.txt
```

> Specify the full path to the copied SAM file. Expected output: Hashes in samdump format (e.g., USERNAME:::::HASH), saved to samdump.txt. If SYSTEM is not provided, LM hashes may be uncrackable; pair with BootKey extraction.

### Step 4: Dump Hashes Using Samdump2 (Full SYSTEM and SAM)

**Context**: For complete extraction including BootKey decryption, provide both files to samdump2. This produces crackable NTLM hashes.

**Command** ([[commands/samdump2-extract-hashes-from-system-and-sam]]):

```bash
samdump2 SYSTEM SAM -o sam.txt
```

> Ensure both files are in the current directory. Expected output: sam.txt with formatted hashes (e.g., user:UID:PID:LM:NT:::), ready for cracking. Verify by checking for valid NTLM hashes (32 hex chars).

### Step 5: Crack Hashes Using John the Ripper

**Context**: Load the dumped hashes into John the Ripper in NT format to attempt cracking. Use wordlists or rules for efficiency.

**Command** ([[commands/john-convert-sam-to-nt-format]]):

```bash
john --format=NT /root/sam.txt
```

> Replace /root/sam.txt with your hash file path. Expected output: Cracking session starts, showing progress (e.g., "Loaded 5 password hashes"). Recovered passwords appear in ~/.john/john.pot. If weak passwords, plaintext recovered quickly; otherwise, use --incremental for brute-force.
