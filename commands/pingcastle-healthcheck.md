---
type: command
executor: powershell
data: pingcastle.exe --healthcheck --server $_DOMAIN
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - assessment
  - active-directory
verified: true
validated: true
---

# pingcastle-healthcheck

## Command

```powershell
pingcastle.exe --healthcheck --server $_DOMAIN
```

## Description

Basic health check for AD security posture using null sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain FQDN | Yes |

## Examples

### Basic Usage

```powershell
pingcastle.exe --healthcheck --server example.com
```

## Expected Output

Summary report with basic risks like weak encryption.

## Related

- [[tools/PingCastle]]
