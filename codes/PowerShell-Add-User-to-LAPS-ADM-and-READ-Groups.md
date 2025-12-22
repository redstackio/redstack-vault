---
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:04.524465+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - group-manipulation
  - laps
validated: true
---

# PowerShell-Add-User-to-LAPS-ADM-and-READ-Groups

## Code

```powershell
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred -Domain "domain.local"
Add-DomainGroupMember -Identity 'LAPS READ' -Members 'user1' -Credential $cred -Domain "domain.local"
```

## Description

This PowerShell script snippet uses the PowerView module to add a specified user to both the LAPS ADM and LAPS READ groups in Active Directory. It enables the user to manage (reset) and read LAPS passwords for domain-joined computers, facilitating credential access and privilege escalation in AD environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $cred | PSCredential object holding domain credentials | `$cred = Get-Credential` |
| user1 | Attacker-controlled username to add to groups | `attackeruser` |
| domain.local | Target domain FQDN | `corp.example.com` |

## Usage

Load PowerView with Import-Module PowerView.ps1, create $cred via Get-Credential using compromised domain creds, then execute the script. Run from a domain-joined machine or via PSSession. After execution, proceed to query LAPS passwords with Get-ADComputer. Ideal for red team scenarios targeting LAPS misconfigurations.

## Detection

- PowerShell Script Block Logging capturing Add-DomainGroupMember executions.
- AD audit logs for group membership changes (Event ID 4728/4732).
- Network traffic to DCs with unusual LDAP queries from non-admin accounts.
- EDR alerts on PowerView module imports or unsigned script execution.

## Related

- [[procedures/Retrieve-LAPS-Password-via-Group-Manipulation]]
- [[tools/PowerView]]
