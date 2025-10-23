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





![b675a33c-3f10-4770-a43d-eed79a95d8b5.PNG](_assets/images/Mash/b675a33c-3f10-4770-a43d-eed79a95d8b5.PNG)







2.  After logging into the account with username and password, a 4 digit security code will be required to authenticate as part of 2FA .





![2d575b66-cb55-4e61-8203-d442a5e25f67.PNG](_assets/images/Mash/2d575b66-cb55-4e61-8203-d442a5e25f67.PNG)







3.Access the email to check for security code that was sent through registered email.







![2b180a39-6057-47ce-b215-13329b420c21.PNG](_assets/images/Mash/2b180a39-6057-47ce-b215-13329b420c21.PNG)





4. As it can be observed,  login is successful .





![f5c79eb7-95ff-4504-bdb3-3ce840e76471.PNG](_assets/images/Mash/f5c79eb7-95ff-4504-bdb3-3ce840e76471.PNG)





5. After successful login , click on * my account *and observe the url in the browser .

url:

[*https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id](https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id=)=wiener*





![dbee08ed-c139-494f-b98e-2825a8d08134.PNG](_assets/images/Mash/dbee08ed-c139-494f-b98e-2825a8d08134.PNG)



6.As an attacker with access to victim's username and password(which were acquired through other attack techniques), login into the application. A 4-digit security is required to access the account . Change the url as observed in step 5 to get access to victim's account bypassing 2FA authentication.



Modified URL:



[*https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id](https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id=)=carlos*









![d5c1821c-3ae1-4ea1-94b2-5db4b5fa13b3.PNG](_assets/images/Mash/d5c1821c-3ae1-4ea1-94b2-5db4b5fa13b3.PNG)



















## Platforms

- Web

## Tags

- [[authentication bypass]]
- [[broken authentication]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


