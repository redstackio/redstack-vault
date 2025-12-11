---
data: cat /var/opt/gitlab/.ssh/authorized_keys
tags:
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: 0542277b-5304-484d-8048-2b4b6026911b
created_at: '2025-12-11T06:10:29.240Z'
updated_at: '2025-12-11T06:10:29.240Z'
verified: false
validated: true
submitted: true
---
# cat-authorized-keys

## Command

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

## Description

Reads the contents of the SSH authorized_keys file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/var/opt/gitlab/.ssh/authorized_keys` | File path | Yes |

## Examples

### Basic Usage

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

## Expected Output

Commit details including injected SSH public key.

## Related

- [[procedures/Establish-SSH-Access]]
