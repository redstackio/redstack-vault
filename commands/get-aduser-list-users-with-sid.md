---
id: 44d65861-c679-47d4-ac7e-fa0a2ab583ec
name: get-aduser-list-users-with-sid
type: command
executor: powershell
data: 'Get-ADUser -Filter * | Select-Object -Property name,sid'
output: >-
  PS C:\> Get-ADUser -Filter * | Select-Object -Property name,sid
                                            
  name                                                          sid     

  ----                                                          ---

  Administrator                                                
  S-1-5-21-3072663084-364016917-1341370565-500

  Guest                                                        
  S-1-5-21-3072663084-364016917-1341370565-501

  DefaultAccount                                               
  S-1-5-21-3072663084-364016917-1341370565-503

  krbtgt                                                       
  S-1-5-21-3072663084-364016917-1341370565-502

  Exchange Online-ApplicationAccount                           
  S-1-5-21-3072663084-364016917-1341370565-1123

  SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1}          
  S-1-5-21-3072663084-364016917-1341370565-1124
created_at: '2020-03-20T22:38:48.722091+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - Enumeration
verified: true
validated: true
---

# get-aduser-list-users-with-sid

## Command

```powershell
Get-ADUser -Filter * | Select-Object -Property name,sid
```

## Description

This command uses the ActiveDirectory PowerShell module to retrieve all domain users and display their names along with Security Identifiers (SIDs). It is useful for initial enumeration in AD environments to identify users for further privilege checks, such as DCSync rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter * | Retrieves all users (no specific filter applied) | Yes |
| Select-Object -Property name,sid | Limits output to name and SID columns | Yes |

## Examples

### Basic Usage

```powershell
Get-ADUser -Filter * | Select-Object -Property name,sid
```

### Advanced Usage

```powershell
Get-ADUser -Filter {Enabled -eq $true} | Select-Object -Property name,sid | Export-Csv -Path users.csv -NoTypeInformation
```

> This variation filters for enabled users only and exports to CSV for offline analysis.

## Expected Output

Description of what output to expect when the command runs successfully.

```
PS C:\> Get-ADUser -Filter * | Select-Object -Property name,sid
                                          
name                                                          sid     
----                                                          ---
Administrator                                                 S-1-5-21-3072663084-364016917-1341370565-500
Guest                                                         S-1-5-21-3072663084-364016917-1341370565-501
DefaultAccount                                                S-1-5-21-3072663084-364016917-1341370565-503
krbtgt                                                        S-1-5-21-3072663084-364016917-1341370565-502
Exchange Online-ApplicationAccount                            S-1-5-21-3072663084-364016917-1341370565-1123
SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1}           S-1-5-21-3072663084-364016917-1341370565-1124
```

## Related

- [[procedures/Query-Active-Directory-User-for-DCSync-Rights]]
- [[commands/get-objectacl-query-user-dcsync-rights]]
