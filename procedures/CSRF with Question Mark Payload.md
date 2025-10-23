---
id: 39590323-17f5-4e99-9366-cd0d268a1a0e
name: CSRF with Question Mark Payload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.346123+00:00'
updated_at: '2023-04-10T20:21:27.598559+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Bypass referer header validation]]'
- '[[Cross-Site Request Forgery]]'
- '[[With question mark(`?`) payload]]'
commands:
- '[[Open CSRF page]]'
- '[[Set Referer header]]'
---

# CSRF with Question Mark Payload

## Summary

Cross-Site Request Forgery (CSRF) is a type of attack that tricks a user into performing an action they did not intend to do. A common way to bypass referer header validation is to use a question mark payload. The attacker can craft a URL with a question mark payload that will be executed by the vi

## Description

# Description

Cross-Site Request Forgery (CSRF) is a type of attack that tricks a user into performing an action they did not intend to do. A common way to bypass referer header validation is to use a question mark payload. The attacker can craft a URL with a question mark payload that will be executed by the victim's browser. This technique is often used to perform actions such as changing a user's password or transferring funds. This attack can be executed from a malicious website, email, or other means of social engineering.

Technical Explanation: The attacker crafts a URL with a question mark payload that will be executed by the victim's browser. The payload can include parameters that will execute an action on the victim's behalf. The victim's browser will include the referer header, which is used to validate the request. However, the attacker can bypass this validation by using a question mark payload.

Business Value: CSRF attacks can result in unauthorized access to user accounts, financial loss, and reputational damage to the organization. By exploiting CSRF vulnerabilities, attackers can steal sensitive information, perform unauthorized transactions, and gain access to the victim's account.

 

## Requirements

1. Victim must be logged in to the trusted domain

 

## Defense

1. Implement CSRF tokens to validate requests

1. Use SameSite cookies to prevent cross-site request forgery

1. Implement multi-factor authentication to prevent unauthorized access

 

## Objectives

1. To execute unauthorized actions on behalf of the victim

 

# Instructions

1. 

 

The command contains a URL with a question mark payload. The victim must be logged in to the trusted domain for the attack to be successful. The attacker sends the URL to the victim, who clicks on the link. The victim's browser executes the payload, which can include parameters to perform an action on the victim's behalf. The referer header is included in the request, but the attacker can bypass this validation by using a question mark payload.



**Command** ([[Open CSRF page]]):

```bash
Open https://attacker.com/csrf.html?trusted.domain.com
```





**Command** ([[Set Referer header]]):

```bash
Referer: https://attacker.com/csrf.html?trusted.domain.com
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[Open CSRF page]]
- [[Set Referer header]]

## Tags

- [[Bypass referer header validation]]
- [[Cross-Site Request Forgery]]
- [[With question mark(`?`) payload]]


