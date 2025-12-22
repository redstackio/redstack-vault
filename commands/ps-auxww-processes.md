---
data: ps auxww
tags:
  - enumeration
  - process-list
type: command
executor: bash
platforms:
  - Linux
id: 2229ce90-649b-4529-a1cc-69bb1f139388
created_at: '2025-12-11T03:47:57.743Z'
updated_at: '2025-12-11T03:47:57.743Z'
verified: false
validated: true
submitted: true
---
# ps-auxww-processes

## Command

```bash
ps auxww
```

## Description

Lists all running processes with detailed information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `a` | All users | Yes |
| `u` | User-oriented format | Yes |
| `x` | Processes without tty | Yes |
| `ww` | Unlimited width | Yes |

## Examples

### Basic Usage

```bash
ps auxww
```

## Expected Output

Detailed process list including PIDs, users, CPU, memory, etc.

## Related

- [[procedures/Post-Exploitation-System-Enumeration]]
