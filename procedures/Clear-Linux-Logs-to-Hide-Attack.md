---
id: 8d872b76-6a70-43c1-9bde-f73005534fb5
name: Clear-Linux-Logs-to-Hide-Attack
type: procedure
verified: true
submitted: true
created_at: '2019-10-31T21:16:30.160944+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques: []
tags:
  - audit
  - incident-response
  - operating-systems
commands:
  - '[[commands/clear-bash-history-files]]'
  - '[[commands/clear-auth-log-files]]'
platforms:
  - Linux
tools: []
validated: true
---

# Clear-Linux-Logs-to-Hide-Attack

## Summary

This procedure outlines how to securely erase common Linux log files, such as user bash history and authentication logs, to remove indicators of compromise after gaining access to a system. It uses shredding and overwriting techniques to minimize forensic recovery, though it warns that such actions can trigger monitoring alerts in SIEM systems.

## Description

In post-exploitation scenarios on Linux systems, attackers often need to cover their tracks by clearing logs that record commands executed or authentication attempts. This procedure targets key files like .bash_history in user home directories and /var/log/auth.log, using the shred utility to overwrite data multiple times before truncating the file. This approach aligns with defense evasion tactics but carries the risk of detection, as log clearing is a common indicator monitored by security tools. It assumes root or sufficient privileges to access and modify these files across the system.

## Requirements

1. Root or sudo access to the target Linux system to modify protected log files.
2. Availability of the coreutils package (includes shred and find, standard on most distributions).
3. Basic familiarity with bash scripting for executing the clearing commands.
4. Awareness of potential monitoring: This action may log the shred or truncate operations themselves in auditd or other logs.

## Defense

Defensive measures and detection strategies:

- Enable file integrity monitoring (e.g., via auditd or OSSEC) to detect modifications to log files.
- Configure SIEM rules to alert on shred, truncate (> or cat /dev/null), or find commands targeting log directories.
- Use immutable log files (e.g., via chattr +i) or remote syslog forwarding to prevent local tampering.
- Monitor for anomalous process behavior, such as shred running on /var/log or /home directories.

## Objectives

1. Remove evidence of executed commands from user histories to hide attacker activity.
2. Erase authentication logs to conceal login attempts or privilege escalations.
3. Minimize data recovery potential through secure overwriting.
4. Achieve this with minimal residual indicators, though accepting the risk of meta-logging.

## Instructions

### Step 1: Clear Bash History Files

**Context**: This step securely erases .bash_history files for all users in /home and /root directories. These files store command history and can reveal attacker actions; shredding overwrites the data before truncation to hinder recovery.

**Command** ([[commands/clear-bash-history-files]]):
```bash
for FILE in $(find /home /root -name '.bash_history' 2>/dev/null); do shred -z $FILE; cat /dev/null > $FILE; done
```

> This command locates all .bash_history files, shreds them (overwriting with zeros after random passes), and then truncates them to empty. Run as root to access all files. Expected output is minimal (no stdout unless errors); verify by checking file sizes with ls -la /home/*/.bash_history (should be 0 bytes) or cat (should be empty).

### Step 2: Clear Authentication Log Files

**Context**: This step targets auth.log files in /var/log, which record login attempts, sudo usage, and authentication events. Clearing them hides evidence of unauthorized access; the same shred-and-truncate method is used for security.

**Command** ([[commands/clear-auth-log-files]]):
```bash
for FILE in $(find /var/log -name "auth.log" 2>/dev/null); do shred -z $FILE; cat /dev/null > $FILE; done
```

> This locates and securely erases all auth.log files (handles rotations like auth.log.1). Run as root. Expected output is silent on success; verify with ls -la /var/log/auth* (files should be 0 bytes) and tail /var/log/auth.log (should show no recent entries). Note: Rotated logs may need separate handling if not caught by the find.
