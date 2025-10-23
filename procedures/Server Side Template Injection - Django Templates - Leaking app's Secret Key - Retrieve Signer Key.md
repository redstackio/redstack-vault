---
id: 86930e5b-5bf0-412b-a890-73ccdb374f47
name: Server Side Template Injection - Django Templates - Leaking app's Secret Key
  - Retrieve Signer Key
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.497438+00:00'
updated_at: '2023-04-10T20:23:40.424192+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Django Templates]]'
- '[[Leaking app’s Secret Key]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Retrieve Storage Signer Key]]'
---

# Server Side Template Injection - Django Templates - Leaking app's Secret Key - Retrieve Signer Key

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on a target server. In the context of Django Templates, this vulnerability can be exploited to leak the app's Secret Key, which can be used to perform further attacks. By retrieving the Signer

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on a target server. In the context of Django Templates, this vulnerability can be exploited to leak the app's Secret Key, which can be used to perform further attacks. By retrieving the Signer Key, an attacker can modify the contents of signed cookies, which can lead to session hijacking and other security issues.

To exploit this vulnerability, an attacker needs to inject malicious code into a template that is later rendered on the server. This can be achieved by sending a specially crafted request to the server, or by exploiting a vulnerable component in the application.

The business value of exploiting this vulnerability is that it allows an attacker to gain access to sensitive data and perform actions on behalf of the victim user, which can result in financial loss, reputational damage, and legal consequences.

 

## Requirements

1. Access to the target server

1. Knowledge of the application's technology stack

1. Ability to send requests to the server

 

## Defense

1. Ensure that the application is up to date and all security patches are applied

1. Implement input validation and output encoding to prevent injection attacks

1. Use a Web Application Firewall (WAF) to detect and block malicious requests

 

## Objectives

1. Retrieve the app's Secret Key

1. Retrieve the Signer Key

 

# Instructions

1. To retrieve the signer key, use the following command:

 



**Code**: [[{{ messages.storages.0.signer.key }}]]



> This command retrieves the signer key from the first storage location in the messages object. The signer key is a unique identifier used to sign and verify digital signatures. This command is useful when you need to verify the authenticity of a message or document that has been signed by a specific signer.



**Command** ([[Retrieve Storage Signer Key]]):

```bash
{{ messages.storages.0.signer.key }}
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Retrieve Storage Signer Key]]

## Tags

- [[Django Templates]]
- [[Leaking app’s Secret Key]]
- [[Server Side Template Injection]]


