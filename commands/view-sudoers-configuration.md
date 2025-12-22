---
id: 66f7adec-bd8b-4118-9f73-74de2de60be1
type: command
executor: bash
data: cat /etc/sudoers
output: null
created_at: '2020-07-14T18:14:41.281513+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - configuration
verified: true
validated: true
---

# View Sudoers Configuration

## Command

```bash
cat /etc/sudoers
```

## Description

Displays the sudoers file contents to review privilege configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /etc/sudoers | Path to sudoers file | Built-in |

## Examples

### Basic Usage

```bash
cat /etc/sudoers
```

## Expected Output

File contents with user permissions.

## Related

- [[procedures/spawn-root-shell-using-sudo-perl]]
