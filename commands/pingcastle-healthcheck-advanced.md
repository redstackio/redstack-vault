---
type: command
executor: powershell
data: >-
  pingcastle.exe --healthcheck --server $_DOMAIN_CONTROLLER --user $_USERNAME
  --password $_PASSWORD --advanced-live --nullsession
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

# pingcastle-healthcheck-advanced

## Command

```powershell
pingcastle.exe --healthcheck --server $_DOMAIN_CONTROLLER --user $_USERNAME --password $_PASSWORD --advanced-live --nullsession
```

## Description

Performs an advanced health check on AD, including live queries and null sessions for comprehensive risk assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN_CONTROLLER | DC IP or FQDN | Yes |
| $_USERNAME | Username for auth | No |
| $_PASSWORD | Password for auth | No |
| --advanced-live | Enable live mode | No |
| --nullsession | Allow null auth | No |

## Examples

### Basic Usage

```powershell
pingcastle.exe --healthcheck --server dc01.example.com --user admin --password Pass123 --advanced-live
```

## Expected Output

Healthcheck.html report with risk levels (0-5), e.g., "STIG-1: Anonymous access enabled - Risk 3".

## Related

- [[tools/PingCastle]]
- [[procedures/Active-Directory-Assessment-and-Privilege-Escalation]]
