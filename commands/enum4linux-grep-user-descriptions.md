---
id: new-id-for-enum4linux
name: enum4linux-grep-user-descriptions
type: command
executor: bash
data: enum4linux -U $_TARGET | grep -i desc
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - samba-enumeration
  - ad-enumeration
verified: true
validated: true
---

# enum4linux-grep-user-descriptions

## Command

```bash
enum4linux -U $_TARGET | grep -i desc
```

## Description

This command uses enum4linux to enumerate users on a Samba/AD target and pipes output to grep for description fields, revealing potential secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | Enumerate users | Built-in |
| $_TARGET | Target IP or hostname | Yes |
| grep -i desc | Filter for description lines | Built-in |

## Examples

### Basic Usage

```bash
enum4linux -U 10.0.2.11 | grep -i desc
```

## Expected Output

```
User: admin Desc: Password: AdminPass
```

## Related

- [[procedures/Enumerate-Passwords-in-AD-User-Descriptions]]
- [[commands/powershell-get-ad-user-accounts-descriptions]]
