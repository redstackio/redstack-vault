---
data: ln -s /path/to/target /path/to/symlink
tags:
  - file-system
  - symlink
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.811Z'
id: 299093de-f9d6-4289-91e5-6d9707d90428
verified: false
validated: true
submitted: true
---
# ln-create-symlink

## Command

```bash
ln -s /path/to/target /path/to/symlink
```

## Description

The `ln` command with `-s` flag creates a symbolic link (symlink) pointing from the symlink path to the target file or directory. Used in attacks to redirect file operations, such as in privilege escalation scenarios where installers follow links insecurely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Specifies symbolic link (soft link) | Yes |
| `/path/to/target` | The file or directory to link to | Yes |
| `/path/to/symlink` | The path where the symlink is created | Yes |

## Examples

### Basic Usage

```bash
ln -s /etc/sudoers /tmp/fake-sudoers
```

### Advanced Usage

```bash
ln -s /Library/Preferences /tmp/redirect-lib
ln -sf /new-target /tmp/symlink  # -f to force overwrite
```

## Expected Output

No output on success; use `ls -l` to verify the symlink (shows `target -> /path/to/target`).

## Related

- [[Related Procedure: Create Symbolic Links to Redirect File Operations]]
