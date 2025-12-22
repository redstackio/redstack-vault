---
id: 2428aafb-34e6-4be7-9840-05b2f645c151
name: Creating-Files-with-Zero-Width-Spaces
type: procedure
verified: true
submitted: true
created_at: '2020-01-23T22:06:49.225853+00:00'
updated_at: '2023-05-25T20:21:20.144028+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Obfuscation]]'
commands: []
platforms:
  - Linux
tools: []
validated: true
---

# Creating-Files-with-Zero-Width-Spaces

## Summary

This procedure demonstrates how to create files and directories on Linux systems using zero-width spaces (Unicode U+200B) embedded in filenames. These non-printing characters make files visually indistinguishable from legitimate ones, enabling attackers to obfuscate malicious artifacts, confuse defenders during incident response, or hide payloads in shared environments.

## Description

Zero-width spaces are invisible Unicode characters typically used for formatting in text processors to indicate word boundaries without adding visible space. In offensive security contexts, attackers leverage them to craft filenames that appear identical to existing files when viewed in file explorers or terminals without Unicode-aware rendering. For instance, a file named "index.html" and another named "i​ndex.html" (with a zero-width space between "i" and "n") will display the same visually but have different actual names, leading to confusion in file management, backups, or forensic analysis. This technique is particularly useful in post-exploitation scenarios for persistence or command and control, where hiding files in plain sight evades basic detection. It works on Linux filesystems that support Unicode filenames (e.g., ext4) and can be applied to files, directories, or paths in web server configurations, though not directly in domain names.

## Requirements

1. Access to a Linux terminal or shell environment (local or remote).
2. Knowledge of Unicode input methods, such as Ctrl+Shift+U in GNOME Terminal or similar emulators.
3. Sufficient permissions to create files in the target directory (e.g., user-level write access).
4. A terminal that supports Unicode input; most modern Linux distributions (Ubuntu, Kali) do by default.

## Defense

Defensive measures and detection strategies:

- Use tools like `ls --color=never` or `exa` to reveal hidden characters in filenames.
- Implement filesystem monitoring with tools like Auditd to log file creation events and inspect names for non-ASCII characters.
- Employ hex editors or `hexdump` on filenames to detect embedded Unicode control characters.
- Configure file explorers (e.g., Nautilus) to display raw bytes or use `find` with regex to identify suspicious names.

## Objectives

1. Create obfuscated files that blend visually with legitimate ones to evade casual inspection.
2. Demonstrate persistence by hiding malicious scripts or payloads in accessible directories.
3. Enable confusion in defender workflows during incident response or cleanup.

## Instructions

### Step 1: Prepare the Terminal for Unicode Input

**Context**: Ensure your terminal supports direct Unicode entry, which is standard in most Linux environments. This step verifies the setup before creating the file.

Test by opening a terminal and attempting to input a known Unicode character, such as U+00A9 (©). Press Ctrl+Shift+U, type 'a9', then Enter. If it appears correctly, proceed.

**Expected Output**: The copyright symbol © displays in the terminal or a text editor.

### Step 2: Create the File with Embedded Zero-Width Space

**Context**: Use the `touch` command combined with Unicode input to create a file with a zero-width space. The zero-width space is Unicode U+200B, which is invisible and does not affect visual rendering but alters the filename's byte representation.

**Code** ([[codes/Create-File-With-Zero-Width-Space-Bash]]):

```bash
touch i[CTRL + SHIFT + U]200b[ENTER]ndex.html
```

> This command creates a file named "i​ndex.html" (with U+200B between "i" and "n"). The [CTRL + SHIFT + U]200b[ENTER] sequence inputs the zero-width space directly. Replace the filename as needed for files, directories (use `mkdir` instead of `touch`), or paths.

**Expected Output**: The file is created without errors. Running `ls` will show "index.html" and "i​ndex.html" appearing identical, but `ls -b` (escape sequences) or `hexdump -C filename` will reveal the difference (e.g., e2 80 8b for U+200B).

### Step 3: Verify the Obfuscation

**Context**: Confirm the files are distinct by interacting with them separately, ensuring the technique works as intended for evasion.

Use `ls` to list files, then attempt to interact with each (e.g., `cat index.html` vs. `cat i​ndex.html`). To input the obfuscated name again, repeat the Unicode sequence.

**Expected Output**: Both files list as "index.html" visually, but commands target different files, and tools like `diff` or `cmp` show they are distinct.

### Step 4: Apply to Directories or Paths

**Context**: Extend the technique to directories for broader obfuscation, such as hiding a staging folder.

Adapt the code for `mkdir`: `mkdir dir[CTRL + SHIFT + U]200b[ENTER]ectory`. Use in paths like web roots (e.g., `/var/www/html/i​ndex.html`).

**Expected Output**: Directory created invisibly distinct from "directory", verifiable via `ls -la` or filesystem dumps.
