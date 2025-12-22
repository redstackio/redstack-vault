---
id: 687ad6c5-203c-46c8-b61e-533d26ba97aa
name: Invoke-ACL-PS1-for-AD-ACL-Abuse
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.826409+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-abuse
  - privilege-escalation
validated: true
---

# Invoke-ACL-PS1-for-AD-ACL-Abuse

## Code

```powershell
./Invoke-ACL.ps1 -SharpHoundLocation .\sharphound.exe -mimikatzLocation .\mimikatz.exe -Username 'user1' -Domain 'domain.local' -Password 'Welcome01!'
```

## Description

This PowerShell script invocation automates the discovery and exploitation of unsafe ACL configurations in Active Directory. It integrates SharpHound for collecting AD relationship and permission data (including weak ACLs) and Mimikatz for extracting and cracking credentials from vulnerable service accounts or objects, enabling privilege escalation and lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| SharpHoundLocation | File path to the SharpHound executable | .\sharphound.exe |
| mimikatzLocation | File path to the Mimikatz executable | .\mimikatz.exe |
| Username | Domain username for authentication | user1 |
| Domain | Target Active Directory domain FQDN | domain.local |
| Password | Plaintext password for the username | Welcome01! |

## Usage

Execute this on a compromised domain-joined Windows host with initial credentials. The script first runs SharpHound to enumerate AD (outputting JSON with ACL paths), then uses Mimikatz to target weak points for credential theft. Ideal for red teaming after initial access; follow up by using dumped creds for DCSync or Golden Ticket attacks. Ensure binaries are staged locally to avoid detection.

## Detection

- PowerShell execution logs (Event ID 4104) showing script invocation with SharpHound/Mimikatz paths.
- Process creation for sharphound.exe and mimikatz.exe (Sysmon Event ID 1) with unusual parent (powershell.exe).
- AD audit logs (Event ID 4624/4672) for anomalous logons or permission changes post-exploitation.
- Network traffic to DCs on LDAP (389/636) or SMB (445) from non-admin hosts.
- AMSI scans flagging Mimikatz signatures or LSASS access (Event ID 10).

## Related

- [[procedures/Abuse-Active-Directory-ACLs-Using-WriteDACL-and-Invoke-ACL-Tool]]
- [[tools/SharpHound]]
- [[tools/Mimikatz]]
