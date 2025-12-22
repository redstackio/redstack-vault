---
type: command
executor: bash
data: ls -la /etc/passwd
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - discovery
  - privesc
verified: true
validated: true
---

# check-etc-passwd-permissions

## Command

```bash
ls -la /etc/passwd
```

## Description

Lists the permissions and ownership of the /etc/passwd file to determine if it is writable by non-root users, a key check for privilege escalation exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /etc/passwd | Path to the passwd file | Yes |
| -l | Long format listing | Yes |
| -a | Include all files (hidden) | Yes |

## Examples

### Basic Usage

```bash
ls -la /etc/passwd
```

### Advanced Usage

```bash
ls -la /etc/ | grep passwd
```
To filter for passwd-related files.

## Expected Output

```
-rw-rw-rw- 1 root root 2048 Oct 1 12:00 /etc/passwd
```
Look for 'rw' in group or other columns indicating writability.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/view-etc-passwd]]
