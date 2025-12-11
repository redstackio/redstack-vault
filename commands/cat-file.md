---
data: (cat /var/opt/gitlab/.ssh/authorized_keys
tags:
  - inspection
type: command
executor: bash
platforms:
  - Linux
id: 2fc92765-b714-409e-9d1f-0bd3fd070492
created_at: '2025-12-11T06:10:22.606Z'
updated_at: '2025-12-11T06:10:22.606Z'
verified: false
validated: true
submitted: true
---
# cat-file

## Command

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

## Description

Displays the content of the specified file, used to verify overwrite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/var/opt/gitlab/.ssh/authorized_keys` | Path to the file | Yes |

## Examples

### Basic Usage

```bash
cat file.txt
```

## Expected Output

Shows tar headers followed by the injected SSH public key.

## Related

- [[procedures/Verify-File-Overwrite]]
