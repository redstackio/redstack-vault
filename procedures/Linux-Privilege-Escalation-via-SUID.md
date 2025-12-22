---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Setuid and Setgid|T1166 - Setuid and Setgid]]'
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/SUID]]'
commands:
  - '[[commands/list-suid-binaries]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-SUID

## Summary

This procedure identifies SetUID (SUID) binaries on a Linux system, which can be exploited for privilege escalation by running with elevated permissions (typically root). Attackers enumerate SUID files to find misconfigurations or vulnerable binaries that allow execution of arbitrary commands as the file owner, leading to root access.

## Description

SUID binaries are executable files with the SUID bit set, allowing them to run with the effective user ID of the file owner rather than the executing user. This is useful for legitimate administrative tasks but poses a security risk if an SUID binary can be abused (e.g., via path hijacking, race conditions, or built-in features like shell spawning). Common exploitable SUID binaries include custom scripts or misconfigured system tools like 'find', 'vim', or 'sudo'. This procedure focuses on enumeration to identify candidates for exploitation, assuming low-privileged shell access. Successful identification can lead to root shell, enabling persistence or data exfiltration.

## Requirements

1. Low-privileged shell access to the target Linux system (e.g., via initial access vector like SSH with user credentials).
2. Standard Unix tools available (e.g., 'find' and 'ls', typically present on most distributions).
3. No root privileges required for enumeration, but exploitation may need write access to certain paths.

## Defense

- Regularly audit SUID binaries using tools like 'find' or automated scripts to remove unnecessary ones.
- Apply least privilege: Ensure only essential binaries have SUID set and monitor for changes with file integrity tools like AIDE.
- Use AppArmor or SELinux to confine SUID executions and log privilege changes via auditd.
- Patch known vulnerable SUID binaries and restrict PATH variables to prevent hijacking.

## Objectives

1. Enumerate all SUID binaries on the system to identify potential escalation vectors.
2. Inspect permissions and ownership of discovered binaries for exploitation opportunities.
3. Gain root privileges by abusing a vulnerable SUID binary (e.g., spawning a root shell).
4. Verify escalation success and maintain access if needed.

## Instructions

### Step 1: Enumerate SUID Binaries

**Context**: Search the filesystem for files with the SUID bit set. This reveals binaries that run as their owner (often root), which can be abused if they allow command execution or environment manipulation.

**Command** ([[commands/list-suid-binaries]]):
```bash
find / -perm -u=s -type f 2>/dev/null
```

> This command recursively searches from the root directory for regular files (-type f) with the SUID permission (-perm -u=s), suppressing error messages (2>/dev/null) for noisy paths like /proc. It lists paths to potential targets. Run this as the current user to avoid alerting defenders.

### Step 2: Inspect Specific SUID Binary Permissions

**Context**: Once SUID binaries are identified, examine their detailed permissions, ownership, and size to assess exploitability. Focus on non-standard or writable binaries.

**Command** ([[commands/list-suid-binaries]]):
```bash
ls -l /path/to/suid/binary
```

> Replace /path/to/suid/binary with a discovered file (e.g., /usr/bin/find). Look for output like -rwsr-xr-x (the 's' indicates SUID). Ownership by root and executable status confirm potential for escalation. If the binary is world-writable or in a controllable PATH, it may be hijackable.

### Step 3: Test for Exploitation

**Context**: For known vulnerable SUID binaries (e.g., if 'vim' is SUID), attempt to spawn a root shell. This step assumes identification of an exploitable binary; research specific exploits (e.g., GTFOBins for 'find' command abuse).

> No specific command here, as exploitation varies. For example, if 'find' is SUID: execute `find . -exec /bin/sh \; -quit` to get a root shell. Verify with `id` command showing uid=0(root). If unsuccessful, pivot to other binaries or techniques like kernel exploits.

### Step 4: Verify Privilege Escalation

**Context**: Confirm root access post-exploitation to ensure the escalation worked and assess further actions.

```bash
whoami
id
```

> Expected output: 'root' from whoami and uid=0(root) gid=0(root) from id. This validates success and allows proceeding to objectives like data access.
