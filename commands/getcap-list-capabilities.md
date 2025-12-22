---
id: e077b775-3951-4831-9582-c3c7891c415f
type: command
executor: bash
data: getcap -r / 2>/dev/null
output: |-
  user@ubuntu18x64:~$ getcap -r / 2>/dev/null
  /usr/bin/openssl = cap_dac_override+ep
  /usr/bin/nmap = cap_net_raw,cap_net_admin+ep
created_at: '2019-10-11T21:24:57.010925+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - priv-esc
  - enumeration
verified: true
validated: true
---

# getcap-list-capabilities

## Command

```bash
getcap -r / 2>/dev/null
```

## Description

Recursively lists files with Linux capabilities, showing extended privileges that could aid escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Recursive search | Yes |
| / | Start from root | Yes |
| 2>/dev/null | Hide permission errors | Yes |

## Examples

### Basic Usage

```bash
getcap -r / 2>/dev/null
```

### Specific Directory

```bash
getcap -r /usr/bin 2>/dev/null
```

## Expected Output

Capabilities like /usr/bin/nmap = cap_net_raw+ep.

## Related

- [[procedures/Find-Linux-Files-with-Elevated-Privileges]]
