---
id: 2c360a86-12b1-4be4-a3fb-2f9f678ef18f
name: list-all-ad-trusts-in-domain
type: command
executor: powershell
data: Get-ADTrust -Filter *
output: null
created_at: '2023-04-06T03:56:02.419776+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - trust-enumeration
verified: true
validated: true
---

# list-all-ad-trusts-in-domain

## Command

```powershell
Get-ADTrust -Filter *
```

## Description

Enumerates all trust relationships in the current domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter * | All trusts | Yes |

## Examples

### Basic Usage

```powershell
Get-ADTrust -Filter *
```

### Export Results

```powershell
Get-ADTrust -Filter * | Export-Csv trusts.csv
```

## Expected Output

Trust list:

```
Name              : trusted.com
TrustType         : External
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-details-of-specific-ad-trust]]
