---
id: 35f722c3-5628-48b5-bbbb-26b8428f27cf
name: Windows - Retail Credential Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.677374+00:00'
updated_at: '2023-04-10T20:37:56.325287+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
tags:
- '[[Get credentials]]'
- '[[Retail Credential]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Login as RetailAdmin]]'
---

# Windows - Retail Credential Theft

## Summary

Retail Credential Theft is a technique used by attackers to gain access to retail accounts and steal sensitive information such as payment card details. This technique involves obtaining the credentials of a retail account and then using these credentials to log in to the account and extract the de

## Description

# Description

Retail Credential Theft is a technique used by attackers to gain access to retail accounts and steal sensitive information such as payment card details. This technique involves obtaining the credentials of a retail account and then using these credentials to log in to the account and extract the desired information. Attackers can obtain these credentials through various means, such as phishing attacks or by purchasing them on the dark web.

From a technical perspective, this technique involves using the 'RetailAdmin Credentials' command to obtain the credentials of a retail account. Once the credentials have been obtained, the attacker can then use them to log in to the account and extract the desired information.

The business value of this technique is that it allows attackers to gain access to sensitive information that can be used for financial gain, such as payment card details. This can result in significant financial losses for the targeted organization.

 

## Requirements

1. Access to the targeted network

1. Credentials for the 'RetailAdmin' account

 

## Defense

1. Implement strong password policies and regular password changes to prevent unauthorized access to credentials

1. Implement multi-factor authentication to add an extra layer of security to accounts

1. Monitor for suspicious activity, such as failed login attempts or unusual login locations

 

## Objectives

1. Obtain credentials for a retail account

1. Use the obtained credentials to log in to the retail account

1. Extract sensitive information from the retail account

 

# Instructions

1. To use these credentials, enter the username and password when prompted.

 



**Code**: [[Username: RetailAdmin
Password: trs10]]



> The RetailAdmin credentials are used to access a retail system. The username is 'RetailAdmin' and the password is 'trs10'. These credentials are provided as a convenience and should be changed immediately after use.



**Command** ([[Login as RetailAdmin]]):

```bash
Username: RetailAdmin
Password: trs10
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]

## Commands Used

- [[Login as RetailAdmin]]

## Tags

- [[Get credentials]]
- [[Retail Credential]]
- [[Windows - Using credentials]]


