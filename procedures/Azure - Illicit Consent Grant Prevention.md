---
id: 1d412a6f-3c64-4c9f-ae91-0991e1660eca
name: Azure - Illicit Consent Grant Prevention
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.144307+00:00'
updated_at: '2023-04-10T20:19:38.026650+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
tags:
- '[[Cloud - Azure]]'
- '[[Illicit Consent Grant]]'
- '[[Setup Vajra]]'
commands:
- '[[Update registry value]]'
---

# Azure - Illicit Consent Grant Prevention

## Summary

This procedure aims to prevent the abuse of Azure's user consent mechanism by malicious actors. Illicit consent grants can allow attackers to gain access to sensitive resources without the knowledge or permission of the resource owner. By disallowing user consent, this procedure helps to mitigate t

## Description

# Description

This procedure aims to prevent the abuse of Azure's user consent mechanism by malicious actors. Illicit consent grants can allow attackers to gain access to sensitive resources without the knowledge or permission of the resource owner. By disallowing user consent, this procedure helps to mitigate this risk. From an offensive perspective, attackers may attempt to abuse user consent in order to gain access to sensitive resources or data. From a technical standpoint, this procedure involves disabling the ability for users to grant consent to applications. The business value of this procedure is that it helps to protect sensitive data and resources from unauthorized access.

 

## Requirements

1. Access to Azure portal

1. Permissions to modify Azure Active Directory settings

 

## Defense

1. Regularly review and audit Azure Active Directory settings

1. Implement multi-factor authentication for all users

1. Enforce strict access controls and permissions

 

## Objectives

1. Prevent the abuse of Azure's user consent mechanism

1. Mitigate the risk of illicit consent grants

1. Protect sensitive data and resources from unauthorized access

 

# Instructions

1. To disallow user consent, add the following line to your code:

 



**Code**: [[Do not allow user consent]]



> This command prevents users from giving their consent to certain actions or data collection. It is useful for maintaining privacy and security in certain applications or websites.



**Command** ([[Update registry value]]):

```bash
REG ADD HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors /v DisableLocation /t REG_DWORD /d 1 /f
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]

## Commands Used

- [[Update registry value]]

## Tags

- [[Cloud - Azure]]
- [[Illicit Consent Grant]]
- [[Setup Vajra]]


