---
id: cmd-003
data: 'sudo chown root:root /suidfs/passwd'
tags:
  - ownership-change
type: command
output: 'Ownership changed to root:root'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.217Z'
verified: false
validated: true
submitted: true
---
# sudo-chown-root-binary

## Command

```bash
sudo chown root:root /suidfs/passwd
```

## Description

Changes ownership of the binary to root:root for setuid functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| root:root | Owner:group | Yes |
| /suidfs/passwd | Target file | Yes |

## Examples

### Basic Usage

```bash
sudo chown root:root /suidfs/passwd
```

## Expected Output

Ownership updated confirmation.

## Related

- [[commands/sudo-cp-copy-binary]]
