---
id: b90bf6c8-e5b9-4e7a-a59c-d128636082c3
type: command
executor: bash
data: find / -perm -4000 -ls 2>/dev/null
output: |-
  user@ubuntu18x64:~$ find / -perm -4000 -ls 2>/dev/null
    1180389     40 -rwsr-xr-x   1 root     root        40344 Jan 25  2018 /usr/bin/newgrp
    1180536    148 -rwsr-xr-x   1 root     root       149080 Jan 18  2018 /usr/bin/sudo
    1181285   2612 -rwsr-xr-x   1 root     root      2671240 Jun  6 17:31 /usr/bin/nmap
created_at: '2019-10-11T21:24:57.011696+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - priv-esc
  - enumeration
verified: true
validated: true
---

# find-setuid-files

## Command

```bash
find / -perm -4000 -ls 2>/dev/null
```

## Description

Searches the filesystem for setuid executables (permission 4000), listing details to identify potential privilege escalation vectors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| / | Start search from root | Yes |
| -perm -4000 | Match setuid bit | Yes |
| -ls | Long listing format | Yes |
| 2>/dev/null | Suppress errors | Yes |

## Examples

### Basic Usage

```bash
find / -perm -4000 -ls 2>/dev/null
```

### Specific Path

```bash
find /usr/bin -perm -4000 -ls
```

## Expected Output

List of SUID files like -rwsr-xr-x /usr/bin/nmap.

## Related

- [[procedures/Find-Linux-Files-with-Elevated-Privileges]]
