---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - '[[techniques/Password Filter DLL|T1174 - Password Filter DLL]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Search for file contents]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/powershell-cd-and-findstr-password-files]]'
  - '[[commands/powershell-findstr-append-password-config]]'
  - '[[commands/powershell-findstr-recursive-password-search]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Windows-Password-Looting-via-File-Contents-Search

## Summary

This procedure searches for files containing password-related information on a compromised Windows system by scanning common file types like XML, INI, TXT, and CONFIG files across the C: drive. It uses built-in PowerShell commands to identify potential credential stores, which can aid in privilege escalation or lateral movement by extracting usable passwords from configuration files or logs.

## Description

In a post-compromise scenario on a Windows host, attackers often loot for credentials stored in plaintext within application configuration files, scripts, or documents. This procedure leverages the findstr utility via PowerShell to perform case-insensitive searches for the string 'password' in specified file extensions, starting from the C: drive root. It includes recursive searching in subdirectories and outputs results to a file for review. This technique is particularly effective against systems with poor credential hygiene, such as development environments or legacy applications that embed passwords in files. Prerequisites include shell access (e.g., via initial foothold) and read permissions on the target directories. Success enables the attacker to collect credentials for further exploitation, such as domain admin access or network pivoting.

## Requirements

1. Shell access to a compromised Windows system (e.g., via PowerShell or CMD).
2. Read permissions on the C: drive and subdirectories (local user or higher).
3. PowerShell execution policy allowing script runs (bypass if needed with Set-ExecutionPolicy).

## Defense

Defensive measures and detection strategies:

- Implement least privilege access controls to restrict file read operations on sensitive directories.
- Monitor for anomalous file access patterns using Windows Event Logs (e.g., Event ID 4663 for file access) or EDR tools.
- Use credential guard features like Windows Credential Manager encryption and avoid plaintext storage in configs; enforce multi-factor authentication (MFA) to mitigate stolen credential impact.

## Objectives

1. Locate files containing potential password strings for credential extraction.
2. Collect and export search results for offline analysis to support privilege escalation.
3. Identify misconfigurations in file-based credential storage to enable lateral movement.

## Instructions

### Step 1: Navigate to C: Drive and Initial File Search

**Context**: Change to the C: drive root and search for files containing 'password' in common config extensions (XML, INI, TXT) to quickly identify surface-level hits without recursion.

**Command** ([[commands/powershell-cd-and-findstr-password-files]]):

```powershell
cd C:\ & findstr /SI /M "password" *.xml *.ini *.txt
```

> This command switches to C:\ and performs a case-insensitive (/I) multi-file search (/M) for 'password' in specified extensions, listing matching filenames. Expected output: A list of file paths like C:\path\to\config.xml if matches are found. If no output, no matches in root-level files.

### Step 2: Append Search Results for Config Files to Output File

**Context**: Extend the search to include .config files and redirect output to a results file for persistence and review, suppressing errors to focus on valid hits.

**Command** ([[commands/powershell-findstr-append-password-config]]):

```powershell
findstr /si password *.xml *.ini *.txt *.config 2>nul >> results.txt
```

> This runs from the current directory (C:\), searches case-insensitively (/i) in the listed extensions including .config, redirects errors to null (2>nul), and appends matching lines to results.txt. Expected output: No console display; check results.txt for lines like 'password=secret123' from matching files. Create results.txt manually if it doesn't exist.

### Step 3: Perform Recursive Search Across Subdirectories

**Context**: Conduct a full recursive scan of all files in C:\ and subfolders to uncover deeply nested password references, skipping problematic files.

**Command** ([[commands/powershell-findstr-recursive-password-search]]):

```powershell
findstr /spin "password" *.*
```

> This searches recursively (/s) in all files (*.*), skipping non-printable character files (/p), case-insensitively (/i), and includes line numbers (/n) for context. Expected output: Formatted results like 'filename:line:password content', e.g., config.ini:45:password=adminpass. Pipe to >> results.txt for logging if needed.
