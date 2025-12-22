---
id: 4236d141-024c-4028-b7c6-b7911e78b413
name: Enumerate Computers with Expired LAPS Passwords
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.929811+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - laps
  - discovery
validated: true
---

# Enumerate Computers with Expired LAPS Passwords

## Code

```powershell
Get-ADComputer -Filter {ms-Mcs-AdmPwdExpirationTime -like '*'} -Properties 'ms-Mcs-AdmPwd','ms-Mcs-AdmPwdExpirationTime'
```

## Description

This PowerShell snippet uses the ActiveDirectory module to query domain-joined computers that have LAPS passwords configured, specifically filtering for those with an expiration time set (indicating expired or rotatable passwords). It retrieves the password and expiration attributes, aiding in identifying targets for credential access in AD environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ms-Mcs-AdmPwd | LAPS password attribute (no substitution needed) | N/A |
| ms-Mcs-AdmPwdExpirationTime | Expiration timestamp attribute (filter uses wildcard) | N/A |

(No user-defined variables; relies on AD module context. Ensure Import-Module ActiveDirectory is run first.)

## Usage

Execute this in a PowerShell session on a domain-joined Windows machine with AD tools installed. It is typically the first step in LAPS abuse procedures to list vulnerable computers before targeting specific ones. Pipe output to Export-Csv for logging: `... | Export-Csv laps_computers.csv -NoTypeInformation`.

## Detection

- Monitor PowerShell execution logs (Event ID 4104) for Get-ADComputer cmdlets querying LAPS attributes.
- AD audit logs (Event ID 4662) for attribute reads on computer objects.
- Anomalous queries from non-admin accounts to ms-Mcs-AdmPwd.

## Related

- [[procedures/Abusing-Active-Directory-ACLs-ACEs-to-Retrieve-LAPS-Passwords]]
- [[tools/ActiveDirectoryModule]]
