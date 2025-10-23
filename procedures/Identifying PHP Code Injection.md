---
id: 1f52fba1-8ab5-418e-a668-adb4bc45d464
name: Identifying PHP Code Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T18:26:38.252802+00:00'
updated_at: '2023-05-26T18:40:05.656289+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Identifying PHP Code Injection

**Status**: ✓ Verified

## Summary

PHP code injection can be performed through user input fields or URL parameters. 

## Description

# Description

PHP code injection can be performed through user input fields or URL parameters.

# Instructions

# 

1. Identify an input field in the application.





![d7516b72-b6d7-4c4e-a571-98be4f008592.PNG](_assets/images/Mash/d7516b72-b6d7-4c4e-a571-98be4f008592.PNG)









2. Insert *<> * to observe if the application generates an error message.





![9d7e98b3-ae2e-4f79-9ce1-db6962d93e6b.PNG](_assets/images/Mash/9d7e98b3-ae2e-4f79-9ce1-db6962d93e6b.PNG)











3. As error message was observed in the previous step, php code can be passed through input fields.





![401c09aa-bbcf-4903-a31e-e3b8f953c710.PNG](_assets/images/Mash/401c09aa-bbcf-4903-a31e-e3b8f953c710.PNG)









4. Echo command along with a string is inserted through input field to observe if the message gets printed. Application response contains the inserted string.









![cd0433d3-5d77-462c-a69b-65cb151c9c24.PNG](_assets/images/Mash/cd0433d3-5d77-462c-a69b-65cb151c9c24.PNG)









## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


