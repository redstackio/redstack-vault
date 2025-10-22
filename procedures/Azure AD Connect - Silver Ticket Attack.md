---
id: 05c206d0-5fdd-4289-bec0-cf4452a3be59
name: Azure AD Connect - Silver Ticket Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.181536+00:00'
updated_at: '2023-04-10T20:19:22.517655+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
- '[[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
tags:
- '[[Azure AD Connect]]'
- '[[Azure AD Connect - Seamless Single Sign On Silver Ticket]]'
- '[[Cloud - Azure]]'
commands:
- '[[DCSync AzureADSSOACC$]]'
---

# Azure AD Connect - Silver Ticket Attack

## Summary

The Azure AD Connect - Silver Ticket Attack is a technique that allows an attacker to create a Silver Ticket for Azure Active Directory (AAD) Group (AADG) and gain unauthorized access to resources in the AAD environment. The attacker can retrieve the NTLM password hash of the AZUREADSSOACC account 

## Description

# Description

The Azure AD Connect - Silver Ticket Attack is a technique that allows an attacker to create a Silver Ticket for Azure Active Directory (AAD) Group (AADG) and gain unauthorized access to resources in the AAD environment. The attacker can retrieve the NTLM password hash of the AZUREADSSOACC account and use it to create a Silver Ticket for AADG. This attack is possible because of the way Azure AD Connect is designed to provide seamless single sign-on (SSO) between on-premises and cloud environments.

From a technical perspective, the Silver Ticket Attack involves creating a forged Kerberos ticket that grants access to a specific service. The attacker can use this ticket to authenticate themselves as a legitimate user and access the resources associated with that user.

The business value of this attack is that it allows an attacker to gain access to sensitive data and resources in the AAD environment, potentially leading to data theft, data manipulation, or further compromise of the organization's systems.

## Requirements

1. Access to the Azure AD Connect server

1. Knowledge of the AZUREADSSOACC account

1. Knowledge of the AADG

## Defense

1. Limit access to the Azure AD Connect server to authorized personnel only

1. Monitor for unusual activity, such as the creation of Silver Tickets or other unauthorized authentication attempts

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

## Objectives

1. Gain unauthorized access to resources in the AAD environment

1. Retrieve sensitive data

1. Manipulate data

1. Further compromise the organization's systems

# Instructions

1. This command uses Mimikatz to retrieve the NTLM password hash of the AZUREADSSOACC account. The account name is specified using the /user argument.

**Code**: [[mimikatz.exe "lsadump::dcsync /user:AZUREADSSOACC$]]

> This command is useful for testing the security of an Active Directory environment. By retrieving the NTLM password hash of a privileged account like AZUREADSSOACC, an attacker could potentially use this hash to gain access to other systems or escalate their privileges within the network. It is important to ensure that privileged accounts have strong passwords and that their password hashes are properly secured.

**Command** ([[DCSync AzureADSSOACC$]]):

```bash
mimikatz.exe "lsadump::dcsync /user:AZUREADSSOACC$" exit
```

2. Run the mimikatz command with the given arguments to create a Silver Ticket for AADG.

**Code**: [[mimikatz.exe "kerberos::golden /user:elrond
/sid:S]]

> The command uses mimikatz to create a Kerberos Golden Ticket with the given user, domain, and SID. The /rc4 argument specifies the NTLM hash of the user's password. The /target argument specifies the target service for the ticket. The /service argument specifies the service type for the ticket. The /ptt argument injects the ticket into the current user's Kerberos cache. This command is useful for lateral movement and privilege escalation within a Windows domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Ticket|T1097 - Pass the Ticket]]
- [[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]

## Commands Used

- [[DCSync AzureADSSOACC$]]

## Tags

- [[Azure AD Connect]]
- [[Azure AD Connect - Seamless Single Sign On Silver Ticket]]
- [[Cloud - Azure]]
