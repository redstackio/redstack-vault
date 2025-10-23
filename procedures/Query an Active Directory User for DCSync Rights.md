---
id: d0104fca-b063-47bf-844b-a4a64e3a3399
name: Query an Active Directory User for DCSync Rights
type: procedure
verified: false
submitted: false
created_at: '2020-03-20T22:38:48.772506+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
- '[[powershell]]'
commands:
- '[[ActiveDirectory List AD Users with SID]]'
- '[[Query Active Directory User by SID for DCSync Rights]]'
---

# Query an Active Directory User for DCSync Rights

## Summary

List Active Directory users then query a single user to check for replication privileges needed to perform a DCSync attack. 

## Description

# Description

List Active Directory users then query a single user to check for replication privileges needed to perform a DCSync attack.



# Instructions

1. Get a list of  users with SID using PowerShell's ActiveDirectory module





**Command** ([[ActiveDirectory List AD Users with SID]]):

```bash
Get-ADUser -Filter * | Select-Object -Property name,sid
```





2. Download PowerView (dev branch) and import it into a PowerShell session:  [Download from GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)

3. Query each user by SID, specifying the domain to check for rights associated with DCSync.





**Command** ([[Query Active Directory User by SID for DCSync Rights]]):

```bash
Get-ObjectAcl -Identity "dc=$_DC1,dc=$_DC2" -ResolveGUIDs | ? {$_.SecurityIdentifier -match "$_SID"}
```



Users with replication privileges needed to perform a DCSync attack will have at minimum:

- DS-Replication-Get-Changes - AccessAllowed / ExtendedRight

- DS-Replication-Get-Changes-All - AccessAllowed / ExtendedRight

Note: This command may generate error messages, but will still enumerate DCSync rights if they exist.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[ActiveDirectory List AD Users with SID]]
- [[Query Active Directory User by SID for DCSync Rights]]

## Tags

- [[Active Directory]]
- [[Enumeration]]
- [[powershell]]


