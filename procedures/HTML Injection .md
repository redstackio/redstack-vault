---
id: 9029c61d-c0d3-4174-9cc1-23909f9ddbf5
name: 'HTML Injection '
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T13:59:51.707927+00:00'
updated_at: '2023-05-26T18:29:16.065509+00:00'
platforms:
- Web
tags:
- '[[HTML Injection]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# HTML Injection 

**Status**: ✓ Verified

## Summary

HTML injection can be performed through user input fields. Inject the HTML tags through input fields and observe if the application is processing the injected tags. 

## Description

# Description

HTML injection can be performed through user input fields. Inject the HTML tags through input fields and observe if the application is processing the injected tags.

# Instructions

# 

1. *Test* message is entered in the search field





![d1b3b0b9-7f2b-4982-8063-c705b5267674.png](_assets/images/Mash/d1b3b0b9-7f2b-4982-8063-c705b5267674.png)







2. Result for the search was displayed as shown below





![7240f24a-4dc4-49f0-a350-69376331be74.png](_assets/images/Mash/7240f24a-4dc4-49f0-a350-69376331be74.png)







3. Insert the HTML tag in the search field



Payload:* <h1>Test</h1>*



![5d2ca259-e243-46b3-9b43-87b65a5ea4c5.png](_assets/images/Mash/5d2ca259-e243-46b3-9b43-87b65a5ea4c5.png)





4. Difference in the response can be observed as the application has rendered the inserted HTML tag. *Test* message is loaded in *Heading 1* format.







![d9c0e57c-d938-4f97-8d64-456db5fd644b.png](_assets/images/Mash/d9c0e57c-d938-4f97-8d64-456db5fd644b.png)













## Platforms

- Web

## Tags

- [[HTML Injection]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


