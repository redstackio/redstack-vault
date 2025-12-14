---
tags:
  - setup
  - symlink
  - toctou
type: procedure
tools:
  - '[[tools/rename-custom]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/ls-long]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:24:19.254Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b1f30255-4387-4378-a9a5-c6bdee2a79eb
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Prepare-Environment-for-libcurl-Race-Condition

## Summary

This procedure sets up the file system environment required for exploiting the libcurl TOCTOU race condition, including creating a symlink to a target file, a directory for swapping, and compiling the custom rename tool. It supports two scenarios: overwriting a protected file owned by the victim (e.g., root) or leaking data to an attacker-controlled file.

## Description

In the attack scenario, the attacker prepares files in a shared directory accessible to the victim process (curl). A symlink 'a' points to 'flag' (victim-owned for overwrite or attacker-owned with 0666 perms for leakage). A directory 'b' is created for swapping. The custom rename tool is compiled from source to enable atomic swaps. This setup exploits the lack of synchronization in libcurl's Curl_fopen, where stat() sees 'a' as a directory (non-regular file), leading to direct fopen('a', 'w') that follows the swapped symlink. Prerequisites include local access and a vulnerable libcurl version (7.84.0-8.1.2). Expected outcome: Environment ready for race exploitation without triggering alerts.

## Requirements

1. Local file system write access to the target directory
2. GCC compiler for building the rename tool
3. Vulnerable libcurl installed (check with curl --version)
4. Target file 'flag' created (e.g., echo "secret" > flag; chown root flag for scenario A)

## Defense

Defensive measures and detection strategies:

- Use file system namespaces or AppArmor/SELinux to restrict symlink following
- Monitor for rapid file renames/swaps in sensitive directories (e.g., via auditd)
- Patch libcurl to version 8.3.0+ where O_PATH and openat() fix the race

## Objectives

1. Establish symlink and directory for TOCTOU window
2. Compile tool for atomic operations
3. Verify setup without alerting defenses
4. Prepare for both overwrite and leakage scenarios

## Instructions

### Step 1: Create Symlink and Directory

**Context**: Set up 'a' as symlink to 'flag' and 'b' as empty directory.

**Command** ([[commands/ln-symlink]]):
```bash
ln -s flag a
mkdir b
```

> Creates 'a -> flag' and directory 'b'. For scenario B, ensure 'flag' is attacker-owned with chmod 0666 flag.

### Step 2: Compile Rename Tool

**Context**: Build the custom C program for atomic swaps using renameat2.

**Command** ([[commands/gcc-compile]]):
```bash
gcc -o rename rename.c
```

> Compiles rename.c (from https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c) into executable 'rename'. Expected output: No errors, binary created.

### Step 3: Verify Setup

**Context**: Confirm files and ownership.

**Command** ([[commands/ls-long]]):
```bash
ls -l
```

> Lists contents; expected: lrwxrwxrwx 1 user user 4 ... a -> flag; drwxr-xr-x 2 user user 4096 ... b; -rw-r--r-- 1 root root 6 ... flag.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/ln-symlink]]
- [[commands/mkdir-directory]]
- [[commands/gcc-compile]]
- [[commands/ls-long]]

## Tools Used

- [[tools/rename-custom]]

## Tags

- setup
- symlink
- compilation
