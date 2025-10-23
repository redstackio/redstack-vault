---
id: f6d436f9-082f-43ba-a0f9-f3a4f27794ea
name: Golden Ticket Generation with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.272004+00:00'
updated_at: '2023-04-10T20:37:17.670142+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Golden ticket]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Create Golden Ticket]]'
---

# Golden Ticket Generation with Mimikatz

## Summary

Golden Ticket Generation with Mimikatz is a technique used to gain unauthorized access to a Windows environment by forging Kerberos tickets. This technique allows an attacker to remain persistent in a network even if the domain password is changed. Mimikatz is a powerful post-exploitation tool that

## Description

# Description

Golden Ticket Generation with Mimikatz is a technique used to gain unauthorized access to a Windows environment by forging Kerberos tickets. This technique allows an attacker to remain persistent in a network even if the domain password is changed. Mimikatz is a powerful post-exploitation tool that can extract plaintext passwords, hash, and Kerberos tickets from memory. With this information, an attacker can create a Golden Ticket that grants access to any resource in the domain. The business value of this attack is that it can allow an attacker to gain access to sensitive data or systems without being detected.

 

## Requirements

1. Local Administrator access to a Windows system

1. Mimikatz tool

 

## Defense

1. Implement strong password policies and password rotation procedures

1. Monitor for suspicious activity in Kerberos ticket logs

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Gain unauthorized access to a Windows environment

1. Remain persistent in a network

 

# Instructions

1. Use mimikatz to generate a Kerberos Golden Ticket. This command requires administrative privileges on the domain controller.

 



**Code**: [[.\mimikatz kerberos::golden /admin:ADMINACCOUNTNAM]]



> The 'kerberos::golden' command in mimikatz generates a Kerberos Golden Ticket, which can be used to authenticate as any user in the domain. The command requires several arguments:
- /admin:ADMINACCOUNTNAME: the name of an administrative account on the domain controller
- /domain:DOMAINFQDN: the fully-qualified domain name of the domain
- /id:ACCOUNTRID: the RID (relative identifier) of the account you wish to impersonate
- /sid:DOMAINSID: the security identifier (SID) of the domain
- /krbtgt:KRBTGTPASSWORDHASH: the password hash of the KRBTGT account, which is used to encrypt the ticket
- /ptt: this flag tells mimikatz to inject the ticket into the current process, which allows you to use it immediately for authentication.



**Command** ([[Create Golden Ticket]]):

```bash
.\mimikatz kerberos::golden /admin:ADMINACCOUNTNAME /domain:DOMAINFQDN /id:ACCOUNTRID /sid:DOMAINSID /krbtgt:KRBTGTPASSWORDHASH /ptt
```



2. This command uses Mimikatz to create a golden ticket. The golden ticket is a forged Kerberos ticket that can be used to authenticate as any user in the domain. The command requires the following arguments:
- /admin: the username of a domain admin
- /domain: the name of the domain
- /id: the ID of the user to impersonate
- /sid: the SID of the user to impersonate
- /krbtgt: the NTLM hash of the domain krbtgt account
- /startoffset: the time offset (in minutes) to use for the ticket's starttime
- /endin: the duration (in minutes) of the ticket
- /renewmax: the maximum duration (in minutes) that the ticket can be renewed
- /ptt: injects the ticket into the current process

 



**Code**: [[.\mimikatz "kerberos::golden /admin:DarthVader /do]]



> This command is typically used by attackers to gain access to a domain by creating a forged Kerberos ticket that can be used to authenticate as any user in the domain. It requires knowledge of the domain admin username, the domain name, the ID and SID of the user to impersonate, and the NTLM hash of the domain krbtgt account. The ticket is injected into the current process, allowing the attacker to use it to access resources on the domain as the impersonated user.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Create Golden Ticket]]

## Tags

- [[Golden ticket]]
- [[Windows - Mimikatz]]


