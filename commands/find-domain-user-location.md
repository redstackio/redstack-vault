---
id: unknown
type: command
executor: powershell
data: >-
  Find-DomainUserLocation -Domain $_DOMAIN_NAME | Select-Object UserName,
  SessionFromName
output: null
created_at: '2023-04-06T03:56:02.229000+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Enumerate Domain Machines Where Users Are Logged In

## Command

```powershell
Find-DomainUserLocation -Domain $_DOMAIN_NAME | Select-Object UserName, SessionFromName
```

## Description

Finds machines where specific users have sessions in the domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Domain | Target domain | Yes |

## Examples

### Basic Usage

```powershell
Find-DomainUserLocation -Domain 'example.com' | Select-Object UserName, SessionFromName
```

## Expected Output

Table of UserName and SessionFromName.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
