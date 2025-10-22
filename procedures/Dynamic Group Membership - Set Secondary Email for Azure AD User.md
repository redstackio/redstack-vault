---
id: 30390063-f426-4b33-8a88-a2f6c21f01fc
name: Dynamic Group Membership - Set Secondary Email for Azure AD User
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.824351+00:00'
updated_at: '2023-04-10T20:19:27.822091+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Cloud - Azure]]'
- '[[Dynamic Group Membership]]'
commands:
- '[[Add other email to Azure AD user]]'
---

# Dynamic Group Membership - Set Secondary Email for Azure AD User

## Summary

The Dynamic Group Membership - Set Secondary Email for Azure AD User procedure is a method of gaining initial access to an Azure Active Directory (AD) environment. This procedure involves setting a secondary email for an Azure AD user, which can be used for password resets or as a phishing target. 

## Description

# Description

The Dynamic Group Membership - Set Secondary Email for Azure AD User procedure is a method of gaining initial access to an Azure Active Directory (AD) environment. This procedure involves setting a secondary email for an Azure AD user, which can be used for password resets or as a phishing target. The attacker can then use this email to gain access to the Azure AD environment and potentially move laterally to other systems.

To execute this procedure, the attacker needs to have valid credentials for an Azure AD user. This can be achieved through phishing or other methods of obtaining credentials. The attacker can then use the 'Set Secondary Email for Azure AD User' command to set a secondary email for the user, which can be used for password resets or as a phishing target.

The business value of this procedure lies in the fact that it can be used to gain initial access to an Azure AD environment, which can then be used to access sensitive data or systems. This can lead to data theft, espionage, or other malicious activities.

## Requirements

1. Valid credentials for an Azure AD user

## Defense

1. Implement multi-factor authentication for Azure AD users to prevent unauthorized access

1. Monitor Azure AD logs for suspicious activity, such as changes to user accounts or group memberships

1. Educate users on the dangers of phishing attacks and how to identify them

## Objectives

1. Gain initial access to an Azure AD environment

1. Set a secondary email for an Azure AD user

1. Use the secondary email for password resets or as a phishing target

# Instructions

1. Use this command to set the secondary email for an Azure AD user. Replace <OBJECT-ID> with the ID of the user you want to modify and <Username> and <TENANT NAME> with the desired email address and your tenant name respectively.

**Code**: [[PS> Set-AzureADUser -ObjectId <OBJECT-ID> -OtherMa]]

> -ObjectId: The ID of the user you want to modify.
-OtherMails: The secondary email address you want to set for the user.
-Verbose: Optional parameter to provide verbose output for the command.

**Command** ([[Add other email to Azure AD user]]):

```bash
Set-AzureADUser -ObjectId <OBJECT-ID> -OtherMails <Username>@<TENANT NAME>.onmicrosoft.com -Verbose
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Phishing|T1566 - Phishing]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Add other email to Azure AD user]]

## Tags

- [[Cloud - Azure]]
- [[Dynamic Group Membership]]
