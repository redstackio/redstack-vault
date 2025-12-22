---
id: 13f59ced-51e6-4054-8f70-7a6a0e3ada17
name: hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.756151+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Hide Artifacts|T1564 - Hide Artifacts]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques:
  - >-
    [[sub-techniques/Hidden Files and Directories|T1564.001 - Hidden Files and
    Directories]]
tags:
  - '[[tags/Hiding Text]]'
  - '[[tags/Linux - Evasion]]'
commands:
  - '[[commands/display-file-contents-cat]]'
  - '[[commands/preview-first-lines-head]]'
  - '[[commands/view-last-lines-tail]]'
  - '[[commands/open-file-vim]]'
  - '[[commands/create-new-file-nano]]'
  - '[[commands/open-existing-file-nano]]'
  - '[[commands/save-changes-nano]]'
  - '[[commands/exit-nano]]'
platforms:
  - Linux
tools: []
validated: true
---

# Hide Artifacts Using Hidden Files and Obfuscated Scripts on Linux

## Summary

This procedure demonstrates how to use Linux text editors and commands to create, edit, and hide files containing malicious payloads or sensitive information. By leveraging hidden files (prefixed with a dot) and obfuscated Bash scripts, attackers can evade detection while maintaining persistence on a compromised Linux system.

## Description

On a compromised Linux system, attackers often need to store payloads, configuration files, or scripts without drawing attention from defenders or automated tools. This involves creating files with editors like Nano, Vim, or Emacs, viewing their contents with commands like cat, head, and tail, and hiding them by prefixing filenames with a dot (e.g., .hidden_payload.sh), which makes them invisible in standard ls listings unless explicitly shown with ls -a. Additionally, obfuscation techniques, such as embedding payloads in scripts with misleading comments and clear commands, can further conceal intent. This approach maps to defense evasion tactics, allowing attackers to hide artifacts in user directories or temporary locations. The target environment is any Linux distribution with standard shell access, and success enables persistent storage of malicious content without immediate detection.

## Requirements

1. Shell access to a Linux system (local or remote via SSH).
2. Basic knowledge of Bash commands and text editors.
3. Installed editors: nano, vim, or emacs (typically pre-installed on most distributions).
4. Permissions to create and write files in the current directory or user home.

## Defense

- Implement strict file permissions and access controls to prevent unauthorized file creation in sensitive directories.
- Regularly monitor system logs (e.g., via auditd) and file integrity (e.g., using Tripwire or AIDE) to detect suspicious file changes or hidden files.
- Use security tools like ClamAV or YARA rules to scan for obfuscated scripts and unusual Bash executions; enable process monitoring with tools like Sysdig or Falco to flag anomalous editor usage or script executions.

## Objectives

1. Create and edit files containing payloads or sensitive data without detection.
2. Hide files using dot-prefixing to evade casual inspection.
3. Obfuscate scripts to disguise malicious commands as benign configurations.
4. Verify file contents and modifications securely.

## Instructions

### Step 1: View File Contents with Cat

**Context**: Use cat to display the full contents of a file, useful for quickly verifying a payload or script after creation. This step helps confirm that hidden or obfuscated content is correctly placed.

**Command** ([[commands/display-file-contents-cat]]):
```bash
cat $_FILE
```

> The cat command concatenates and outputs the file contents to stdout. Replace $_FILE with the path to your target file (e.g., .hidden_payload.sh). If the file contains sensitive data, pipe output to a pager like less for controlled viewing. Expected output is the raw file contents; success is indicated by no errors and visible payload text.

### Step 2: Preview First Lines with Head

**Context**: Use head to inspect the beginning of a file without loading the entire content, ideal for checking script headers or initial payload setup in large files.

**Command** ([[commands/preview-first-lines-head]]):
```bash
head -n $_LINES $_FILE
```

> This prints the first $_LINES (default 10) of $_FILE. Use -n 5 for fewer lines if needed. Expected output shows the initial lines; success if the header matches expected obfuscation (e.g., comments).

### Step 3: View Last Lines with Tail

**Context**: Tail allows inspection of the end of a file, helpful for verifying the payload command at the bottom of an obfuscated script.

**Command** ([[commands/view-last-lines-tail]]):
```bash
tail -n $_LINES $_FILE
```

> Displays the last $_LINES (default 10) of $_FILE. Use -f for real-time monitoring if the file is being appended. Expected output reveals the final lines; success if the payload is intact.

### Step 4: Create or Open a New Hidden File with Nano

**Context**: Nano is a simple editor for creating hidden files. Prefix the filename with . to hide it immediately upon creation.

**Command** ([[commands/create-new-file-nano]]):
```bash
nano .$_FILENAME
```

> Launches nano to create/edit .$_FILENAME (e.g., .payload.sh). Enter your payload content, then save and exit. Expected: Editor opens with empty buffer; success if file is created and hidden (ls won't show it without -a).

### Step 5: Open an Existing Hidden File with Nano

**Context**: Edit an existing hidden file to insert or modify the payload without exposing it.

**Command** ([[commands/open-existing-file-nano]]):
```bash
nano .$_FILENAME
```

> Opens the hidden file in nano for editing. Make changes to embed obfuscated content. Expected: File contents load; success if modifications are saved without errors.

### Step 6: Save Changes in Nano

**Context**: After editing, save the file to persist the hidden payload.

**Command** ([[commands/save-changes-nano]]):
```bash
# In nano: Press Ctrl+O, then Enter to confirm filename
```

> This writes changes to disk. Expected: Prompt confirms save; success if file size updates (check with ls -la).

### Step 7: Exit Nano

**Context**: Close the editor after saving to return to the shell.

**Command** ([[commands/exit-nano]]):
```bash
# In nano: Press Ctrl+X
```

> Exits nano, prompting to save if unsaved. Expected: Return to shell prompt; success if no pending changes lost.

### Step 8: Open a File in Vim for Advanced Editing

**Context**: Use Vim for more complex editing of hidden scripts, such as inserting obfuscation comments.

**Command** ([[commands/open-file-vim]]):
```bash
vim .$_FILENAME
```

> Opens the hidden file in Vim. Use i to insert, Esc :wq to save and quit. Expected: Vim interface loads; success if edits are applied and file remains hidden.

### Step 9: Create an Obfuscated Bash Script with Payload

**Context**: Build a script that hides a payload behind clear and fake comments, making it appear benign when casually viewed.

**Command** ([[commands/create-obfuscated-bash-script]]):
```bash
echo "sneaky-payload-command" > script.sh
echo "# $(clear)" >> script.sh
echo "# Do not remove. Generated from /etc/issue.conf by configure." >> script.sh
```

> This creates script.sh with a payload line, followed by a clear command (which clears the terminal on execution) and a misleading comment. To hide, rename to .script.sh. Expected output when cat script.sh: Only the comment visible after clear; success if payload executes on bash script.sh but looks innocent.
