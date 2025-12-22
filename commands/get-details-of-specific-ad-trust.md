---
id: 6a2431c8-81a3-46c4-b963-462ee4c94241
name: get-details-of-specific-ad-trust
type: command
executor: powershell
data: Get-ADTrust -Identity <DomainName>
output: null
created_at: '2023-04-06T03:56:02.419826+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - trust-enumeration
verified: true
validated: true
---

# get-details-of-specific-ad-trust

## Command

```powershell
Get-ADTrust -Identity $_DomainName
```

## Description

Gets detailed information on a specific domain trust relationship.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_DomainName | Name of the trusted domain | Yes |

## Examples

### Basic Usage

```powershell
Get-ADTrust -Identity "partner.com"
```

### With Specific Properties

```powershell
Get-ADTrust -Identity "partner.com" | Select Name, TrustType, TrustDirection
```

## Expected Output

Trust object:

```
Name              : partner.com
TrustType         : Forest
TrustDirection    : Bidirectional
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/list-all-ad-trusts-in-domain]]
