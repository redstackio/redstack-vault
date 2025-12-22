---
id: 98219e0f-2eab-46d2-94ec-a7d677e7dfdb
name: Linux-File-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.984500+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - file-enumeration
  - linux-discovery
  - interesting-files
commands:
  - '[[commands/find-all-files-linux]]'
  - '[[commands/cat-etc-passwd]]'
  - '[[commands/find-suid-files]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-File-Enumeration

## Summary

Linux File Enumeration is a technique used to discover interesting files on a Linux system. This procedure involves traversing directories, searching for sensitive files like configuration data, user accounts, and system logs, and inspecting their contents where possible. It is commonly employed by attackers during post-exploitation to identify credentials, network configurations, or misconfigurations that enable further lateral movement or privilege escalation.

## Description

Linux File Enumeration targets the file system to locate files containing valuable information such as usernames, passwords, API keys, or application configurations. With even low-privileged shell access, many files in /etc, /proc, and user home directories are readable. The technique leverages built-in commands like find, ls, and cat to systematically probe the system without requiring additional tools. This is particularly useful in reconnaissance phases after initial access, helping attackers map the environment and find vectors for escalation. For example, readable shadow files or bash history can reveal weak passwords or prior commands executed by users.

## Requirements

1. Shell access to the target Linux system (local or remote via SSH/reverse shell)
2. Basic read permissions on common directories like /etc and /proc (often available to standard users)
3. No elevated privileges required for most files, but sudo or root may be needed for protected ones like /etc/shadow

## Defense

- Implement proper access controls to limit access to sensitive files, such as using chmod and chown to restrict readability
- Regularly monitor file system changes and file access logs with tools like auditd or SELinux
- Implement file integrity monitoring (e.g., AIDE or Tripwire) to detect unauthorized access or modifications to critical files

## Objectives

1. Discover interesting files on a Linux system that may contain sensitive data
2. Identify credentials, configurations, or system details for further exploitation
3. Highlight potential weaknesses in file permissions to aid in system hardening

## Instructions

### Step 1: Broad File System Traversal

**Context**: Start with a system-wide search to identify accessible files and directories, focusing on patterns that reveal structure without overwhelming output. This step uses find to list files while suppressing permission errors, providing an overview of the file system layout.

**Command** ([[commands/find-all-files-linux]]):
```bash
find / -type f 2>/dev/null | head -50
```

> The find command recursively searches from root, limiting to files (-type f) and redirecting errors to /dev/null. The head -50 limits output for initial review. Pipe to grep for specific extensions like .conf or .key if needed. This helps spot directories like /etc or /home early.

### Step 2: Inspect Key System Files

**Context**: Target well-known locations for sensitive data, such as user accounts and configs in /etc. Use cat to read contents if permissions allow, revealing users, hosts, or database settings. Cross-reference with the list of interesting files for comprehensive coverage.

Reference the curated list: [[codes/List-of-Interesting-Linux-Files]]

**Command** ([[commands/cat-etc-passwd]]):
```bash
cat /etc/passwd
```

> This displays user account details including usernames, UIDs, home directories, and shells. Look for service accounts or unusual users. If /etc/shadow is readable (rare without root), cat it for hashed passwords. Expected output includes lines like "root:x:0:0:root:/root:/bin/bash".

### Step 3: Identify Privilege Escalation Vectors

**Context**: Search for files with special permissions like setuid (SUID) that could allow escalation. This step focuses on binaries and scripts that run with elevated privileges, a common post-enumeration pivot.

**Command** ([[commands/find-suid-files]]):
```bash
find / -perm -u=s -type f 2>/dev/null
```

> The -perm -u=s flag finds files where the user has setuid bit set. Review the output for misconfigured binaries (e.g., vim or find with SUID). Expected: Paths like "/usr/bin/sudo" or custom scripts. If any are writable or unusual, they may be exploitable.
