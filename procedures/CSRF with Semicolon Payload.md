---
id: 2a960ef8-01d0-438d-9437-49368b930c1b
name: CSRF with Semicolon Payload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.651830+00:00'
updated_at: '2023-04-06T03:55:55.669434+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Spearphishing Attachment|T1193 - Spearphishing Attachment]]'
tags:
- '[[Bypass referer header validation]]'
- '[[Cross-Site Request Forgery]]'
- '[[With semicolon(`;`) payload]]'
commands:
- '[[Open CSRF page]]'
- '[[Set Referer header]]'
---

# CSRF with Semicolon Payload

## Summary

A CSRF attack with a semicolon payload is a type of attack where an attacker can trick a user into performing an action on a website without their knowledge or consent. This attack is possible because the website does not properly validate the referer header. The attacker can then use a semicolon p

## Description

# Description

A CSRF attack with a semicolon payload is a type of attack where an attacker can trick a user into performing an action on a website without their knowledge or consent. This attack is possible because the website does not properly validate the referer header. The attacker can then use a semicolon payload to bypass the referer header validation and perform actions on the user's behalf. This attack can be used to steal sensitive information or perform unauthorized actions on the user's behalf. The business value of this attack lies in the ability to bypass security controls and gain unauthorized access to sensitive data or systems.

 

## Requirements

1. Access to a website with CSRF vulnerability

1. Ability to send a malicious link to the victim

 

## Defense

1. Implement referer validation to ensure that the referer header matches the expected value

1. Use anti-CSRF tokens to prevent CSRF attacks

1. Educate users on the risks of clicking on links from unknown sources

 

## Objectives

1. Perform unauthorized actions on the user's behalf

1. Steal sensitive information

 

# Instructions

1. Send a malicious link to the victim

 

The attacker sends a link to the victim that contains a semicolon payload. When the victim clicks on the link, the website is opened with the semicolon payload in the referer header. The website does not properly validate the referer header and performs the action on the user's behalf.



**Command** ([[Open CSRF page]]):

```bash
Open https://attacker.com/csrf.html;trusted.domain.com
```





**Command** ([[Set Referer header]]):

```bash
Referer: https://attacker.com/csrf.html;trusted.domain.com
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Spearphishing Attachment|T1193 - Spearphishing Attachment]]

## Commands Used

- [[Open CSRF page]]
- [[Set Referer header]]

## Tags

- [[Bypass referer header validation]]
- [[Cross-Site Request Forgery]]
- [[With semicolon(`;`) payload]]


