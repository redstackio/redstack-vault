---
data: ps auxww
tags:
  - enumeration
type: command
executor: bash
platforms:
  - Linux
id: ce86c773-5c71-43f1-b977-066ebc166fe7
created_at: '2025-12-11T06:10:22.423Z'
updated_at: '2025-12-11T06:10:22.423Z'
verified: false
validated: true
submitted: true
---
# ps-process-list

## Command

```bash
ps auxww
```

## Description

Lists all running processes with detailed information, used in reverse shell for enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `a` | All users | Yes |
| `u` | User-oriented format | Yes |
| `x` | Processes without controlling tty | Yes |
| `ww` | Unlimited width | Yes |

## Examples

### Basic Usage

```bash
ps auxww
```

## Expected Output

Detailed process list including PIDs, users, CPU, memory, etc.

## Related

- [[procedures/Establish-Reverse-Shell-via-Uploaded-PoC]]
