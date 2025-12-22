---
id: 5f25dbf1-d861-4163-8931-77a41081969a
name: whoami-check-current-user
type: command
executor: bash
data: whoami
output: null
created_at: '2023-04-06T03:56:20.471577+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
platforms:
  - Windows
tags:
  - reconnaissance
  - privilege-check
verified: true
validated: true
---

# whoami-check-current-user

## Command

```bash
whoami
```

## Description

This command displays the current Windows user account, useful for verifying privileges during initial access or post-exploitation on a MSSQL host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters; runs in current context | No |

## Examples

### Basic Usage

```bash
whoami
```

### Advanced Usage

```bash
whoami /all
```

## Expected Output

Current user: nt authority\system

Or similar, showing the effective username and domain.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
