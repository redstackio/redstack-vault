---
id: a7e8187c-4d55-4a13-a753-f099bdd50ac2
name: Linux-Command-History-Evasion
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.677770+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Indicator-Removal-on-Host|T1070 - Indicator Removal on Host]]'
sub_techniques:
  - '[[sub-techniques/File-Deletion|T1070.004 - File Deletion]]'
tags:
  - '[[tags/Command-History]]'
  - '[[tags/Linux-Evasion]]'
commands:
  - '[[commands/bash-clear-command-history]]'
  - '[[commands/bash-delete-specific-history-entry]]'
  - '[[commands/bash-disable-history-logging]]'
  - '[[commands/bash-ignore-duplicate-and-specific-commands]]'
  - '[[commands/bash-add-specific-command-to-ignore-list]]'
  - '[[commands/bash-execute-command-with-leading-space]]'
  - '[[commands/bash-remove-pattern-from-histignore]]'
  - '[[commands/bash-remove-most-recent-history-entry]]'
  - '[[commands/bash-set-history-size]]'
  - '[[commands/bash-view-history-file]]'
  - '[[commands/bash-echo-history-file-path]]'
  - '[[commands/bash-display-command-history]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Command-History-Evasion

## Summary

This procedure outlines various techniques to manipulate or disable Bash command history on Linux systems, allowing attackers to evade detection by removing traces of executed commands from logs. It covers viewing, disabling, ignoring specific commands, and clearing history entries, useful in post-exploitation scenarios to maintain stealth during red team engagements or forensic evasion.

## Description

Command history in Linux shells like Bash records previously executed commands in files such as ~/.bash_history, which can be reviewed by investigators or security tools to reconstruct attacker actions. This procedure provides step-by-step methods to view, modify, or eliminate these records, including disabling logging entirely, ignoring patterns or duplicates, executing commands without logging (e.g., via leading spaces), and deleting specific or recent entries. These techniques apply to interactive shell sessions and can be combined for comprehensive evasion. The target environment is any Linux distribution using Bash (default on most systems). Success prevents command traces from persisting across sessions or in memory, reducing the risk of detection via tools like auditd or forensic analysis. Note that some methods require shell access and may not affect other logging mechanisms like syslog.

## Requirements

1. Interactive shell access (local or remote via SSH) on a Linux system using Bash.
2. Basic knowledge of Bash environment variables and history mechanisms.
3. No elevated privileges needed for user-level history, but root may be required for system-wide changes.
4. Optional: Text editor for modifying ~/.bashrc to persist settings across sessions.

## Defense

- Enable comprehensive auditing with tools like auditd to log shell activity beyond history files.
- Monitor for history manipulation commands (e.g., 'history -c', 'unset HISTFILE') via process monitoring or EDR solutions.
- Use immutable logging or remote syslog to prevent local tampering.
- Regularly review and rotate history files, and restrict shell access with tools like rbash.

## Objectives

1. View and understand current command history to identify what needs evasion.
2. Disable or limit history logging to prevent future commands from being recorded.
3. Remove existing history entries to erase traces of prior actions.
4. Execute sensitive commands without leaving artifacts in history.

## Instructions

### Step 1: Display Current Command History

**Context**: Begin by reviewing the current in-memory command history to assess what commands are logged and plan evasion steps. This helps identify sensitive entries for targeted removal.

**Command** ([[commands/bash-display-command-history]]):
```bash
history
```

> The 'history' command lists all commands executed in the current session, numbered for reference. Use this to spot potentially incriminating commands before proceeding to deletion or disabling.

**Expected Output**: A numbered list of commands, e.g.,
```
   1  ls -la
   2  whoami
   3  cat /etc/passwd
```

### Step 2: Echo History File Path

**Context**: Determine the location of the persistent history file to inspect or target it directly for deletion or modification.

**Command** ([[commands/bash-echo-history-file-path]]):
```bash
echo $HISTFILE
```

> This reveals the path to the history file (default ~/.bash_history), allowing manual inspection or deletion if needed.

**Expected Output**: Path to the file, e.g.,
```
/home/user/.bash_history
```

### Step 3: View Persistent History File

**Context**: Examine the on-disk history file to see commands saved from previous sessions, which persist after logout.

**Command** ([[commands/bash-view-history-file]]):
```bash
cat ~/.bash_history
```

