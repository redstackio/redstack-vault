---
id: cmd-chmod-777-passwd
name: set-permissions-777-passwd
type: command
executor: bash
data: chmod 777 /tmp/passwd
output: Permissions changed to rwxrwxrwx
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.216Z'
platforms:
  - Linux
tags:
  - testing
  - permissions
verified: false
validated: true
submitted: true
---

# set-permissions-777-passwd

## Command

```bash
chmod 777 /tmp/passwd
```

## Description

Sets world-readable/writable/executable permissions on /tmp/passwd to simulate accessible sensitive files in symlink testing for GitLab import vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| mode | Permission octal (777) | Yes |
| file | Target file (/tmp/passwd) | Yes |

## Examples

### Basic Usage

```bash
chmod 777 /tmp/passwd
```

### Advanced Usage

```bash
chmod 755 /tmp/another_file
```

## Expected Output

No stdout; permissions updated. Verify with ls -l /tmp/passwd showing -rwxrwxrwx.

## Related

- [[commands/stat-file-passwd]]
