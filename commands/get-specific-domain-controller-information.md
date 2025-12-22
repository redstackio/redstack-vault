---
id: e2cedd7c-c96c-4669-85cc-132475823ab3
name: get-specific-domain-controller-information
type: command
executor: powershell
data: Get-ADDomainController -Identity <DomainName>
output: null
created_at: '2023-04-06T03:56:02.419254+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - dc-enumeration
verified: true
validated: true
---

# get-specific-domain-controller-information

## Command

```powershell
Get-ADDomainController -Identity $_DomainName
```

## Description

Retrieves information on domain controllers in a specific domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_DomainName | Target domain name | Yes |

## Examples

### Basic Usage

```powershell
Get-ADDomainController -Identity "contoso.com"
```

## Expected Output

Filtered DC list:

```
Name            : DC02
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-ad-domain-controller-default]]
