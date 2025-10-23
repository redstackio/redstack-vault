---
id: 9d6b06d7-45ad-4b26-b8ed-748afc366205
name: Login Form Using GET Method - Credentials Exposure
type: procedure
verified: true
submitted: true
created_at: '2020-07-22T18:04:12.377007+00:00'
updated_at: '2023-05-26T01:05:23.567944+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Sensitive Data Exposure]]'
- '[[Web Applications]]'
---

# Login Form Using GET Method - Credentials Exposure

**Status**: ✓ Verified

## Summary

Using GET method in login form will expose credentials in plain-text through web history and web server access logs. 

## Description

# Description

Using GET method in login form will expose credentials in plain-text through web history and web server access logs.



# Instructions

1. Intercept the login form request in BurpSuite







![5958fd5c-772c-40b8-9073-ef2da3b92537.jpg](_assets/images/Mash/5958fd5c-772c-40b8-9073-ef2da3b92537.jpg)













2. Login form is using GET method to transfer username and password from the browser









![70de77b7-a938-4798-8d62-099a2b3a91be.jpg](_assets/images/Mash/70de77b7-a938-4798-8d62-099a2b3a91be.jpg)









3. Browser history revealing username and password in plain-text







![1f51e34c-db38-48f0-950f-54bbd352ddba.jpg](_assets/images/Mash/1f51e34c-db38-48f0-950f-54bbd352ddba.jpg)









4. Web server access logs containing username and password in plain-text 









![b5812286-7a3f-48f7-bf04-578b03011f78.jpg](_assets/images/Mash/b5812286-7a3f-48f7-bf04-578b03011f78.jpg)







## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Sensitive Data Exposure]]
- [[Web Applications]]


