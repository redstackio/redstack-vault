---
id: a63d756b-5f43-4d83-a9cb-a95698ee367e
name: get-aduser-filter-spn-powershell
type: command
executor: powershell
data: >-
  Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties
  ServicePrincipalName
output: null
created_at: '2023-01-12T17:49:32.489275+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# get-aduser-filter-spn-powershell

## Command

```powershell
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

## Description

This PowerShell command uses the Active Directory module to list all domain users who have a Service Principal Name (SPN) set, filtering for non-null SPN attributes. It is essential for identifying Kerberoastable service accounts in AD environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter | LDAP filter to select users with SPN != null | Yes |
| -Properties | Specifies ServicePrincipalName to include in output | Yes |

## Examples

### Basic Usage

```powershell
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

### Advanced Usage

```powershell
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName | Select Name, ServicePrincipalName
```

## Expected Output

DistinguishedName : CN=svc-mssql,CN=Users,DC=corp,DC=local
Name              : svc-mssql
ServicePrincipalName : {MSSQLSvc/server.corp.local}

(List of users with SPNs; empty if none found.)

## Related

- [[procedures/Find-Kerberoastable-Users-with-SPNs]]
