---
id: d99cba06-5e7c-42ac-8d5e-584d87388c0d
name: loot-powershell-transcripts-for-credentials
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.327427+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
sub_techniques:
  - '[[techniques/Unsecured Credentials/Credentials In Files|T1552.001]]'
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Powershell Transcript]]'
  - '[[tags/Windows - Privilege Escalation]]'
  - credential-dumping
  - powershell
commands:
  - '[[commands/powershell-search-transcripts-documents]]'
  - '[[commands/powershell-search-transcripts-custom-folder]]'
  - '[[commands/powershell-extract-sensitive-from-transcript]]'
platforms:
  - Windows
tools: []
validated: true
---

# Loot PowerShell Transcripts for Credentials

## Summary

This procedure details how to search for and extract sensitive credentials, such as plaintext passwords, from PowerShell transcript files on a Windows system. PowerShell transcripts log all commands executed and their outputs, which may inadvertently capture credentials if users run scripts or commands involving passwords. This technique is useful in post-exploitation scenarios to harvest credentials for further privilege escalation or lateral movement.

## Description

PowerShell transcription is a feature that records sessions to text files, often enabled for auditing or troubleshooting. These files can contain sensitive information like passwords typed into commands (e.g., Connect-VPN -Password 'secret123' or Set-Content -Value 'password'). An attacker with initial access can locate these files in default locations and parse them for credential patterns. This is particularly effective if transcription was enabled by administrators or users. The procedure assumes low-privileged access but may require escalation if files are protected. Success depends on transcription being active and users executing sensitive commands in PowerShell.

## Requirements

1. Access to a Windows system via shell (e.g., PowerShell or CMD) with read access to user directories.
2. PowerShell 3.0 or later installed (standard on modern Windows).
3. Knowledge of basic PowerShell scripting for file searching and pattern matching.
4. Optional: Elevated privileges to access transcripts from other users or system folders.

## Defense

- Disable PowerShell transcription via Group Policy (Turn on PowerShell Script Block Logging) or set $PSModuleLogging to avoid logging sensitive data.
- Store transcripts in secure, monitored locations with restricted access (e.g., ACLs denying read to non-admins).
- Implement application whitelisting to prevent unauthorized PowerShell execution.
- Monitor file access to transcript directories using Windows Event Logs (Event ID 4663 for file reads).
- Use tools like Microsoft Defender for Endpoint to detect anomalous file searches in user directories.

## Objectives

1. Locate PowerShell transcript files on the target system.
2. Extract credentials or sensitive data from the transcripts.
3. Use harvested credentials for privilege escalation or further attacks.
4. Validate the presence of usable information without alerting defenses.

## Instructions

### Step 1: Search for Transcripts in User Documents Folder

**Context**: PowerShell transcripts are often saved to the user's Documents folder by default. This step identifies potential log files using a wildcard pattern to match the standard naming convention.

**Command** ([[commands/powershell-search-transcripts-documents]]):
```powershell
Get-ChildItem -Path "$env:USERPROFILE\Documents" -Filter "PowerShell_transcript.*.txt" -Recurse
```

> This command recursively searches the current user's Documents folder for transcript files. It lists file paths, sizes, and last modified dates. If no files are found, transcription may not be enabled for this user.

**Expected Output**:
```
    Directory: C:\Users\username\Documents

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         10/1/2023   2:30 PM           2048 PowerShell_transcript.HOSTNAME.RANDOM.20231001_143000.txt
```

### Step 2: Search for Transcripts in Custom Transcripts Folder

**Context**: Some configurations save transcripts to a centralized folder like C:\Transcripts. This step checks for such directories, handling cases where the folder may not exist to avoid errors.

**Command** ([[commands/powershell-search-transcripts-custom-folder]]):
```powershell
Get-ChildItem -Path "C:\Transcripts" -Filter "PowerShell_transcript.*.txt" -Recurse -ErrorAction SilentlyContinue
```

> This command attempts to search a custom transcripts directory, suppressing errors if the path doesn't exist. It may reveal admin or multi-user transcripts if accessible.

**Expected Output**:
```
    Directory: C:\Transcripts\2023-10-01

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         10/1/2023   3:00 PM           4096 PowerShell_transcript.HOSTNAME.RANDOM.20231001_150000.txt
```

### Step 3: Extract Sensitive Information from Transcript Files

**Context**: Once files are located, parse them for credential patterns like 'password', 'pass', or base64-encoded strings that might contain secrets. This step uses pattern matching to highlight potential leaks.

**Command** ([[commands/powershell-extract-sensitive-from-transcript]]):
```powershell
Select-String -Path "C:\Users\username\Documents\PowerShell_transcript.*.txt" -Pattern "(?i)(password|pass|pwd|secret|key|token)[:=\s]+['\"]?([^\s'\"]+)['\"]?"
```

> This command uses regex to search all transcript files in Documents for common credential keywords, capturing values after them. Adjust the path to specific files if needed. Why: It automates identification of plaintext credentials without manual review.

**Expected Output**:
```
C:\Users\username\Documents\PowerShell_transcript.HOSTNAME.RANDOM.20231001_143000.txt:45: $password = 'AdminPass123!'
C:\Users\username\Documents\PowerShell_transcript.HOSTNAME.RANDOM.20231001_150000.txt:12: Connect-Azure -Key 'abc123def456'
```

**Success Indicators**:
- Transcript files are discovered with recent timestamps.
- Extracted patterns reveal usable credentials (e.g., passwords matching known formats).
- No access denied errors, indicating sufficient privileges.
