---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques:
  - '[[NTDS]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/Using ntdsutil]]'
commands:
  - '[[commands/ntdsutil-create-full-ifm-backup]]'
platforms:
  - Windows
tools: []
validated: true
---

# Dumping-AD-Domain-Credentials-using-ntdsutil

## Summary

This procedure demonstrates how to use the built-in ntdsutil tool on a Windows Domain Controller to create an Install From Media (IFM) backup of the Active Directory database. The backup includes the NTDS.dit file containing hashed passwords for all domain users, enabling subsequent extraction and cracking of credentials for lateral movement or privilege escalation in an Active Directory environment.

## Description

In an Active Directory attack scenario, once an attacker gains administrative access to a Domain Controller, they can dump domain credentials by creating an IFM backup using ntdsutil. This tool, part of the Active Directory Domain Services role, allows authoritative snapshots of the NTDS database without relying on external tools. The resulting backup contains the NTDS.dit file (the AD database), the SYSTEM registry hive (for decryption keys), and other components. These can be transferred off the DC and processed with tools like Impacket's secretsdump.py or DSInternals to extract NTLM hashes, Kerberos keys, and historical passwords. This technique targets environments with Domain Admins or equivalent privileges and is effective in air-gapped or monitored networks where volume shadow copy or LSASS dumping might be detected. Prerequisites include local admin rights on the DC; remote execution is possible via tools like PSExec if initial access is gained elsewhere.

## Requirements

1. Administrative privileges on a Domain Controller (Domain Admin or equivalent).
2. Local or remote command execution access to the Domain Controller (e.g., via RDP, WinRM, or PSEXEC).
3. Sufficient disk space on the target for the backup files (typically several GB depending on domain size).
4. Write access to a directory on the Domain Controller for storing the backup.

## Defense

- Restrict administrative access to Domain Controllers using just-in-time privileges and monitor logon events (Event ID 4624) for unauthorized admin sessions.
- Enable advanced auditing for backup operations and process creation involving ntdsutil (Event ID 4697 for service installation, though IFM doesn't install services).
- Implement application whitelisting to block unauthorized use of ntdsutil or monitor its execution via Sysmon (process creation with Image: ntdsutil.exe).
- Regularly review and secure backup locations; use protected volumes or network shares with strict ACLs.
- Deploy EDR solutions that alert on IFM backup creation or file access to NTDS.dit copies.

## Objectives

1. Create a full IFM backup of the NTDS database to obtain a portable copy of domain credentials.
2. Verify the backup contains the necessary files (NTDS.dit, SYSTEM hive) for offline hash extraction.
3. Prepare the backup for transfer and processing to recover plaintext passwords via cracking.

## Instructions

### Step 1: Create Full IFM Backup Using ntdsutil

**Context**: Execute the ntdsutil command in one line to activate the NTDS instance, enter IFM mode, create a full backup (including database, logs, and registry), and exit. This step requires running as administrator on the Domain Controller. Replace the backup path with a writable directory; avoid system-protected paths to prevent access issues.

**Command** ([[commands/ntdsutil-create-full-ifm-backup]]):
```cmd
ntdsutil "ac i ntds" "ifm" "create full $_BACKUP_PATH" q q
```

> The 'ac i ntds' activates the NTDS instance, 'ifm' enters Install From Media mode, 'create full' generates a complete backup suitable for credential extraction (includes NTDS.dit and decryption keys from SYSTEM hive), and 'q q' quits both modes. Run this from an elevated Command Prompt. If the one-liner fails due to quoting issues in PowerShell, use the interactive mode: launch 'ntdsutil', then 'activate instance ntds', 'ifm', 'create full $_BACKUP_PATH', 'quit', 'quit'. This step typically takes 1-5 minutes depending on domain size.

**Expected Output**: Console output confirming snapshot creation, e.g., "Snapshot created at [timestamp]" followed by "Full backup created successfully." Check the specified path for a new folder (e.g., 'Active Directory') containing files like NTDS.dit, edb.log, SYSTEM (registry hive), and a media stamp file.

### Step 2: Verify and Prepare Backup for Extraction

**Context**: Confirm the backup was created correctly and identify key files for credential dumping. This ensures the backup is usable offline without the live DC. Do not proceed if files are missing, as extraction tools require both NTDS.dit and the SYSTEM hive for decryption.

**Instructions**: Navigate to the backup directory using File Explorer or 'dir $_BACKUP_PATH\Active Directory'. Look for NTDS.dit (the AD database) and the SYSTEM file. Copy the entire backup folder to an attacker-controlled system for processing with tools like secretsdump.py from Impacket suite: secretsdump.py -ntds $_BACKUP_PATH\Active Directory\* -system $_BACKUP_PATH\Active Directory\SYSTEM LOCAL.

**Expected Output**: Directory listing shows NTDS.dit (>1MB), SYSTEM file, and log files. No errors during copy; extraction tool outputs user hashes if successful (e.g., administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::).

### Step 3: Clean Up Traces (Optional but Recommended)

**Context**: Remove the backup to reduce detection risk, as large file creations on DCs can trigger alerts. This step assumes the backup has been securely exfiltrated.

**Instructions**: Delete the backup directory using 'rd /s /q $_BACKUP_PATH' from an elevated prompt. Clear command history if using interactive mode, or enable command logging to review and erase.

**Expected Output**: Directory removed without errors; 'dir $_BACKUP_PATH' shows no files.
