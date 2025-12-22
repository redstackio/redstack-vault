---
type: procedure
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credentials in Files|T1552.001 - Credentials In Files]]'
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Looting for passwords]]'
  - '[[tags/Old passwords in /etc/security/opasswd]]'
  - linux
  - privilege-escalation
  - credential-access
commands:
  - '[[commands/view-linux-opasswd-file]]'
tools: []
platforms:
  - Linux
skill_level: beginner
impact_level: high
detection_risk: low
verified: true
validated: true
---

# Linux-Privilege-Escalation-Looting-for-Old-Passwords

## Summary

This procedure demonstrates how to locate and extract old user password hashes from the /etc/security/opasswd file on older Linux systems. These hashes, stored by certain PAM modules for password quality enforcement, can be cracked offline to recover plaintext passwords, enabling privilege escalation if valid credentials are obtained.

## Description

On legacy Linux distributions or systems using specific authentication modules like pam_pwquality, previous passwords are retained in /etc/security/opasswd to enforce password reuse policies. This file contains hashed credentials for all users and is typically readable only by root. An attacker with root or sufficient privileges can access this file post-compromise to collect hashes for offline cracking using tools like Hashcat or John the Ripper. Success depends on the hash strength and wordlist quality, but it provides a low-effort way to gain additional credentials for lateral movement or persistence. This technique is most effective in environments with outdated configurations where old passwords are not purged.

## Requirements

1. Shell access to a Linux target system (local or remote)
2. Root privileges or read access to /etc/security (typically requires elevated permissions)
3. Basic familiarity with Linux file navigation and command execution

## Defense

- Regularly update Linux systems and PAM configurations to disable or remove old password storage (e.g., via pam_pwquality updates)
- Enforce strict file permissions on /etc/security/opasswd (mode 0600, owned by root:root)
- Monitor file access logs (e.g., via auditd) for unauthorized reads of sensitive files in /etc/security
- Implement password rotation policies and use strong hashing algorithms to reduce cracking feasibility

## Objectives

1. Identify and access the /etc/security/opasswd file containing old password hashes
2. Extract the hashes for offline analysis and cracking
3. Use recovered credentials for privilege escalation or further system compromise

## Instructions

### Step 1: Verify Existence and Access the Old Passwords File

**Context**: Begin by confirming the presence of the /etc/security/opasswd file, which may not exist on modern systems. If accessible, view its contents to retrieve the hashed old passwords. This step assumes you have a shell session; the file's contents will show username:hash pairs, which can then be piped to a cracker.

**Command** ([[commands/view-linux-opasswd-file]]):
```bash
cat /etc/security/opasswd
```

> This command outputs the file's contents directly to the terminal. If the file does not exist, it will return an error like "No such file or directory." Hashes are typically in formats like SHA-512 or MD5, depending on the system's configuration. Copy the output for offline cracking; for example, grep for specific users if needed: `cat /etc/security/opasswd | grep username`.

### Step 2: Extract and Prepare Hashes for Cracking

**Context**: Once viewed, isolate the hashes from the output. This manual step ensures clean input for cracking tools, focusing on why extraction is key: raw output may include metadata, but usernames and hashes are the actionable data for credential recovery.

**Instructions**: From the cat output, note the format (e.g., "root:$6$..."). Save relevant lines to a file like `old_hashes.txt` using redirection: `cat /etc/security/opasswd > old_hashes.txt`. If no dedicated cracking command is needed here, proceed to external tools like Hashcat in a follow-on procedure.

> Expected success: A text file or terminal output showing lines like "username:$hash$salt". If empty or inaccessible, the technique fails—indicating modern hardening or insufficient privileges.
