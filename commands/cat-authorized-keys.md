---
id: cmd-uuid-6
data: cat /var/opt/gitlab/.ssh/authorized_keys
tags:
  - verification
  - ssh
type: command
output: |-
  commit ... 

   ssh-rsa AAAAB3NzaC1yc2E... will@MacBook-Pro.local
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.322Z'
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

Views the authorized_keys file to confirm injected SSH key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /var/opt/gitlab/.ssh/authorized_keys | File path | Yes |

## Examples

### Basic Usage

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

## Expected Output

Commit log followed by public key.

## Related

- [[Related Procedure: Gain-SSH-Access-as-Git-User]]
