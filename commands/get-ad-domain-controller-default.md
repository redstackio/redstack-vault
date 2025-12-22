---
id: 4b29c207-83b4-4694-b50c-fe7e669c269e
name: get-ad-domain-controller-default
type: command
executor: powershell
data: Get-ADDomainController
output: null
created_at: '2023-04-06T03:56:28.627255+00:00'
updated_at: '2023-04-10T20:37:41.799401+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - dc-enumeration
verified: true
validated: true
---

# get-ad-domain-controller-default

## Command

```powershell
Get-ADDomainController
```

## Description

Lists all domain controllers in the current domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Defaults to current domain | No |

## Examples

### Basic Usage

```powershell
Get-ADDomainController
```

### Filter by Site

```powershell
Get-ADDomainController -Discover -SiteName "Default-First-Site-Name"
```

## Expected Output

DC list:

```
Name            : DC01
IPv4Address     : 192.168.1.10
Site            : Default-First-Site-Name
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-specific-domain-controller-information]]
