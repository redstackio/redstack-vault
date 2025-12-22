---
data: cat /tmp/file
tags:
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: 77d8221a-cbdd-4fba-8bfa-223535a07d8b
created_at: '2025-12-11T06:10:29.387Z'
updated_at: '2025-12-11T06:10:29.387Z'
verified: false
validated: true
submitted: true
---
# cat-file-contents

## Command

```bash
cat /tmp/file
```

## Description

Reads and displays the contents of a file to verify overwrite or content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/file` | File path | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/file
```

### Advanced Usage

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

## Expected Output

File contents, e.g., commit log with controlled message.

## Related

- [[procedures/Verify-File-Overwrite]]
- [[procedures/Establish-SSH-Access]]
