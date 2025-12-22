---
type: command
executor: cmd
data: gpresult /r
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reconnaissance
  - active-directory
  - group-policy
verified: true
validated: true
---

# gpresult-display-rsop

## Command

```cmd
gpresult /r
```

## Description

Displays the Resultant Set of Policy (RSoP) for the current user and computer, including details on the authenticating domain controller.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /r | Shows RSoP summary | Yes |

## Examples

### Basic Usage

```cmd
gpresult /r
```

### For Remote System

```cmd
gpresult /r /s:remotehost
```

## Expected Output

RSOP data for DOMAIN\USER on MACHINE : COMPUTER
=====================================

Site: contoso-dc-site

The processing of Group Policy failed.  Windows could not authenticate to the Active Directory service on a domain controller.

## Related

- [[procedures/Active-Directory-Domain-Controller-Lookup]]
