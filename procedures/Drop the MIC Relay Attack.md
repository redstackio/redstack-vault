---
id: 58f343e1-aed7-470f-9230-9e96028ef806
name: Drop the MIC Relay Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.508646+00:00'
updated_at: '2023-04-10T20:26:24.513325+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Drop the MIC]]'
- '[[Man-in-the-Middle attacks & relaying]]'
commands:
- '[[CVE-2019-1040 Scanner]]'
---

# Drop the MIC Relay Attack

## Summary

The Drop the MIC (Microsoft Integrity Check) attack is a technique used to relay authentication attempts to a target system. This technique can be used to elevate privileges and gain access to sensitive data. The attack works by intercepting authentication requests between a client and a server and

## Description

# Description

The Drop the MIC (Microsoft Integrity Check) attack is a technique used to relay authentication attempts to a target system. This technique can be used to elevate privileges and gain access to sensitive data. The attack works by intercepting authentication requests between a client and a server and then relaying them to a target system. This allows an attacker to impersonate a legitimate user and gain access to resources that they would not normally have access to.

Technical Explanation: The attack is possible due to a flaw in the Microsoft Windows implementation of the Kerberos authentication protocol. Specifically, the flaw is in the way that the protocol handles the MIC field, which is used to ensure the integrity of the authentication message. By manipulating the MIC field, an attacker can bypass the integrity check and successfully relay the authentication request.

Business Value: This attack can be used to gain access to sensitive data and elevate privileges, which can lead to data theft, financial loss, and reputational damage.

 

## Requirements

1. Access to a network with vulnerable systems

1. A system to act as a relay

1. Tools to intercept and manipulate authentication requests

 

## Defense

1. Implementing secure authentication protocols, such as multi-factor authentication

1. Limiting access to sensitive data to only those who need it

1. Monitoring network traffic for signs of authentication relaying

 

## Objectives

1. Gain access to sensitive data

1. Elevate privileges

 

# Instructions

1. To check if a target is vulnerable to CVE-2019-1040, run the following command: `python2 scanMIC.py 'DOMAIN/USERNAME:PASSWORD@TARGET'`

 



**Code**: [[python2 scanMIC.py 'DOMAIN/USERNAME:PASSWORD@TARGE]]



> This command checks if a target is vulnerable to CVE-2019-1040, a security vulnerability that allows an attacker to bypass NTLM authentication. The `DOMAIN/USERNAME:PASSWORD` parameter specifies the credentials to use for authentication, and `TARGET` specifies the IP address or hostname of the target machine. If the target is vulnerable, the command will return a message indicating so. If the target is not vulnerable, the command will return a message indicating that authentication was rejected.



**Command** ([[CVE-2019-1040 Scanner]]):

```bash
python2 scanMIC.py 'DOMAIN/USERNAME:PASSWORD@TARGET'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[CVE-2019-1040 Scanner]]

## Tags

- [[Active Directory Attacks]]
- [[Drop the MIC]]
- [[Man-in-the-Middle attacks & relaying]]


