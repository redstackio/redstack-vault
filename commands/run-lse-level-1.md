---
id: 5ca0d118-c397-4f98-886b-27364ca2efc9
name: run-lse-level-1
type: command
executor: bash
data: ./lse.sh -l1
output: null
created_at: '2023-04-06T03:56:18.414082+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
verified: true
validated: true
---

# run-lse-level-1

## Command

```bash
./lse.sh -l1
```

## Description

Runs LSE at level 1 to show priv esc-relevant info.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l1 | Level 1 verbosity | Yes |

## Examples

### Basic Usage

```bash
./lse.sh -l1
```

## Expected Output

[*] Networking info
[*] Processes
[!] SUID binaries: /usr/bin/find

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linux-smart-enumeration]]
