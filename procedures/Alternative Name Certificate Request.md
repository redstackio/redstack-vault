---
id: a35c5260-3ad8-4be2-b2af-7944c9f35d0c
name: Alternative Name Certificate Request
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.904251+00:00'
updated_at: '2023-04-10T20:26:09.214843+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Indirect Command Execution|T1202 - Indirect Command Execution]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[ESC6 - EDITF_ATTRIBUTESUBJECTALTNAME2]]'
commands:
- '[[Certify.exe cas]]'
- '[[Certify.exe request for User template with alternate name DomAdmin]]'
---

# Alternative Name Certificate Request

## Summary

This procedure involves requesting a user certificate with an alternative name, which can be used to bypass certain security controls. Attackers can use this technique to gain access to sensitive information or systems. To request the certificate, the Check UserSpecifiedSAN flag state with Certify.

## Description

# Description

This procedure involves requesting a user certificate with an alternative name, which can be used to bypass certain security controls. Attackers can use this technique to gain access to sensitive information or systems. To request the certificate, the Check UserSpecifiedSAN flag state with Certify.exe command is used to check if the flag is enabled. If it is, the Request User Certificate with Alternative Name command can be used to request the certificate. This technique can be used as part of a larger attack campaign or as a standalone tactic.

 

## Requirements

1. Valid user credentials

1. Access to Active Directory Certificate Services

1. Certify.exe tool

 

## Defense

1. Disable the UserSpecifiedSAN flag to prevent attackers from requesting certificates with alternative names

1. Monitor certificate requests for unusual activity

1. Implement network segmentation to limit the impact of a potential attack

 

## Objectives

1. Request a user certificate with an alternative name

1. Bypass security controls to gain access to sensitive information or systems

 

# Instructions

1. To check the UserSpecifiedSAN flag state, run the following command:

```Certify.exe cas```

 



**Code**: [[Certify.exe cas]]



> This command uses Certify.exe, a tool developed by GhostPack, to check for the UserSpecifiedSAN flag state. This flag refers to the `EDITF_ATTRIBUTESUBJECTALTNAME2` flag, which specifies whether the certificate request includes a Subject Alternative Name (SAN) extension that is specified by the user. The output of the command will indicate whether the flag is set or not, providing valuable information for certificate management and troubleshooting.



**Command** ([[Certify.exe cas]]):

```bash
Certify.exe cas
```



2. To request a user certificate with an alternative name, run the following command:

 



**Code**: [[.\Certify.exe request /ca:dc.domain.local\domain-D]]



> This command requests a certificate using the `User` template and adds an alternative name `DomAdmin`. By default, the `User` template does not allow to specify alternative names, but this command enables you to do so.



**Command** ([[Certify.exe request for User template with alternate name DomAdmin]]):

```bash
.\Certify.exe request /ca:dc.domain.local\domain-DC-CA /template:User /altname:DomAdmin
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Indirect Command Execution|T1202 - Indirect Command Execution]]

## Commands Used

- [[Certify.exe cas]]
- [[Certify.exe request for User template with alternate name DomAdmin]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC6 - EDITF_ATTRIBUTESUBJECTALTNAME2]]


