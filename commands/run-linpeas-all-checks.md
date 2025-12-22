---
id: new-uuid-3
name: run-linpeas-all-checks
type: command
executor: bash
data: ./linpeas.sh -a
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - privilege-escalation
verified: true
validated: true
---

# run-linpeas-all-checks

## Command

```bash
./linpeas.sh -a
```

## Description

Runs LinPEAS with all checks enabled for comprehensive system enumeration, identifying potential priv esc paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Enable all checks (deeper but slower) | Yes |

## Examples

### Basic Usage

```bash
./linpeas.sh -a
```

## Expected Output

[*] System Information
OS: Linux 5.4.0-42-generic
Kernel: 5.4.0-42-generic
...

[!] Possible SUID Binaries:
-rwsr-xr-x 1 root root 12345 /usr/bin/find

[YELLOW] Writable files in /etc/
-rw-rw-rw- 1 root root 1024 /etc/passwd

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linPEAS]]
