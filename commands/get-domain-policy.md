---
id: 87fff44a-7dab-4301-ba82-9502fd042058
type: command
executor: powershell
data: Get-DomainPolicy
output: null
created_at: '2023-04-06T03:56:02.228444+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Domain Policy Configurations

## Command

```powershell
Get-DomainPolicy
```

## Description

Retrieves the overall domain policy configurations, including system access and Kerberos policies, to assess security settings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters needed; queries current domain | No |

## Examples

### Basic Usage

```powershell
Get-DomainPolicy
```

## Expected Output

Returns a collection of policy objects, such as SystemAccess and KerberosPolicy hashtables with settings like password complexity and lockout duration.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
