---
id: 4a3b411f-5dea-4345-b01d-1e3db63c8991
name: Directory-Traversal-using-Dotdotpwn
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.754072+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - directory-traversal
  - file-discovery
  - dotdotpwn
commands:
  - '[[commands/git-clone-dotdotpwn-repository]]'
  - '[[commands/dotdotpwn-directory-traversal-exploit]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/dotdotpwn]]'
validated: true
---

# Directory-Traversal-using-Dotdotpwn

## Summary

This procedure demonstrates how to use the Dotdotpwn tool to automate directory traversal attacks, allowing attackers to access and read files outside the web root or intended directory structure on vulnerable servers. It is particularly useful for discovering and extracting sensitive files like /etc/shadow on Linux systems via protocols such as FTP or HTTP, serving as a key technique in reconnaissance and initial access phases.

## Description

Directory traversal, also known as path traversal, exploits insufficient input validation in applications to navigate the file system beyond restricted directories. Dotdotpwn is a Perl-based tool that automates the fuzzing of directory traversal payloads (e.g., ../ sequences) across various protocols, making it efficient for testing multiple depths and variations. This procedure targets vulnerable FTP or HTTP services, using /etc/shadow as an example target file for password hash extraction. It assumes the attacker has network access to the target and identifies a vulnerable endpoint during reconnaissance. Success enables reading arbitrary files, potentially leading to credential theft or further exploitation.

## Requirements

1. Network access to a target host running a vulnerable FTP or HTTP service that allows directory traversal.
2. Dotdotpwn tool installed on the attacker's machine (via git clone from GitHub).
3. Perl interpreter available on the attacker's system.
4. Knowledge of the target IP and protocol (e.g., FTP on port 21).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to block traversal sequences like ../ in user-supplied paths.
- Enforce access controls and chroot jails to restrict file system access for services like FTP/HTTP.
- Deploy web application firewalls (WAFs) or intrusion detection systems (IDS) to monitor and block anomalous traversal attempts.
- Regularly audit server logs for unusual file access patterns and enable logging for failed directory navigations.

## Objectives

1. Automate the traversal of directories to bypass access restrictions.
2. Read sensitive files outside the intended root, such as configuration files or password stores.
3. Extract usable data like password hashes for offline cracking or further attacks.

## Instructions

### Step 1: Install Dotdotpwn Tool

**Context**: Clone the Dotdotpwn repository to obtain the tool, as it is not available via standard package managers. This sets up the Perl script for execution.

**Command** ([[commands/git-clone-dotdotpwn-repository]]):
```bash
git clone https://github.com/wireghoul/dotdotpwn
```

> This command downloads the tool to the current directory. Navigate into the cloned directory if needed (cd dotdotpwn). Expected output includes progress messages ending with 'Cloning into 'dotdotpwn'...'. Verify by listing files and confirming dotdotpwn.pl exists.

### Step 2: Execute Directory Traversal Attack

**Context**: Run Dotdotpwn against the target to fuzz traversal payloads and attempt to read a sensitive file. Adjust parameters based on the protocol and target file; here, we target /etc/shadow via FTP as an example for Linux systems.

**Command** ([[commands/dotdotpwn-directory-traversal-exploit]]):
```bash
perl dotdotpwn.pl -h $_TARGET_IP -m $_PROTOCOL -t $_TIMEOUT -f $_TARGET_FILE -s -q -b
```

> Replace placeholders: $_TARGET_IP with the target's IP (e.g., 10.10.10.10), $_PROTOCOL with 'ftp' or 'http', $_TIMEOUT with seconds (e.g., 300), $_TARGET_FILE with the desired file (e.g., /etc/shadow). The -s enables SSL if applicable, -q quiets non-essential output, and -b runs in batch mode for automation. Expected output includes successful file contents if traversal succeeds, such as hashed passwords from /etc/shadow. If no output, increase timeout or try different depths with -d flag (not used here).
