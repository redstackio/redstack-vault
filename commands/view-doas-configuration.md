---
id: cbe03aa6-1a1f-4f70-94c3-d50e49619378
name: view-doas-configuration
type: command
executor: bash
data: cat /etc/doas.conf
output: null
created_at: '2023-04-06T03:56:19.040389+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - configuration
verified: true
validated: true
---

# view-doas-configuration

## Command

```bash
cat /etc/doas.conf
```

## Description

This command displays the contents of the doas configuration file, revealing rules that define privilege elevation permissions. Used during reconnaissance to identify misconfigurations exploitable for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cat` | Command to output file contents | Yes |
| `/etc/doas.conf` | Path to the doas config file | Yes |

## Examples

### Basic Usage

```bash
cat /etc/doas.conf
```

### Advanced Usage

With grep for permissive rules:
```bash
grep "nopass" /etc/doas.conf
```

## Expected Output

Sample configuration:
```
# Secure rule
permit keepenv :wheel as root

# Misconfigured rule
permit nopass demo as root cmd vim
```

## Related

- [[procedures/Linux-Privilege-Escalation-via-Doas-Misconfiguration]]
- [[commands/check-doas-presence]]
