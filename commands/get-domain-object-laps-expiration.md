---
id: 9f449209-d23b-49d0-ab98-6e494bc20369
name: get-domain-object-laps-expiration
type: command
executor: powershell
data: >-
  Get-DomainObject -Identity $_TARGET_MACHINE -Properties
  ms-Mcs-AdmPwdExpirationTime
output: null
created_at: '2023-04-06T03:56:28.479282+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - laps
verified: true
validated: true
---

# get-domain-object-laps-expiration

## Command

```powershell
Get-DomainObject -Identity $_TARGET_MACHINE -Properties ms-Mcs-AdmPwdExpirationTime
```

## Description

This PowerShell command, from the PowerView module, queries an Active Directory computer object to retrieve the LAPS password expiration time attribute. Use it to check the current expiration before or after modifications for persistence techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_TARGET_MACHINE | The NetBIOS name, distinguished name, or SID of the target computer object (e.g., 'WORKSTATION01') | Yes |
| -Properties ms-Mcs-AdmPwdExpirationTime | Specifies the AD attribute to retrieve (LAPS expiration time as 64-bit integer) | Yes |

## Examples

### Basic Usage

```powershell
Get-DomainObject -Identity WORKSTATION01 -Properties ms-Mcs-AdmPwdExpirationTime
```

### Advanced Usage

```powershell
Get-DomainObject -Identity 'CN=WORKSTATION01,OU=Computers,DC=domain,DC=com' -Properties ms-Mcs-AdmPwdExpirationTime,ms-Mcs-AdmPwd
```

## Expected Output

A hashtable or object showing the attribute value, e.g.:

```
ms-Mcs-AdmPwdExpirationTime : 132609935231523081
```

Success is indicated by the attribute value being returned without errors. A low or null value means the password may rotate soon.
