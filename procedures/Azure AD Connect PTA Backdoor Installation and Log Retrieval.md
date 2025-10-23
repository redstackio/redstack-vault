---
id: a84aa69d-3774-49ef-8030-4aa120cca2d2
name: Azure AD Connect PTA Backdoor Installation and Log Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.122719+00:00'
updated_at: '2023-04-10T20:19:23.356546+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Data Encrypted|T1022 - Data Encrypted]]'
- '[[File Deletion|T1107 - File Deletion]]'
tags:
- '[[Azure AD Connect]]'
- '[[Cloud - Azure]]'
commands:
- '[[Get AADIntPTASpy Log - Decode Passwords]]'
- '[[Install AADIntPTASpy]]'
---

# Azure AD Connect PTA Backdoor Installation and Log Retrieval

## Summary

This procedure involves installing a backdoor on Azure AD Connect to gain persistent access to the target environment. The attacker can then retrieve logs from the backdoor to gain further information about the target. This attack can be used to gain access to sensitive data, escalate privileges, a

## Description

# Description

This procedure involves installing a backdoor on Azure AD Connect to gain persistent access to the target environment. The attacker can then retrieve logs from the backdoor to gain further information about the target. This attack can be used to gain access to sensitive data, escalate privileges, and move laterally within the target environment.

To install the backdoor, the attacker first gains access to the Azure AD Connect server. They then install the backdoor, which can be configured to encrypt the data it sends back to the attacker. The attacker can then retrieve logs from the backdoor to gain further information about the target. This attack can be used to gain access to sensitive data, escalate privileges, and move laterally within the target environment.

The business value of this attack is that it allows the attacker to gain access to sensitive data and potentially compromise the entire target environment. This can lead to significant financial and reputational damage for the target organization.

 

## Requirements

1. Access to the Azure AD Connect server

1. Credentials with sufficient privileges to install the backdoor

1. Ability to communicate with the backdoor to retrieve logs

 

## Defense

1. Implement strong access controls to prevent unauthorized access to the Azure AD Connect server

1. Monitor for suspicious activity on the server, such as unexpected changes to system files or new user accounts

1. Implement network segmentation to limit the impact of a compromise to a single segment of the network

 

## Objectives

1. Gain persistent access to the target environment

1. Retrieve logs from the backdoor to gain further information about the target

1. Escalate privileges and move laterally within the target environment

 

# Instructions

1. To install a PTA backdoor, run the command 'Install-AADIntPTASpy' in PowerShell. This will install the backdoor on the target system. To retrieve logs from the backdoor, run the command 'Get-AADIntPTASpyLog -DecodePasswords' in PowerShell.

 



**Code**: [[PS AADInternals> Install-AADIntPTASpy
PS AADIntern]]



> This command installs a backdoor on the target system, allowing for remote access and control. The 'Get-AADIntPTASpyLog' command is used to retrieve logs from the backdoor, which can contain sensitive information such as passwords. The '-DecodePasswords' argument can be used to decode any encoded passwords found in the logs.



**Command** ([[Install AADIntPTASpy]]):

```bash
Install-AADIntPTASpy
```





**Command** ([[Get AADIntPTASpy Log - Decode Passwords]]):

```bash
Get-AADIntPTASpyLog -DecodePasswords
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Data Encrypted|T1022 - Data Encrypted]]
- [[File Deletion|T1107 - File Deletion]]

## Commands Used

- [[Get AADIntPTASpy Log - Decode Passwords]]
- [[Install AADIntPTASpy]]

## Tags

- [[Azure AD Connect]]
- [[Cloud - Azure]]


