---
id: 5ece34e3-610e-4fbb-9cde-5f783e1863ee
name: Linux-Timestomping-Evasion
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.824412+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Timestomp|T1099 - Timestomp]]'
sub_techniques: []
tags:
  - linux-evasion
  - timestomping
commands:
  - '[[commands/touch-create-empty-file]]'
  - '[[commands/touch-set-atime-mtime-yyyymmddhhmm]]'
  - '[[commands/touch-set-atime-mtime-epoch]]'
  - '[[commands/touch-copy-atime-mtime-from-file]]'
  - '[[commands/stat-get-mtime-modify-file-restore-timestamp]]'
  - '[[commands/date-set-system-time-touch-restore]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Timestomping-Evasion

## Summary

This procedure demonstrates how to manipulate file timestamps on a Linux system using the `touch` and `date` commands to evade detection by security tools that rely on file metadata for timeline analysis. By altering access time (atime), modification time (mtime), and change time (ctime), attackers can make malicious files appear as if they were created or modified at benign times, hiding their activities during post-exploitation or persistence phases.

## Description

Timestomping on Linux involves modifying the standard Unix file timestamps—atime (last access), mtime (last modification), and ctime (last status change)—to obscure the true timeline of file operations. This is particularly useful in defense evasion scenarios where forensic tools or intrusion detection systems (IDS) use timestamps to correlate events. The technique leverages built-in utilities like `touch` for direct timestamp manipulation and `date` for system-wide time changes, requiring appropriate permissions (often root for system time). It applies to scenarios like dropping backdoors, modifying logs, or planting payloads while mimicking legitimate file activity. Success depends on the attacker's ability to restore original timestamps or align them with system norms to avoid anomalies.

## Requirements

1. Shell access to a Linux system (local or remote via SSH).
2. Write permissions on target files and directories; root privileges for system time changes.
3. Basic knowledge of Unix timestamps and the `stat` command for verification.
4. No additional tools required, as it uses coreutils (`touch`, `date`, `stat`).

## Defense

- Enable file integrity monitoring (FIM) tools like Auditd or OSSEC to log timestamp changes.
- Use immutable file attributes (chattr +i) on critical files to prevent modifications.
- Monitor system time changes via NTP synchronization logs and kernel logs (e.g., /var/log/secure).
- Implement anomaly detection on file metadata using tools like Tripwire or forensic analysis with `ls -l` and `stat`.

## Objectives

1. Alter file timestamps to match legitimate activity patterns, evading timeline-based detection.
2. Preserve operational stealth during file creation, modification, or backdoor deployment.
3. Restore original timestamps after modifications to avoid post-incident discovery.

## Instructions

### Step 1: Create an Empty File for Testing

**Context**: Begin by creating a test file using `touch` to establish a baseline timestamp. This step verifies access and sets up a file for subsequent timestomping experiments. If the file exists, `touch` will update its timestamps to the current time without altering content.

**Command** ([[commands/touch-create-empty-file]]):
```bash
touch $_FILE_NAME
```

> This command creates an empty file or updates the timestamps of an existing one. Replace `$_FILE_NAME` with the desired filename (e.g., "example"). Expected output: No stdout if successful; verify with `ls -l $_FILE_NAME` showing current timestamps.

### Step 2: Set Timestamps Using YYYYMMDDhhmm Format

**Context**: Modify atime and mtime to a specific past or future date in YYYYMMDDhhmm format. This is useful for aligning file activity with known benign events, such as aligning a payload's mtime to a system update time.

**Command** ([[commands/touch-set-atime-mtime-yyyymmddhhmm]]):
```bash
touch -a -m -t $_TIMESTAMP $_FILE_NAME
```

> The `-a` flag updates atime, `-m` updates mtime, and `-t` specifies the time. Use a timestamp like `202210312359` for October 31, 2022, 23:59. No output on success; confirm with `stat $_FILE_NAME` showing updated times.

### Step 3: Set Timestamps Using Unix Epoch

**Context**: Use an epoch timestamp (seconds since 1970-01-01) for precise control, ideal when exact Unix time values are needed from logs or scripts. This avoids format errors in date strings.

**Command** ([[commands/touch-set-atime-mtime-epoch]]):
```bash
touch -a -m -d @$_EPOCH_TIMESTAMP $_FILE_NAME
```

> Prefix the epoch value with `@` (e.g., `@1667275140`). No output; verify timestamps match the intended epoch using `stat --format="%Y" $_FILE_NAME`.

### Step 4: Copy Timestamps from Reference File

**Context**: Duplicate timestamps from a legitimate file (e.g., a system binary) to a malicious one, blending it into the environment. This is effective for persistence where the payload mimics an existing file's age.

**Command** ([[commands/touch-copy-atime-mtime-from-file]]):
```bash
touch -a -m -r $_REFERENCE_FILE $_TARGET_FILE
```

> Copies atime and mtime from `$_REFERENCE_FILE` to `$_TARGET_FILE`. Silent on success; use `ls -l` on both to confirm matching timestamps.

### Step 5: Capture, Modify, and Restore Timestamp

**Context**: For subtle modifications (e.g., injecting code into a file), first capture the original mtime with `stat`, perform the change, then restore to avoid detection. This maintains the file's apparent integrity.

**Command** ([[commands/stat-get-mtime-modify-file-restore-timestamp]]):
```bash
MODIFIED_TS=$(stat --format="%Y" $_FILE_NAME)
echo "$_PAYLOAD" >> $_FILE_NAME
touch -a -m -d @$MODIFIED_TS $_FILE_NAME
```

> Stores mtime in a variable, appends payload (e.g., "backdoor"), then restores. Variable output from `echo`; post-execution `stat` should show original mtime.

### Step 6: Timestomp by Temporarily Changing System Time

**Context**: For root-level evasion, alter the system clock to create files with historical timestamps, then revert. Use cautiously as it affects all processes; suitable for isolated environments.

**Code** ([[codes/bash-timestomp-by-changing-system-time]]):

> This code temporarily sets the system time, touches the file, and restores the original time. Requires root. No direct output; verify with `date` before/after and `stat` on the file.

**Command** ([[commands/date-set-system-time-touch-restore]]):
```bash
ORIG_TIME=$(date)
date -s "$_TARGET_DATE"
touch -a -m $_FILE_NAME
date -s "$ORIG_TIME"
```

> Sets time to `$_TARGET_DATE` (e.g., "2022-10-31 23:59:59"), touches file, restores. System-wide change; logs may capture this.
