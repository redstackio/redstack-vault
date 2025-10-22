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

2. Add an additional extension which is accepted by the application to the malicious exe file. An additional character should also be added between these extensions.

In this case, the file is named as: *Malicious.exeA.jpg*

3. Select the file and click on submit

4. Intercept the request in Burp

5. Click on *Hex* tab to see the request in Hex format. Identify the filename on the right pane and search for the Hex value of A, which is 41

6. Replace the value (41) with Null Byte (00) and forward the request

7. The server strips the extension that is after the Null Byte and uploads the Malicious.exe file

## Platforms

- Web

## Tags

- [[injection]]
- [[Null Byte Injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
