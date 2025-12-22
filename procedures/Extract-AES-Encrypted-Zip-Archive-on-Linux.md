---
id: bb16420e-3fc1-4448-a118-3ff8b9fcca1a
name: Extract-AES-Encrypted-Zip-Archive-on-Linux
type: procedure
verified: true
submitted: true
created_at: '2019-12-13T22:09:49.776883+00:00'
updated_at: '2023-05-26T00:53:12.917123+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Local System]]'
sub_techniques: []
tags:
  - extract
commands:
  - '[[commands/7z-extract-password-protected-zip]]'
platforms:
  - Linux
tools: []
validated: true
---

# Extract-AES-Encrypted-Zip-Archive-on-Linux

## Summary

This procedure allows extraction of AES-encrypted ZIP archives on Linux systems using 7-Zip, as the standard 'unzip' utility does not support AES encryption and fails with an 'unsupported compression method 99' error. It is useful in post-exploitation scenarios where attackers need to access password-protected archives containing sensitive data, such as stolen files or configuration backups.

## Description

AES-encrypted ZIP files are commonly used to secure data, but Linux's native 'unzip' tool lacks support for this encryption method introduced in ZIP version 2.0. Instead, 7-Zip (p7zip on Linux) provides full compatibility for extracting these archives, including handling password prompts interactively or via command-line options. This technique is relevant in data collection phases of an attack, where an attacker has obtained an encrypted archive from a compromised system and needs to decrypt it offline or on a controlled machine. The process requires installation of p7zip-full on Debian-based systems and assumes the attacker knows the password.

## Requirements

1. A Debian-based Linux distribution (e.g., Ubuntu, Kali) with administrative privileges (sudo access).
2. Internet access for package installation.
3. The target AES-encrypted ZIP file available locally.
4. Knowledge of the archive's password.

## Defense

- Implement file access controls and monitor for unauthorized extraction tools like 7-Zip on endpoints.
- Use full-disk encryption and strong password policies for archives to limit offline cracking attempts.
- Enable logging of package installations (e.g., via apt logs) and process execution (e.g., auditd) to detect suspicious 7-Zip usage.

## Objectives

1. Install the 7-Zip package to enable AES ZIP extraction.
2. Extract the contents of the encrypted archive using the provided password.
3. Verify successful extraction to access the contained data.

## Instructions

### Step 1: Install p7zip-full Package

**Context**: The p7zip-full package provides the 7z command-line tool necessary for handling AES-encrypted ZIP files. This step updates the package list and installs the tool, requiring sudo privileges.

```bash
apt update && apt install p7zip-full -y
```

> This command refreshes the apt cache and installs p7zip-full. Expected output includes progress messages from apt, ending with 'p7zip-full is already the newest version' if previously installed, or confirmation of installation.

### Step 2: Extract the AES-Encrypted ZIP Archive

**Context**: Use the 7z tool to decompress the archive. The tool will prompt for the password interactively, supporting AES decryption without issues.

**Command** ([[commands/7z-extract-password-protected-zip]]):
```bash
7z x $_FILENAME.zip
```

> Run this in the directory containing the ZIP file. It scans the archive, prompts for the password (not echoed for security), and extracts contents to the current directory. If the password is correct, files are extracted successfully; otherwise, it reports an error like 'Wrong password.'
