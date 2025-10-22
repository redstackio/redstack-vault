---
id: 3d2cf63a-1e31-4349-82d2-6a2d6302f573
name: Facebook Access Token Leakage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.114842+00:00'
updated_at: '2023-04-06T03:55:53.128187+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials in Registry|T1552.002 - Credentials in Registry]]'
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[API Key Leaks]]'
- '[[Exploit]]'
- '[[Facebook Access Token]]'
commands:
- '[[Facebook Access Token Debugging]]'
---

# Facebook Access Token Leakage

## Summary

Facebook Access Token Leakage is a technique used to obtain Facebook Access Tokens. Access Tokens are used to authenticate a user or application to an API. An attacker can obtain an Access Token by exploiting vulnerabilities in an application or by obtaining the token from a user. Once the attacker

## Description

# Description

Facebook Access Token Leakage is a technique used to obtain Facebook Access Tokens. Access Tokens are used to authenticate a user or application to an API. An attacker can obtain an Access Token by exploiting vulnerabilities in an application or by obtaining the token from a user. Once the attacker has the Access Token, they can use it to perform actions on behalf of the user or application. This technique can be used to gain access to user data or to perform actions that the user or application is authorized to perform. The attacker can then use this information to further compromise the system or to gain access to other systems.

## Requirements

1. Valid Facebook Access Token

## Defense

1. Ensure that all Facebook Access Tokens are properly secured and not leaked

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

1. Monitor for suspicious activity and unauthorized access to user data

## Objectives

1. Obtain Facebook Access Tokens

1. Perform actions on behalf of the user or application

# Instructions

1. Replace ACCESS_TOKEN_HERE with the Access Token you want to debug.

**Code**: [[curl https://developers.facebook.com/tools/debug/a]]

> This command will provide detailed information about the Access Token, including the user ID, expiration time, and permissions granted to the application. This information can be used to further compromise the system or to gain access to other systems.

**Command** ([[Facebook Access Token Debugging]]):

```bash
curl https://developers.facebook.com/tools/debug/accesstoken/?access_token=ACCESS_TOKEN_HERE&version=v3.2
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Registry|T1552.002 - Credentials in Registry]]
- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Facebook Access Token Debugging]]

## Tags

- [[API Key Leaks]]
- [[Exploit]]
- [[Facebook Access Token]]
