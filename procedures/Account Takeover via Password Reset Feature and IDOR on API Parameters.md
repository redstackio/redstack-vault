---
id: 992d10de-acec-46f3-bfa2-ac06fb20c709
name: Account Takeover via Password Reset Feature and IDOR on API Parameters
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.859187+00:00'
updated_at: '2023-04-06T03:55:53.870380+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Account Takeover]]'
- '[[IDOR on API Parameters]]'
- '[[Password Reset Feature]]'
commands:
- '[[Change Password]]'
---

# Account Takeover via Password Reset Feature and IDOR on API Parameters

## Summary

This procedure involves exploiting an insecure password reset feature and an Insecure Direct Object Reference (IDOR) vulnerability in an API parameter to gain unauthorized access to a victim's account. The attacker first identifies the victim's email address or user ID and then sends a request to c

## Description

# Description

This procedure involves exploiting an insecure password reset feature and an Insecure Direct Object Reference (IDOR) vulnerability in an API parameter to gain unauthorized access to a victim's account. The attacker first identifies the victim's email address or user ID and then sends a request to change the victim's password via the API. Since the API endpoint does not properly validate the user ID/email, the attacker can change the victim's password and take over their account.

This attack can be used to gain access to sensitive information or perform unauthorized actions on behalf of the victim, such as transferring funds or stealing confidential data. Businesses can suffer reputational damage and financial losses as a result of such attacks.

 

## Requirements

1. Access to the target's password reset feature

1. Knowledge of the victim's email address or user ID

1. Access to the target's API endpoint

 

## Defense

1. Implement proper input validation and access controls on the password reset feature and API endpoints to prevent IDOR attacks

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

1. Monitor for suspicious activity, such as multiple failed login attempts or changes to account information

 

## Objectives

1. Gain unauthorized access to a victim's account

1. Perform unauthorized actions on behalf of the victim

1. Steal sensitive information

 

# Instructions

1. Follow these steps to execute the attack:

 



**Code**: [[POST /api/changepass
[...]
("form": {"email":"vict]]



> 1. Identify the victim's email address or user ID
2. Send a POST request to the target's API endpoint with the victim's email address/user ID and the new password
3. If the attack is successful, the victim's password will be changed and the attacker will have access to their account



**Command** ([[Change Password]]):

```bash
POST /api/changepass
("form": {"email":"victim@email.com","password":"securepwd"})
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Change Password]]

## Tags

- [[Account Takeover]]
- [[IDOR on API Parameters]]
- [[Password Reset Feature]]


