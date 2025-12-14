---
tags:
  - setup
  - symlink
  - race-condition
type: procedure
tools:
  - '[[tools/rename-custom-swapper]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ln-symlink]]'
  - '[[commands/mkdir-directory]]'
  - '[[commands/gcc-compile-rename]]'
platforms:
  - Linux
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: eacd1378-01aa-44a1-8a30-aeea0641f7c5
created_at: '2025-12-14T17:24:22.198Z'
updated_at: '2025-12-14T17:24:22.198Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-Environment-for-libcurl-Race

## Summary

This procedure sets up the filesystem environment by creating a symlink to a protected victim file, an attacker-owned directory, and compiling a custom rename tool to enable the TOCTOU race in libcurl.

## Description

In the attack scenario, the attacker prepares files in a shared directory: a symlink 'a' pointing to a root-owned 'flag' file (simulating /etc/passwd), a directory 'b', and compiles rename.c from the provided source. This setup allows the stat() call in Curl_fopen to see a directory while fopen() follows the symlink, leading to overwrites. Prerequisites include local access and a vulnerable libcurl version (7.84.0-8.1.2). Expected outcome: Race-ready environment without alerting the victim.

## Requirements

1. Local shell access on Linux system
2. Permissions to create symlinks and directories in target path
3. Source code for rename.c (from https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c)
4. GCC compiler installed

## Defense

Defensive measures and detection strategies:

- Use file system monitoring tools like auditd to log symlink and directory creations
- Enforce strict file permissions and avoid shared writable directories for privileged processes
- Update libcurl to patched versions beyond 8.1.2

## Objectives

1. Create manipulable files for race exploitation
2. Compile tool for atomic swaps
3. Position for victim-triggered curl execution

## Instructions

### Step 1: Create Symlink to Protected File

**Context**: Link 'a' to victim-owned 'flag' to target for overwrite.

**Command** ([[commands/ln-symlink]]):
```bash
ln -s flag a
```

> Creates symbolic link 'a' pointing to 'flag'. Expected output: lrwxrwxrwx 1 user group 4 Oct 1 12:00 a -> flag.

### Step 2: Create Attacker Directory

**Context**: 'b' as directory to swap with symlink, appearing non-regular to stat().

**Command** ([[commands/mkdir-directory]]):
```bash
mkdir b
```

> Creates empty directory 'b'. Expected output: drwxrwxrwx 2 user group 4096 Oct 1 12:00 b.

### Step 3: Compile Rename Tool

**Context**: Build custom C program for atomic file swaps using renameat2.

**Command** ([[commands/gcc-compile-rename]]):
```bash
gcc rename.c -o rename
```

> Compiles source into executable. Expected output: No errors, -rwxr-x--- 1 user group 16k Oct 1 12:00 rename.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts (local access for setup)

### Sub-Techniques


## Commands Used

- [[commands/ln-symlink]]
- [[commands/mkdir-directory]]
- [[commands/gcc-compile-rename]]

## Tools Used

- [[tools/rename-custom-swapper]]

## Tags

- [[setup]]
- [[symlink]]
- [[race-condition]]