> This displays the contents of the history file. Pipe to 'less' for large files: history | less.

**Expected Output**: Unnumbered list of past commands, e.g.,
```
ls -la
whoami
cat /etc/passwd
```

### Step 4: Disable History Logging

**Context**: Prevent any further commands from being saved to history by unsetting the file and zeroing the size, effective for the current session.

**Command** ([[commands/bash-disable-history-logging]]):
```bash
unset HISTFILE
export HISTSIZE=0
```

> Unsetting HISTFILE stops writing to disk, and HISTSIZE=0 clears in-memory history. Add to ~/.bashrc for persistence, but test carefully as it affects all sessions.

**Expected Output**: No output; verify with 'history' showing empty list.

### Step 5: Set History Size Limit

**Context**: Limit the number of commands stored to reduce the history footprint, automatically discarding older entries.

**Command** ([[commands/bash-set-history-size]]):
```bash
export HISTSIZE=100
```

> Replace 100 with desired limit (default 500-1000). This controls in-memory size; pair with HISTFILESIZE for disk.

**Expected Output**: No output; subsequent 'history' shows limited entries.

### Step 6: Ignore Duplicate and Specific Commands

**Context**: Configure Bash to skip logging duplicates or common benign commands, reducing noise while hiding patterns.

**Command** ([[commands/bash-ignore-duplicate-and-specific-commands]]):
```bash
export HISTIGNORE="&:ls:ll:cd:exit"
```

> '&' ignores duplicates; colons separate patterns. Add to ~/.bashrc for persistence. This prevents logging of repeated or listed commands.

**Expected Output**: No output; test by running ignored commands and checking 'history'.

### Step 7: Add Specific Command to Ignore List

**Context**: Dynamically add patterns (e.g., sensitive commands) to HISTIGNORE to exclude them from future logging.

**Command** ([[commands/bash-add-specific-command-to-ignore-list]]):
```bash
export HISTIGNORE="$HISTIGNORE:ls -l"
```

> Appends to existing HISTIGNORE. Use exact or wildcard patterns for matching.

**Expected Output**: No output; verify by executing 'ls -l' and omitting from 'history'.

### Step 8: Execute Command with Leading Space for Evasion

**Context**: Bypass history logging for a single command by prefixing with a space, if HISTCONTROL=ignorespace is set (default in many distros).

**Command** ([[commands/bash-execute-command-with-leading-space]]):
```bash
 my-sneaky-command
```

> The leading space prevents logging. Use for one-off sensitive actions like password entry or tool invocation.

**Expected Output**: Output of the command itself; not present in subsequent 'history'.

### Step 9: Delete Specific History Entry

**Context**: Remove a particular logged command by its index to erase evidence of a mistake or sensitive action.

**Command** ([[commands/bash-delete-specific-history-entry]]):
```bash
history -d 123
```

> Replace 123 with the entry number from 'history'. This shifts subsequent indices; re-run 'history -w' to save changes to disk.

**Expected Output**: No output; the entry is removed from 'history' list.

### Step 10: Remove Most Recent History Entry

**Context**: Quickly erase the last command (and the deletion command itself) to avoid self-logging.

**Command** ([[commands/bash-remove-most-recent-history-entry]]):
```bash
history -d -2 && history -d -1
```

> Deletes the previous command (-2) and this one (-1). Follow with 'history -w' to persist.

**Expected Output**: No output; recent entries gone from 'history'.

### Step 11: Remove Pattern from HISTIGNORE

**Context**: If needed, remove a previously ignored pattern to resume logging certain commands.

**Command** ([[commands/bash-remove-pattern-from-histignore]]):
```bash
HISTIGNORE=${HISTIGNORE%%:"ls -l"*}
export HISTIGNORE
```

> Strips the pattern from HISTIGNORE variable. Rarely used but useful for dynamic control.

**Expected Output**: Updated HISTIGNORE value echoed.

### Step 12: Clear All Command History

**Context**: Completely wipe in-memory and on-disk history as a final evasion step before exfiltration or persistence.

**Command** ([[commands/bash-clear-command-history]]):
```bash
history -c && history -w
```

> '-c' clears memory, '-w' writes empty to disk. This erases all traces for the user.

**Expected Output**: No output; 'history' shows empty list, ~/.bash_history is zero-length.
