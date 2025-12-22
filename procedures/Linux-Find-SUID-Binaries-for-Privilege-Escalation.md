---
id: 329beb02-6453-42a4-9316-58cff93604af
name: Linux-Find-SUID-Binaries-for-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.822508+00:00'
updated_at: '2023-04-10T20:34:27.113361+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Setuid and Setgid|T1166 - Setuid and Setgid]]'
sub_techniques: []
tags:
  - '[[tags/Find SUID binaries]]'
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/SUID]]'
commands:
  - '[[commands/find-all-suid-binaries]]'
  - '[[commands/find-root-owned-suid-binaries]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Find-SUID-Binaries-for-Privilege-Escalation

## Summary

This procedure identifies SetUID (SUID) binaries on a Linux system, which can be exploited for privilege escalation. SUID binaries allow processes to run with the privileges of their owner, often root, enabling attackers with low-privilege access to potentially execute commands as a higher-privileged user if the binary is misconfigured or vulnerable.

## Description

In Linux environments, SUID binaries are special executables that temporarily grant elevated privileges to the user running them, matching the file owner's permissions. Attackers often search for these during post-exploitation to escalate from a standard user shell to root access. This technique is common in privilege escalation phases of penetration tests or real attacks, targeting systems where unnecessary SUID bits are set on custom or legacy binaries. The procedure scans the filesystem for SUID files, lists their details, and focuses on root-owned ones, which pose the highest risk. Once identified, manual analysis or known exploits can be applied to leverage them, such as editing environment variables or chaining with other vulnerabilities. This is typically used after initial access in a Unix-like target environment with shell access.

## Requirements

1. Shell access to the target Linux system (local or remote via SSH/reverse shell).
2. Sufficient permissions to execute read commands on the filesystem (standard user level is often enough for enumeration).
3. Basic knowledge of Linux file permissions and the `find` utility.

## Defense

- Regularly audit and remove unnecessary SUID binaries using tools like `find` or automated scripts.
- Implement application whitelisting and least privilege principles to limit SUID usage.
- Monitor for anomalous executions of SUID binaries via process auditing (e.g., auditd) and file integrity monitoring.
- Apply security baselines like CIS benchmarks to restrict SUID on sensitive paths.

## Objectives

1. Enumerate all SUID binaries across the filesystem to identify potential escalation vectors.
2. Specifically locate root-owned SUID binaries for high-impact targets.
3. Provide detailed listings for further manual analysis or exploitation.

## Instructions

### Step 1: Enumerate All SUID Binaries

**Context**: This step searches the entire filesystem for files with the SUID bit set, excluding SGID for focus, and lists them with detailed permissions to reveal ownership and paths. It helps identify any executable that could grant elevated privileges.

**Command** ([[commands/find-all-suid-binaries]]):
```bash
find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
```

> The `find` command recursively scans from root (`/`), filtering for files (`-type f`) with SUID permissions (`-perm -4000`). The `-exec ls -la` provides verbose output including owner, group, and permissions. Errors from inaccessible directories are suppressed (`2>/dev/null`). Run this as a low-privilege user to simulate real attack conditions. Expected output includes lines like `-rwsr-xr-x 1 root root ... /usr/bin/sudo`, indicating SUID (the 's' in permissions).

### Step 2: Enumerate Root-Owned SUID Binaries

**Context**: Narrow the search to SUID binaries owned by root (UID 0), as these offer the most direct path to root privileges. This refines the results from Step 1, prioritizing high-risk targets for exploitation.

**Command** ([[commands/find-root-owned-suid-binaries]]):
```bash
find / -uid 0 -perm -4000 -type f 2>/dev/null
```

> This command combines ownership filter (`-uid 0` for root) with SUID (`-perm -4000`) and file type (`-type f`). It lists paths without additional `ls` for a cleaner, faster output focused on locations. Expected output is a list of paths like `/usr/bin/passwd` or custom binaries. If no output, no root SUID binaries are present, indicating a hardened system. Follow up by testing identified binaries (e.g., `sudo -l` or environment manipulation) to check exploitability.
