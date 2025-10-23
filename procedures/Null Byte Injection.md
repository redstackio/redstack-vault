---
id: e6d5df54-85ff-4c9f-8181-d2361d41acd6
name: Null Byte Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T14:40:52.823830+00:00'
updated_at: '2023-05-26T01:30:10.499969+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[Null Byte Injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Null Byte Injection

**Status**: ✓ Verified

## Summary

Null Byte injection can be performed at file upload functionalities where certain files types are allowed to be uploaded. The restriction can be bypassed by using Null Byte injection. 

## Description

# Description

Null Byte injection can be performed at file upload functionalities where certain files types are allowed to be uploaded. The restriction can be bypassed by using Null Byte injection.

# Instructions

# 

1. Identify file upload function and click on *Browse* to select the file





![a8277c40-7833-4162-b772-2f9581a5188f.jpg](_assets/images/Mash/a8277c40-7833-4162-b772-2f9581a5188f.jpg)





2. Add an additional extension which is accepted by the application to the malicious exe file. An additional character should also be added between these extensions.

In this case, the file is named as: *Malicious.exeA.jpg*







![0b135b64-56f7-441d-b386-d066ac1f06a8.jpg](_assets/images/Mash/0b135b64-56f7-441d-b386-d066ac1f06a8.jpg)



3. Select the file and click on submit







![df5ee4f1-661e-4038-aa69-3542e71887c2.jpg](_assets/images/Mash/df5ee4f1-661e-4038-aa69-3542e71887c2.jpg)









4. Intercept the request in Burp







![cde1f1a5-5a28-40d8-960f-5849f3d14301.jpg](_assets/images/Mash/cde1f1a5-5a28-40d8-960f-5849f3d14301.jpg)













5. Click on *Hex* tab to see the request in Hex format. Identify the filename on the right pane and search for the Hex value of A, which is 41

















6. Replace the value (41) with Null Byte (00) and forward the request









![b63cba8b-bcdf-40d2-a584-51320526fd35.jpg](_assets/images/Mash/b63cba8b-bcdf-40d2-a584-51320526fd35.jpg)









7. The server strips the extension that is after the Null Byte and uploads the Malicious.exe file









![25800465-a417-48f2-8d30-4e9a10f47cf2.jpg](_assets/images/Mash/25800465-a417-48f2-8d30-4e9a10f47cf2.jpg)















## Platforms

- Web

## Tags

- [[injection]]
- [[Null Byte Injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


