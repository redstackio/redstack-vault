---
id: 95fa9d41-99e2-424c-aae4-b8879524f67d
name: cd-directory-navigate
type: command
executor: bash
data: cd /root
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.829Z'
platforms:
  - Linux
tags:
  - navigation
  - bash
verified: false
validated: true
submitted: true
---

# cd-directory-navigate

## Command

```bash
cd /root
```

## Description

This command changes the current working directory to /root, setting the location from which the featurebook server will serve content, enabling traversal to system files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/root` | Target directory path | Yes |

## Examples

### Basic Usage

```bash
cd /root
```

### Advanced Usage

```bash
cd /tmp/test-dir
```

## Expected Output

No output on success; the shell prompt updates to reflect the new directory. Use `pwd` to confirm.

## Related

- [[commands/featurebook-serve]]
