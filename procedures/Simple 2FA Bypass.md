---
id: 528273ec-5365-45d9-bea6-41f65b5210e7
name: Simple 2FA Bypass
type: procedure
verified: false
submitted: false
created_at: '2020-08-04T16:54:38.989773+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[authentication bypass]]'
- '[[broken authentication]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Simple 2FA Bypass

## Summary

2FA authentication is considered to be an extra layer of security for authentication mechanism. An attacker can simply bypass 2FA if there are no proper checks in place 

## Description

# Description

2FA authentication is considered to be an extra layer of security for authentication mechanism. An attacker can simply bypass 2FA if there are no proper checks in place

# Instructions

# 

1.Create a valid account with credentials on the application and login .

2.  After logging into the account with username and password, a 4 digit security code will be required to authenticate as part of 2FA .

3.Access the email to check for security code that was sent through registered email.

4. As it can be observed,  login is successful .

5. After successful login , click on * my account *and observe the url in the browser .

url:

[*https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id](https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id=)=wiener*

6.As an attacker with access to victim's username and password(which were acquired through other attack techniques), login into the application. A 4-digit security is required to access the account . Change the url as observed in step 5 to get access to victim's account bypassing 2FA authentication.

Modified URL:

[*https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id](https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id=)=carlos*

## Platforms

- Web

## Tags

- [[authentication bypass]]
- [[broken authentication]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
