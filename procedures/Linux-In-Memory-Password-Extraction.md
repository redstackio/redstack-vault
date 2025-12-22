---
type: procedure
description: >-
  Extracts passwords and sensitive strings from Linux system memory using
  standard utilities to search for credential patterns.
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.540878+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/In memory passwords]]'
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Looting for passwords]]'
commands:
  - '[[commands/strings-grep-search-memory-for-passwords]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-In-Memory-Password-Extraction

## Summary

This procedure extracts printable strings from Linux kernel memory (/dev/mem) and filters for potential password indicators, enabling attackers to recover in-use credentials for privilege escalation or lateral movement. It leverages built-in tools like strings and grep, requiring root access to read memory directly.

## Description

Linux systems temporarily store passwords and other sensitive data in memory during active sessions, such as in process address spaces or kernel buffers. This procedure targets /dev/mem, a device file exposing physical memory, to dump and analyze strings for patterns like 'PASS' that may indicate password fields. It is particularly useful in post-exploitation scenarios where an attacker has gained initial shell access and seeks to loot credentials without relying on external tools. Success depends on the system's memory state (e.g., recent logins) and may yield partial or obfuscated data. This technique aligns with credential dumping but is limited to volatile memory, making it non-persistent.

## Requirements

1. Root or elevated privileges on the target Linux system (e.g., via sudo or kernel exploit) to access /dev/mem.
2. Standard Linux utilities available: strings (from binutils) and grep (coreutils), typically pre-installed.
3. A shell environment (bash or similar) for execution.
4. Awareness of system stability risks, as reading /dev/mem on running systems can cause crashes.

## Defense

Defensive measures and detection strategies:

- Restrict access to /dev/mem using file permissions (e.g., chmod 600 /dev/mem) and SELinux/AppArmor policies to prevent unauthorized reads.
- Enable kernel parameters like lockdown=confidentiality to block /dev/mem access even by root.
- Monitor for anomalous memory access via auditd rules (e.g., watch opens of /dev/mem) or tools like Sysdig for process behavior.
- Implement full-disk encryption and secure memory handling (e.g., via grsecurity patches) to minimize plaintext credential storage.
- Use endpoint detection tools to flag executions of strings or grep against memory devices.

## Objectives

1. Identify and extract potential password strings from system memory.
2. Recover credentials for privilege escalation or lateral movement.
3. Validate the presence of sensitive data in volatile memory without persistent artifacts.

## Instructions

### Step 1: Verify Access to Memory Device

**Context**: Ensure elevated privileges and check if /dev/mem is accessible, as modern kernels may restrict it. This prevents execution errors and confirms the environment supports memory dumping.

Run a permission check:

```bash
ls -l /dev/mem
```

> This command lists permissions; expect crw-r----- (readable by root). If inaccessible, escalate privileges first. Expected output: device file details confirming root read access.

### Step 2: Dump and Filter Memory Strings for Password Indicators

**Context**: Extract printable ASCII strings from memory and search for common password-related patterns. The -n10 flag limits strings to at least 10 characters to reduce noise from short fragments.

**Command** ([[commands/strings-grep-search-memory-for-passwords]]):

```bash
strings /dev/mem -n 10 | grep -i pass
```

> This searches for case-insensitive matches to 'pass', which often appears in password fields (e.g., 'password123'). It may return partial credentials like 'pass:secretkey'. Review output manually for context, as false positives (e.g., 'password' in configs) are common. Expected output: Lines containing potential passwords, such as '/etc/passwd' references or actual credential strings. If no output, try broader patterns like grep -i 'pass|key|cred' or target /proc/kcore for user-space memory.

### Step 3: Analyze and Extract Valid Credentials

**Context**: Post-process the filtered output to identify usable credentials, such as by correlating with known users or testing in a controlled manner. This step verifies the extracted data's utility.

Save output to a file for review:

```bash
strings /dev/mem -n 10 | grep -i pass > memory_passwords.txt
cat memory_passwords.txt
```

> Inspect the file for plaintext passwords, tokens, or hashes. Test extracted creds against sudo, SSH, or su for validation. Expected output: A text file with candidate strings; success if any yield access (e.g., sudo -l shows new privileges).
