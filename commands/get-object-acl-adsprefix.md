---
id: 7ce7cdff-9364-47d2-8cf4-ac6bc3a04a84
type: command
executor: powershell
data: Get-ObjectAcl -ADSprefix '$_ADS_PREFIX' -Verbose
output: null
created_at: '2023-04-06T03:56:02.230551+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get ACLs with ADS Prefix

## Command

```powershell
Get-ObjectAcl -ADSprefix '$_ADS_PREFIX' -Verbose
```

## Description

Retrieves ACLs using LDAP prefix, with verbose output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ADSprefix | LDAP path (e.g., 'CN=Users,DC=domain') | Yes |
| -Verbose | Detailed output | No |

## Examples

### Basic Usage

```powershell
Get-ObjectAcl -ADSprefix 'CN=Administrator,CN=Users' -Verbose
```

## Expected Output

Verbose ACL details.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
