---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/System Service Discovery|T1007 - System Service Discovery]]'
platforms:
  - Linux
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Service Attacks]]'
commands:
  - '[[commands/pspy-run-process-monitor]]'
tools:
  - '[[tools/pspy]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Monitor-System-Processes-and-Commands-with-Pspy

## Summary

This procedure uses the pspy tool to monitor and report on system processes and commands executed by various users, including root and system services. It enables discovery of running cron jobs, scheduled tasks, and commands from higher-privilege users without requiring elevated access, aiding in reconnaissance during penetration testing or red team engagements.

## Description

Pspy is a process monitoring utility designed to capture command executions across the system in real-time. By leveraging Linux process monitoring techniques, it bypasses common limitations of tools like 'ps' by directly observing process forks and executions via ptrace or inotify. This is particularly useful in environments where an attacker has limited shell access and needs to identify privilege escalation vectors, such as cron jobs running as root or service restarts. The procedure assumes a Linux target and focuses on static binaries to avoid dependencies. Expected outcomes include a live stream of process activities, which can reveal hidden automations or misconfigurations exploitable for further attacks.

## Requirements

1. Low-privilege shell access to the target Linux system (e.g., via initial foothold like SSH or reverse shell).
2. Ability to download and transfer files to the target (e.g., via wget, curl, or scp).
3. Target architecture knowledge (x86_64, ARM, etc.) to select the correct pspy binary.
4. No root privileges required, but firewall rules allowing outbound connections if downloading on-target.

## Defense

Defensive measures and detection strategies:

- Monitor for unknown binaries in /tmp or user directories using file integrity monitoring tools like AIDE or OSSEC.
- Enable process auditing with auditd to log ptrace and inotify usage, which pspy relies on.
- Implement application whitelisting (e.g., AppArmor or SELinux) to restrict unauthorized process monitoring.
- Regularly review cron logs (/var/log/cron) and system journals (journalctl) for anomalous executions.

## Objectives

1. Capture real-time command executions by all users, including root.
2. Identify potential privilege escalation opportunities from observed processes.
3. Document system behaviors for mapping attack surfaces without alerting defenders.

## Instructions

### Step 1: Download the Appropriate Pspy Binary

**Context**: Select and download the static pspy binary matching the target's architecture to ensure compatibility and avoid compilation dependencies. This step prepares the tool for transfer and execution.

Visit the official GitHub repository and download the pre-built static binary for your target's architecture (e.g., pspy_x86_64).

**Command** ([[commands/pspy-download-binary]]):
```bash
wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 -O /tmp/pspy
```

> This command fetches the x86_64 binary directly to /tmp. Verify the architecture with 'uname -m' on the target first. Expected output is a successful download with HTTP 200 response and file size around 2-3 MB.

### Step 2: Make the Binary Executable and Verify Integrity

**Context**: Ensure the binary is executable and test it briefly to confirm it runs without errors, preventing runtime issues during monitoring.

Transfer the binary if downloaded off-target, then set permissions.

**Command** ([[commands/pspy-make-executable]]):
```bash
chmod +x /tmp/pspy
/tmp/pspy --help
```

> The 'chmod' makes it runnable, and '--help' displays usage options. Expected output includes version info and flags like '-pf' for pid filtering. If it segfaults, wrong architecture—redownload.

### Step 3: Run Pspy to Monitor Processes

**Context**: Execute pspy to start real-time monitoring of process creations and command invocations, capturing output for analysis.

Launch pspy in the background or foreground to observe system activity.

**Command** ([[commands/pspy-run-process-monitor]]):
```bash
/tmp/pspy
```

> This runs pspy with default settings, monitoring all processes. Redirect output to a file if needed (e.g., > output.log). Expected output is a banner with version followed by timestamped CMD lines showing UID, PID, and executed commands, such as cron jobs or service starts. Let it run for 5-10 minutes to capture periodic tasks; Ctrl+C to stop.

### Step 4: Analyze Captured Output for Insights

**Context**: Review the logged output to identify high-value processes, such as root-owned scripts or writable cron files, informing next attack steps.

If output was redirected, grep for keywords like 'root' or 'cron'.

**Command** ([[commands/pspy-analyze-output]]):
```bash
grep 'UID=0' output.log
```

> Filters for root processes. Expected output lists commands run by UID 0, revealing potential escalations like /bin/sh -c scripts. Cross-reference with /etc/crontab for validation.
