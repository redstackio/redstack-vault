---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Last edited files]]'
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Looting for passwords]]'
commands:
  - '[[commands/find-recently-modified-files-exclude-proc]]'
platforms:
  - Linux
tools: []
verified: true
validated: true
---

# Linux-Password-Looting-via-Recently-Modified-Files

## Summary

This procedure demonstrates how to search for recently modified files on a Linux system to identify potential locations of unsecured credentials, such as password hashes or plaintext passwords in configuration files, history logs, or temporary files. It is useful during privilege escalation or post-exploitation phases to loot credentials for further access.

## Description

In Linux environments, attackers often look for recently modified files because they may contain updated credentials, such as those in user home directories, application configs, or system logs. This technique involves using file system search commands to filter for modifications within a short time frame (e.g., last 10 minutes) and excluding noisy directories like /proc. Once identified, these files can be inspected manually or with additional tools like grep for keywords like 'password' or 'hash'. This approach maps to discovering unsecured credentials and can lead to privilege escalation if sensitive files like /etc/shadow or user .ssh keys are found. It requires shell access and is most effective on systems with lax file permissions.

## Requirements

1. Shell access to the target Linux system (local or remote via SSH).
2. Read permissions on the file system (typically available to standard users).
3. Basic knowledge of Linux file paths and common credential storage locations (e.g., /etc, /home, /var).

## Defense

- Implement strict file permissions using chmod and chown to restrict access to sensitive directories.
- Use tools like auditd or file integrity monitoring (e.g., Tripwire, AIDE) to detect unauthorized file modifications.
- Rotate credentials frequently and store them in secure vaults (e.g., HashiCorp Vault) rather than plaintext files.
- Monitor for anomalous file access patterns via syslogs or SIEM tools.

## Objectives

1. Identify files modified recently that may contain credentials.
2. Loot and extract password hashes or plaintext secrets from discovered files.
3. Use extracted credentials for privilege escalation or lateral movement.

## Instructions

### Step 1: Search for Recently Modified Files

**Context**: Begin by scanning the entire file system for files modified within the last 10 minutes, excluding the /proc directory to reduce noise from system processes. This step uncovers potential credential files like bash history or config updates.

**Command** ([[commands/find-recently-modified-files-exclude-proc]]):
```bash
find / -mmin -10 2>/dev/null | grep -Ev "^/proc"
```

> This command starts the search from the root directory (/), limits to files modified in the last 10 minutes (-mmin -10), suppresses permission errors (2>/dev/null), and pipes output to grep to exclude /proc paths. Expected output is a list of file paths. Review the list manually for sensitive locations (e.g., /home/user/.ssh/id_rsa, /etc/passwd backups) and cat or grep them for credentials.

### Step 2: Inspect and Extract Credentials

**Context**: From the list of files, prioritize inspection of common credential spots. Use additional commands like cat, grep, or strings to extract content. For example, search for password-related strings in the discovered files.

**Instructions**: Pipe the output from Step 1 into grep for keywords:
```bash
grep -r "password\|hash\|key" /path/to/discovered/files
```

> Replace /path/to/discovered/files with actual paths from Step 1. If a file contains hashes (e.g., from /etc/shadow), copy them for offline cracking. Success is indicated by finding readable credential data; if files are encrypted or permission-denied, escalate privileges first.
