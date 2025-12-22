---
id: 4eb9ecd7-be60-4729-a7bc-b282b7af397a
name: Linux-Password-Looting-from-Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.459223+00:00'
updated_at: '2023-04-10T20:34:28.644594+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
  - '[[Credentials in Files]]'
sub_techniques: []
tags:
  - files-containing-passwords
  - linux-privilege-escalation
  - looting-for-passwords
commands:
  - '[[commands/grep-search-for-password-in-filesystem]]'
  - '[[commands/find-grep-search-for-password-in-directory]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Password-Looting-from-Files

## Summary

This procedure searches for files on a Linux system that may contain plain text passwords, enabling attackers to extract credentials for privilege escalation or lateral movement. It uses built-in tools like grep and find to recursively scan the filesystem or specific directories for keywords such as 'PASSWORD', helping identify misconfigured or hardcoded credentials in configuration files, scripts, or logs.

## Description

In a post-exploitation scenario on a Linux system, attackers often look for credentials stored in plain text within files to expand their access. This technique targets common locations like configuration files (/etc/), user home directories, application logs, and scripts where developers might have left passwords exposed. The procedure assumes initial shell access as a low-privileged user and focuses on non-destructive searches to avoid alerting defenders. Success can lead to valid credentials for SSH keys, database access, or sudo escalation. It maps to credential access tactics by dumping files for offline analysis if needed.

## Requirements

1. Shell access to a Linux system as a low-privileged user (e.g., via SSH or reverse shell).
2. Read permissions on target directories (filesystem searches may require elevated privileges for protected areas like /root).
3. Basic familiarity with bash commands; no additional tools required as grep and find are standard.

## Defense

- Enforce strict file permissions using chmod and chown to restrict read access to sensitive files (e.g., 600 for config files containing secrets).
- Implement password policies prohibiting plain text storage; use tools like Vault or environment variables for secrets management.
- Monitor filesystem access with auditd or SELinux to detect anomalous reads on credential-like files; enable logging for grep/find usage in security contexts.

## Objectives

1. Identify files containing plain text passwords or credential keywords.
2. Extract and validate discovered credentials for further exploitation.
3. Escalate privileges or access additional resources using looted passwords.

## Instructions

### Step 1: Search Entire Filesystem for Password Keywords

**Context**: Perform a recursive search across the entire Linux filesystem for the keyword 'PASSWORD' to locate potential credential files. This step uses grep to scan all readable files, ignoring case and whole-word matches, while suppressing errors for efficiency. It's broad and may take time on large systems, so run it in a screen or tmux session.

**Command** ([[commands/grep-search-for-password-in-filesystem]]):
```bash
grep --color=auto -rnw '/' -ie "PASSWORD" --color=always 2> /dev/null
```

> This command highlights matches in color, shows file paths and line numbers, and redirects errors to /dev/null to reduce noise. Expected output includes lines like '/etc/app.conf:23:PASSWORD=secret123' if credentials are found. Pipe to a file (e.g., | tee passwords.txt) for later review. If no output, narrow the search to specific directories like /etc or /home.

### Step 2: Search Current Directory and Subdirectories for Password Keywords

**Context**: For targeted looting in the current working directory (e.g., after navigating to /var/www or a user's home), use find combined with grep to search files while handling spaces in filenames and skipping binaries. This is faster for focused areas and avoids full-system scans.

**Command** ([[commands/find-grep-search-for-password-in-directory]]):
```bash
find . -type f -exec grep -i -I "PASSWORD" {} /dev/null \;
```

> The find command locates files (-type f), executes grep on each (-exec), ignores case (-i), skips binaries (-I), and uses {} /dev/null to handle spaces. Expected output mirrors grep: file paths and matching lines. Review results for context (e.g., is it a real password or just a comment?). If matches are found, cat the full file for surrounding details.
