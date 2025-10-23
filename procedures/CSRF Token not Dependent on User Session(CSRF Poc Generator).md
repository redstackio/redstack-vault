---
id: 074f5074-1652-4fcd-8e25-0f067fe187dc
name: CSRF Token not Dependent on User Session(CSRF Poc Generator)
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T08:56:23.032875+00:00'
updated_at: '2023-05-26T18:38:12.304331+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[Session Management]]'
- '[[Web Applications]]'
---

# CSRF Token not Dependent on User Session(CSRF Poc Generator)

**Status**: ✓ Verified

## Summary

Descritpion CSRF PoC generator is used to create form based on the request and a CSRF token has to be generated and changed for every form submission.CSRF tokens are used to prevent CSRF attacks, but if the token is not associated to the user's session an attacker can simply use random token from a

## Description

# Descritpion

CSRF PoC generator is used to create form based on the request and a CSRF token has to be generated and changed for every form submission.CSRF tokens are used to prevent CSRF attacks, but if the token is not associated to the user's session an attacker can simply use random token from a pool of tokens genrated by the application server to take over the user's account.

# Instructions







1. With Burp proxying the requests from the browser and intercept off, browse the application. Identify the submit *change email form*.

![2b604ebb-1df1-4ecf-891f-65312263d771.png](_assets/images/Mash/2b604ebb-1df1-4ecf-891f-65312263d771.png)







2.Navigate to change email form and enter the new email and intercept the request using burp.





![d2b364a2-f7e0-4801-ac5f-899cc61bc2b4.png](_assets/images/Mash/d2b364a2-f7e0-4801-ac5f-899cc61bc2b4.png)





3. Copy the CSRF token to the notepad.







![3bba8435-cc4b-4873-b2bd-8c0f55e266b4.png](_assets/images/Mash/3bba8435-cc4b-4873-b2bd-8c0f55e266b4.png)





4.Open incognito window in the chrome browser , login to the application and send the change email request to the burp repeater tab.





![c3ab37c6-4609-4a6a-ac13-0258377e0d13.png](_assets/images/Mash/c3ab37c6-4609-4a6a-ac13-0258377e0d13.png)





5.Change the CSRF token value in step4 to the value copied in step 3. Send the request to the server and observe that request is accepted.





![0d819ba7-0a6e-43d7-97f2-df7417931425.png](_assets/images/Mash/0d819ba7-0a6e-43d7-97f2-df7417931425.png)





6.Use CSRF PoC generator to create a form with the request change email. CSRF tokens are single use, need to geenrate a new csrf token for every form submitted.

 With the form created , an attacker can change victim's email ID.





![6dff0edd-dd5e-4796-8f70-e9ed9acef7c2.png](_assets/images/Mash/6dff0edd-dd5e-4796-8f70-e9ed9acef7c2.png)











## Platforms

- Web

## Tags

- [[CSRF]]
- [[Session Management]]
- [[Web Applications]]


