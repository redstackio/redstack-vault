---
id: a48b8860-77fd-4cce-afff-f0698b828fb5
name: SAML Injection for Authentication Bypass and Signature Stripping with Admin
  NameID
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.139423+00:00'
updated_at: '2023-04-10T20:23:27.929132+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Email Collection|T1114 - Email Collection]]'
- '[[Regsvr32|T1117 - Regsvr32]]'
tags:
- '[[Authentication Bypass]]'
- '[[SAML Injection]]'
- '[[Signature Stripping]]'
commands:
- '[[Set NameID to admin]]'
---

# SAML Injection for Authentication Bypass and Signature Stripping with Admin NameID

## Summary

SAML injection is an attack that exploits vulnerabilities in the SAML authentication process. By crafting a malicious SAML response, an attacker can bypass authentication and gain unauthorized access to a system. In this specific procedure, the attacker uses a SAML assertion with an Admin NameID to

## Description

# Description

SAML injection is an attack that exploits vulnerabilities in the SAML authentication process. By crafting a malicious SAML response, an attacker can bypass authentication and gain unauthorized access to a system. In this specific procedure, the attacker uses a SAML assertion with an Admin NameID to bypass authentication and gain admin privileges. Additionally, the attacker strips the signature from the SAML response to avoid detection. This attack can be used for credential theft, lateral movement, and other malicious activities.

From a technical standpoint, SAML injection involves manipulating the SAML response by modifying the XML data. The attacker can change the NameID field to an admin user, and remove the signature to avoid detection. This attack is possible when the SAML implementation is not properly configured or does not validate the response correctly.

From a business perspective, this attack can have severe consequences. An attacker with admin privileges can access sensitive data, modify configurations, and cause significant damage to the organization. This procedure can be used by malicious actors to gain access to high-value targets, such as financial institutions, government agencies, or healthcare organizations.

 

## Requirements

1. Access to the target SAML implementation

1. Knowledge of the SAML protocol and injection techniques

1. Tools for crafting and sending malicious SAML responses

 

## Defense

1. Implement proper configuration and validation of SAML responses

1. Use multi-factor authentication to mitigate the risk of credential theft

1. Monitor for suspicious SAML responses and unusual admin activity

 

## Objectives

1. Bypass authentication and gain admin privileges

1. Steal credentials and perform lateral movement

1. Access sensitive data and modify configurations

 

# Instructions

1. To generate a SAML assertion with an admin NameID, follow these steps:
1. Open your SAML service provider.
2. Navigate to the settings for your SAML integration.
3. Locate the 'NameID' field and enter 'admin'.
4. Save your changes and generate a new SAML assertion.

 



**Code**: [[NameID=admin]]



> The 'NameID' field in a SAML assertion identifies the user or entity that is being authenticated. In this example, the NameID is set to 'admin', indicating that the user being authenticated is an administrator. The SAML assertion can be generated using a SAML service provider and can be used for single sign-on (SSO) authentication with a SAML identity provider (IdP).



**Command** ([[Set NameID to admin]]):

```bash
NameID=admin
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Email Collection|T1114 - Email Collection]]
- [[Regsvr32|T1117 - Regsvr32]]

## Commands Used

- [[Set NameID to admin]]

## Tags

- [[Authentication Bypass]]
- [[SAML Injection]]
- [[Signature Stripping]]


