---
id: cmd-ln-s-passwd
name: create-symlink-passwd
type: command
executor: bash
data: ln -s /tmp/passwd ./passwd
output: 'Symlink created: lrwxr-xr-x ... ./uploads/passwd -> /tmp/passwd'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.192Z'
platforms:
  - Linux
tags:
  - symlink
  - testing
verified: false
validated: true
submitted: true
---

# create-symlink-passwd

## Command

```bash
ln -s /tmp/passwd ./passwd
```

## Description

Creates a symbolic link named 'passwd' pointing to /tmp/passwd in the current directory for testing symlink preservation in GitLab import/export.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| target | Source file (/tmp/passwd) | Yes |
| link | Link name (./passwd) | Yes |
| options | -s for symbolic | Yes |

## Examples

### Basic Usage

```bash
ln -s /tmp/passwd ./passwd
```

### Advanced Usage

```bash
ln -s /etc/shadow ./shadow_link
```

## Expected Output

Symlink created; verify with ls -l showing lrwxr-xr-x -> /tmp/passwd.

## Related

- [[commands/cd-uploads-dir]]
