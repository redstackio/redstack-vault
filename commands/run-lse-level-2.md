---
id: 9200e8fc-998d-4265-8440-d82864fb80de
name: run-lse-level-2
type: command
executor: bash
data: ./lse.sh -l2
output: null
created_at: '2023-04-06T03:56:18.414138+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
verified: true
validated: true
---

# run-lse-level-2

## Command

```bash
./lse.sh -l2
```

## Description

Full system dump with LSE level 2.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l2 | Level 2 verbosity | Yes |

## Examples

### Basic Usage

```bash
./lse.sh -l2
```

## Expected Output

Comprehensive sections on users, files, services, etc.

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linux-smart-enumeration]]
