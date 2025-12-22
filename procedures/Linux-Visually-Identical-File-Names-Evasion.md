---
type: procedure
description: >-
  Create files with visually identical names using Unicode characters to
  masquerade malicious files as legitimate ones on Linux systems.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Match Legitimate Name or Location]]'
sub_techniques: []
tags:
  - file-names
  - linux-evasion
  - masquerading
commands:
  - '[[commands/touch-create-visually-identical-files]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Visually-Identical-File-Names-Evasion

## Summary

This procedure demonstrates how to create decoy and imposter files on a Linux system using visually identical names by inserting a Unicode zero-width joiner (\u200D) into the filename. This evasion technique tricks visual inspections by system administrators or users, allowing malicious files to blend in with legitimate ones, potentially enabling undetected code execution or persistence.

## Description

In offensive security operations, attackers often need to hide their artifacts to avoid detection during post-exploitation or lateral movement. The Linux-Visually-Identical-File-Names-Evasion technique exploits the reliance on visual file name inspection by creating files that appear identical but differ in their Unicode composition. For example, a legitimate 'index.php' can be mimicked by 'index\u200D.php', where the zero-width joiner is invisible to the eye but distinguishes the files technically. This is particularly useful in environments with limited automated integrity checks, such as shared directories or web servers. The technique maps to MITRE ATT&CK [[Match Legitimate Name or Location]] Masquerading: Match Legitimate Name or Location under the Defense Evasion tactic. It requires shell access and is effective against manual reviews but may be caught by hash-based or entropy-based detection tools.

## Requirements

1. Shell access to a Linux system (local or remote via SSH).
2. Permissions to create files in the target directory (typically write access to the current working directory).
3. Bash shell environment (standard on most Linux distributions).

## Defense

Defensive measures and detection strategies:

- Implement file name validation that checks for Unicode anomalies or non-printable characters using tools like `ls -b` or regex-based scanners.
- Deploy file integrity monitoring (FIM) solutions such as OSSEC or Tripwire to detect unexpected file creations or modifications based on hashes rather than names.
- Enforce least privilege principles to restrict file creation in sensitive directories and use automated auditing with tools like Auditd to log file operations.

## Objectives

1. Create visually indistinguishable files to evade manual detection.
2. Masquerade malicious payloads as legitimate files for persistence or execution.
3. Demonstrate evasion against visual inspection-based security reviews.

## Instructions

### Step 1: Create Decoy and Imposter Files

**Context**: This step uses the `touch` command to generate two files: a legitimate decoy and a visually identical imposter containing a hidden Unicode zero-width joiner. The decoy serves as a reference, while the imposter can host malicious content. Verify the files' distinction using `ls` or `hexdump` to confirm the Unicode difference without visual cues.

**Command** ([[commands/touch-create-visually-identical-files]]):

```bash
# Create the decoy file with a standard name
touch 'index.php'

# Create the imposter file with a visually identical name using Unicode zero-width joiner
touch $'index\u200D.php'
```

> The first command creates a benign empty file named 'index.php'. The second inserts \u200D (zero-width joiner) after 'index', making it appear as 'index.php' visually but technically different. This allows placing malicious code in the imposter file (e.g., via `echo 'malicious content' > $'index\u200D.php'`). Expected output from `ls` will show both files as 'index.php', but `ls -b` or `hexdump -C` reveals the difference (e.g., \u200D as 0xE2 0x80 0x8D). If permissions are insufficient, the command will fail with 'Permission denied'.

**Code** ([[codes/bash-touch-visually-identical-files]]):

> For a reusable snippet with comments, refer to the linked code document, which provides the same functionality with additional explanatory notes.

### Step 2: Verify File Distinction

**Context**: After creation, confirm the files are distinct to ensure the evasion works as intended. This step uses built-in commands to inspect without modifying files, helping validate success before proceeding to payload placement.

**Command**:

```bash
ls -la
ls -b
hexdump -C index.php $'index\u200D.php' 2>/dev/null || echo 'Files created but hexdump may vary'
```

> `ls -la` lists files, showing apparent identical names. `ls -b` escapes non-printable characters, revealing the Unicode in the imposter. `hexdump -C` displays byte-level differences. Success is indicated if both files appear but only the imposter shows extra bytes (e.g., E2 80 8D). If files are not listed separately, check directory permissions or shell escaping.
