---
id: 49e92cda-7a3b-4ffb-848a-8eb2433a60e9
name: 2FA Bypass via Force Browsing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.960614+00:00'
updated_at: '2023-04-06T03:55:53.973875+00:00'
tactics:
  - '[[Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[Brute Force|T1110 - Brute Force]]'
tags:
  - '[[2FA Bypasses]]'
  - '[[Account Takeover]]'
  - '[[Bypass 2FA by Force Browsing]]'
  - authentication-bypass
  - web-vulnerability
  - bypass-technique
commands:
  - '[[Navigate to My Account page]]'
ports:
  - 80
  - 443
services:
  - HTTP
  - HTTPS
platforms:
  - Web
mitre_tactics:
  - Initial Access
mitre_techniques:
  - T1078
  - T1190
  - T1621
title: Bypassing Two-Factor Authentication via Forced Browsing
---

# 2FA Bypass via Force Browsing

## Summary

Bypassing 2FA by force browsing is an attack technique that allows an attacker to bypass 2FA authentication by directly accessing the authenticated page without the 2FA check. This technique works when the application does not properly validate the 2FA code and allows the user to access the page wi

## Description

# Description

Bypassing 2FA by force browsing is an attack technique that allows an attacker to bypass 2FA authentication by directly accessing the authenticated page without the 2FA check. This technique works when the application does not properly validate the 2FA code and allows the user to access the page without it. Attackers can use this technique to gain unauthorized access to a user's account and steal sensitive information or perform malicious activities. This technique is commonly used in phishing attacks to steal user credentials and bypass 2FA authentication.

 

## Requirements

1. Access to the authenticated page

1. Knowledge of the URL structure

 

## Defense

1. Ensure proper validation of 2FA codes

1. Implement multi-factor authentication

1. Monitor for suspicious activities and unauthorized access

 

## Objectives

1. Gain unauthorized access to a user's account

1. Steal sensitive information

1. Perform malicious activities

 

# Instructions

1. 

 



**Code**: [[/my-account]]



> This command instructs the attacker to access the authenticated page and try to bypass 2FA authentication by replacing the /my-account URL with /2fa/verify. If the application does not properly validate the 2FA code, the attacker can gain access to the account without it.



**Command** ([[Navigate to My Account page]]):

```bash
go to /my-account
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Navigate to My Account page]]

## Tags

- [[2FA Bypasses]]
- [[Account Takeover]]
- [[Bypass 2FA by Force Browsing]]


