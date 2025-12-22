---
type: command
executor: powershell
data: pingcastle.exe --scanner $_SCANNER_NAME --server $_DOMAIN
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - scanning
  - active-directory
verified: true
validated: true
---

# pingcastle-scanner

## Command

```powershell
pingcastle.exe --scanner $_SCANNER_NAME --server $_DOMAIN
```

## Description

Runs a specific scanner for targeted AD vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SCANNER_NAME | Scanner like 'localadmin' or 'nullsession' | Yes |
| $_DOMAIN | Domain FQDN | Yes |

## Examples

### Basic Usage

```powershell
pingcastle.exe --scanner localadmin --server example.com
```

## Expected Output

List of vulnerable objects, e.g., machines with local admin shares.

## Related

- [[tools/PingCastle]]
