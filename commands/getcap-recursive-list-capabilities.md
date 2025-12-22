---
id: e077b775-3951-4831-9582-c3c7891c415f
type: command
executor: bash
data: getcap -r / 2>/dev/null
output: |-
  user@ubuntu18x64:~$ getcap -r / 2>/dev/null
  /usr/bin/openssl = cap_dac_override+ep
  /usr/bin/mtr-packet = cap_net_raw+ep
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

# getcap-recursive-list-capabilities

## Command

```bash
ggetcap -r $_DIRECTORY 2>/dev/null
```

## Description

Recursively lists all files and directories in the specified path that have Linux capabilities set. This is useful for privilege escalation enumeration by identifying files with elevated permissions that could be abused.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Perform a recursive search starting from the specified directory | Yes |
| $_DIRECTORY | The starting directory for the recursive search (e.g., / for root) | Yes |
| 2>/dev/null | Suppress error messages (stderr redirection) | No |

## Examples

### Basic Usage

```bash
ggetcap -r / 2>/dev/null
```

### Advanced Usage

```bash
ggetcap -r /usr/bin 2>/dev/null
```

## Expected Output

A list of files with their associated capabilities, such as:

```
/usr/bin/openssl = cap_dac_override+ep
/usr/bin/mtr-packet = cap_net_raw+ep
```

This output shows files like openssl with the cap_dac_override capability, which bypasses file permission checks.

## Related

- [[procedures/Find-Linux-Files-with-Elevated-Privileges]]
