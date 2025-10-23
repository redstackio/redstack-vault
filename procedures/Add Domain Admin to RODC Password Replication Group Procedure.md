---
id: 2b9b06ca-b490-4226-8613-27673a0099fa
name: Add Domain Admin to RODC Password Replication Group Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.366454+00:00'
updated_at: '2023-04-10T20:26:02.526383+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Active Directory Attacks]]'
- '[[RODC Computer Object]]'
- '[[RODC - Read Only Domain Controller]]'
commands:
- '[[Set Domain Object]]'
---

# Add Domain Admin to RODC Password Replication Group Procedure

## Summary

The Add Domain Admin to RODC Password Replication Group procedure is an attack technique used to gain access to an RODC (Read Only Domain Controller) by adding a Domain Admin account to the Password Replication Group. This procedure can be used to escalate privileges and gain access to sensitive in

## Description

# Description

The Add Domain Admin to RODC Password Replication Group procedure is an attack technique used to gain access to an RODC (Read Only Domain Controller) by adding a Domain Admin account to the Password Replication Group. This procedure can be used to escalate privileges and gain access to sensitive information. 

Technical Description: An attacker can use this procedure to add a Domain Admin account to the Password Replication Group of an RODC, which will allow the attacker to obtain the password hashes of the Domain Admin account. The attacker can then use these hashes to authenticate to other systems within the domain. 

Business Value: This procedure can be used by attackers to gain access to sensitive information, such as intellectual property, financial data, and personal information. This can result in financial loss, reputational damage, and legal liability.

 

## Requirements

1. Access to the RODC

1. Authenticated access to the domain

 

## Defense

1. Limit access to RODCs to authorized personnel only

1. Monitor the RODC for changes to the Password Replication Group

1. Implement multi-factor authentication to prevent unauthorized access to domain accounts

 

## Objectives

1. Escalate privileges

1. Gain access to sensitive information

 

# Instructions

1. To add a domain admin account to the RODC's **msDS-RevealOnDemandGroup** attribute, use the following command:

 



**Code**: [[PowerSploit> Set-DomainObject -Identity RODC$ -Set]]



> This command sets the **msDS-RevealOnDemandGroup** attribute of the RODC object to include the **Allowed RODC Password Replication Group** and **Administrator** accounts. By adding the domain admin account to this group, the account will be able to replicate its password to the RODC, allowing it to authenticate users even when the writable domain controllers are offline. This is useful for remote sites with low bandwidth connections to the main data center.



**Command** ([[Set Domain Object]]):

```bash
PowerSploit> Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Set Domain Object]]

## Tags

- [[Active Directory Attacks]]
- [[RODC Computer Object]]
- [[RODC - Read Only Domain Controller]]


