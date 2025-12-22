---
type: command
executor: bash
data: find / -perm -u=s -type f 2>/dev/null
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - privilege-escalation
  - enumeration
verified: true
validated: true
---

# list-suid-binaries

## Command

```bash
find / -perm -u=s -type f 2>/dev/null
```

## Description

This command enumerates all SetUID (SUID) binaries on a Linux filesystem, identifying files that can be executed with elevated privileges. Use it during privilege escalation reconnaissance to find potential exploit targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/` | Starting search directory (root for full system scan) | Yes |
| `-perm -u=s` | Matches files with SUID bit set for user | Yes |
| `-type f` | Limits to regular files (excludes directories/symbolic links) | Yes |
| `2>/dev/null` | Suppresses permission-denied errors for cleaner output | No |

## Examples

### Basic Usage

```bash
find / -perm -u=s -type f 2>/dev/null
```

### Advanced Usage

```bash
find /usr/bin -perm -u=s -type f 2>/dev/null | xargs ls -l
```

This variant lists details of SUID binaries in /usr/bin only.

## Expected Output

A list of file paths, e.g.:

```
/bin/su
/bin/ping
/usr/bin/passwd
/usr/bin/sudo
/usr/local/bin/vulnerable-script
```

Success is indicated by paths to root-owned executables, which can be further inspected for exploits.

## Related

- [[procedures/Linux-Privilege-Escalation-via-SUID]]
- [[commands/ls-detailed-permissions]]
