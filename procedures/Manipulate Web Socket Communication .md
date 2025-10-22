---
id: 04f4b3a1-5428-4b70-8c06-998a2d1ce361
name: 'Manipulate Web Socket Communication '
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T14:26:01.202086+00:00'
updated_at: '2023-05-26T01:10:27.514218+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web sockets]]'
---

# Manipulate Web Socket Communication 

**Status**: ✓ Verified

## Summary

An attacker will manipulate the web sockets messages by modifying and replaying the mesages with malicious payload . 

## Description

# Description

An attacker will manipulate the web sockets messages by modifying and replaying the mesages with malicious payload .

# Instructions

1. Obserev the live chat in the application.

2. With burp intercept on , intercept the request from step 1 and send it to the repeater.

3. Edit the web socket message from step 2 with a basic xss payload *`<img src=1 onerror='alert(1)'*> and send the message to the server. Observe that the message has been blocked and and the web socket connection is closed.`

4. Add the x-forwarded-for: 1.1.1.1 and click connect to re-establish web socket connection to the server

5. obfuscate XSS payload like: *`<iframe src='jAvAsCripT:alert`1`'></iframe>* and send the request to the repeater.Observe that the message has been parsed by the application`

## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web sockets]]
