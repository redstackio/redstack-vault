---
data: cat /var/opt/gitlab/.ssh/authorized_keys
tags:
  - file-read
  - ssh
type: command
executor: bash
platforms:
  - Linux
id: b846e1aa-a53a-4d3e-89f0-bc7bc49b930d
created_at: '2025-12-11T03:47:47.563Z'
updated_at: '2025-12-11T03:47:47.563Z'
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

Displays the contents of the SSH authorized_keys file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/var/opt/gitlab/.ssh/authorized_keys` | Path to file | Yes |

## Examples

### Basic Usage

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

## Expected Output

Commit details including the injected SSH public key.

## Related

- [[procedures/Establish-SSH-Access-and-Verify]]
