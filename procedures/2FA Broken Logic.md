---
id: f6b5c697-6670-4147-a0ee-5a275acf5618
name: 2FA Broken Logic
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T05:40:56.124670+00:00'
updated_at: '2023-05-26T01:29:57.813833+00:00'
platforms:
  - Web
tags:
  - '[[broken authentication]]'
  - '[[Web Applications]]'
  - intruder-attack
title: Bypassing 2FA via Broken Authentication Logic
mitre_techniques:
  - T1621
---

# 2FA Broken Logic

**Status**: ✓ Verified

## Summary

An attacker can use the application's logic to bypass the 2FA authentication and get unauthorised access to victim's account 

## Description

# Description

An attacker can use the application's logic to bypass the 2FA authentication and get unauthorised access to victim's account

# Instructions







1. Login to the application with given credentials and burp running and proxying requests .







![45205696-7e6f-4f91-b981-24f4d97243e0.png](_assets/images/Mash/45205696-7e6f-4f91-b981-24f4d97243e0.png)





2. Notice that the login has 2FA enabled and need to enter 4-digit security code.





![cb9fe420-6bbe-4067-9ee4-544a318eb55c.png](_assets/images/Mash/cb9fe420-6bbe-4067-9ee4-544a318eb55c.png)





3. Intercept the request and notice that verify parameter is used to determine the user 





![96922044-7201-4c79-ab80-df838889e1fa.png](_assets/images/Mash/96922044-7201-4c79-ab80-df838889e1fa.png)





4.Access your email and notice the 4-digit security code.





![099fbd8c-e2b8-456f-a8ea-401137aa99f3.png](_assets/images/Mash/099fbd8c-e2b8-456f-a8ea-401137aa99f3.png)





5.Enter the 4-digit code to login to the application





![be8340ee-f1a8-4aae-bf10-607da3575917.png](_assets/images/Mash/be8340ee-f1a8-4aae-bf10-607da3575917.png)





6.Identify the GET /Login2  request and send it to intruder tab.





![f8ec3cc4-9322-40fd-9d0c-505b3a39947b.png](_assets/images/Mash/f8ec3cc4-9322-40fd-9d0c-505b3a39947b.png)





7.From the *intruder* tab,Change the *verify *paramter value to *carlos *







![5120e314-9ed7-4ffd-8403-fdd82b707425.png](_assets/images/Mash/5120e314-9ed7-4ffd-8403-fdd82b707425.png)





8.From the positions tab, highlight the *mfa-code* value and click on *add *to add the value to position 





![567eba35-5921-44af-88c5-dcdc8f8a1b22.png](_assets/images/Mash/567eba35-5921-44af-88c5-dcdc8f8a1b22.png)





9.From payloads tab, enter the details as below and click on *start attack* to start the brute-forcing attack.









![298beb4b-f3f1-4241-bb1a-40b4c3821e90.png](_assets/images/Mash/298beb4b-f3f1-4241-bb1a-40b4c3821e90.png)





10.When the attack finishes , observe that only one response contains *302 response. Make a note of the mfa-code that generated 302 response.*







![a8a56f63-3d0a-40f1-a626-ffe6d1ec8b81.png](_assets/images/Mash/a8a56f63-3d0a-40f1-a626-ffe6d1ec8b81.png)





11.Notice that you are logged in to carlos account with out authentication by bypassing the application's logic.



![cf244a14-e71b-4d20-b400-e7d27746eca4.png]()





## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]


