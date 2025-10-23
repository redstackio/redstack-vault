---
id: e7a14678-b2cd-491d-82a9-80acea43ae3c
name: Privilege Escalation Using Deserialisation
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T17:52:47.569921+00:00'
updated_at: '2023-05-26T18:37:47.238971+00:00'
platforms:
- Web
tags:
- '[[Insecure Deserialisation]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Privilege Escalation Using Deserialisation

**Status**: ✓ Verified

## Summary

Application that depends on the cookie value to set the user's privilege can be tested for deserialisation attacks. 

## Description

# Description

Application that depends on the cookie value to set the user's privilege can be tested for deserialisation attacks.



# Instructions

1. A cookie *_user* is set in the browser by the application. It is base64 encoded serialised value.





![7a28bb7c-2e86-4430-b9ea-a0ad730eb268.png](_assets/images/Mash/7a28bb7c-2e86-4430-b9ea-a0ad730eb268.png)



2. The value is decoded in Burp decoder to obtain serialised value. It is observed that "s" value is set to '0' as the logged in user is a non-admin.







![a4747f44-91da-42fb-8770-8028bc818575.png](_assets/images/Mash/a4747f44-91da-42fb-8770-8028bc818575.png)





3.  The "s" value is set to '1' which is the value for an admin user. It is then encoded to base64 using Burp encoder.



![112b1bf3-8986-4da8-8333-2b96863b7ed4.png](_assets/images/Mash/112b1bf3-8986-4da8-8333-2b96863b7ed4.png)





4. Copy the encoded value and save in the *_user* cookie. Refresh the browser and observe that the user is modified as an admin user.









![58790a25-c360-4424-afd8-183c21563e2b.png]()











## Platforms

- Web

## Tags

- [[Insecure Deserialisation]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


