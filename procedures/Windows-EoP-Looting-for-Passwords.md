---
id: f6793a11-c4b0-4cac-9cb9-bb924d9086d1
name: Windows-EoP-Looting-for-Passwords
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.988087+00:00'
updated_at: '2023-04-10T20:37:53.834552+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Search for a file with a certain filename]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/windows-dir-search-password-files]]'
  - '[[commands/windows-where-search-user-txt]]'
  - '[[commands/windows-where-search-ini-files]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-EoP-Looting-for-Passwords

## Summary

This procedure outlines how to search a compromised Windows system for files containing passwords or credentials, enabling privilege escalation by extracting sensitive information from common storage locations like text files, configuration files, and the registry. It uses built-in Windows commands to recursively scan directories for patterns indicative of credentials, such as files with 'pass', 'cred', or 'vnc' in their names, or specific extensions like .ini and .config.

## Description

In a privilege escalation scenario on Windows, attackers often loot the filesystem for hardcoded credentials, weak passwords, or configuration files that reveal secrets. This technique targets plain-text storage of credentials in user directories, application configs, or system logs, which can be used to impersonate higher-privileged accounts or pivot to other systems. The approach leverages native tools like dir and where to avoid detection from introducing new binaries. It is particularly effective post-initial access when limited to command-line execution, mapping to MITRE ATT&CK techniques for credential access and discovery. Success depends on the target's configuration, such as unencrypted files or poor access controls, and can lead to domain admin access if sensitive creds are found.

## Requirements

1. Local access to a compromised Windows system (e.g., via initial foothold like a reverse shell).
2. Ability to execute commands in PowerShell or Command Prompt with at least user-level privileges.
3. No additional tools required, as it uses built-in Windows utilities.
4. Sufficient disk space and permissions to read target directories (e.g., C:\).

## Defense

- Implement application whitelisting and monitor for unusual file searches using tools like Sysmon (Event ID 11 for file creation/access patterns).
- Encrypt sensitive files and use credential managers like Windows Credential Vault to avoid plain-text storage.
- Enable auditing for file and directory access, alerting on recursive searches in sensitive paths like C:\Users or %APPDATA%.
- Regularly scan for and remove unnecessary credential files, and enforce least privilege to limit read access to configs.

## Objectives

1. Identify and extract files containing potential passwords or credentials from the filesystem.
2. Use discovered credentials to attempt privilege escalation, such as running processes as admin or lateral movement.
3. Collect evidence of system configuration weaknesses for further exploitation or reporting in red team exercises.

## Instructions

### Step 1: Search for Password and Credential Pattern Files

**Context**: Begin by using the dir command to recursively search the current directory and subdirectories for files matching common credential patterns, such as those with 'pass', 'cred', 'vnc' in the name or specific extensions like .txt, .xml, .ini, and .config. This step targets plain-text leaks in user or application files.

**Command** ([[commands/windows-dir-search-password-files]]):

```powershell
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*
```

> This command lists full paths to matching files in bare format (/B). The == operators chain the search patterns, though in practice, multiple dir invocations may be needed if syntax issues arise. Expected output includes paths to files like C:\Users\user\passwords.txt if present. Review listed files manually for credentials.

### Step 2: Locate user.txt File Recursively

**Context**: In capture-the-flag or assessment scenarios, search for a specific file like user.txt which may contain a flag or credential. This uses the where command to scan from the C:\ root, helping discover hidden or misplaced sensitive files.

**Command** ([[commands/windows-where-search-user-txt]]):

```powershell
where /R C:\ user.txt
```

> The /R flag enables recursive search. Expected output is the full path to user.txt if it exists, e.g., C:\Users\target\user.txt. If found, cat or type the file to extract contents.

### Step 3: Enumerate All .ini Configuration Files

**Context**: Configuration files like .ini often store unencrypted credentials for applications. Recursively search C:\ for all .ini files to inspect for passwords in sections like [Database] or [Auth]. This step complements the pattern search by targeting a common credential storage format.

**Command** ([[commands/windows-where-search-ini-files]]):

```powershell
where /R C:\ *.ini
```

> Similar to Step 2, this lists all .ini file paths. Expected output: A list of paths like C:\Windows\system.ini or C:\ProgramData\app.ini. Open and grep for keywords like 'password' or 'key' in these files using type or notepad.
