---
id: be88df2a-7edf-4d1e-be87-cdc5dcb030f9
name: 'Identifying Blind XXE Using Out of Band '
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T14:47:39.103836+00:00'
updated_at: '2023-05-26T01:17:20.455560+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xxe]]'
commands:
- '[[Netcat windows in listening mode on port 80]]'
---

# Identifying Blind XXE Using Out of Band 

**Status**: ✓ Verified

## Summary

In case of out of band XXE attack, there will be no immediate response from the application. An attacker will send a crafted XXE payload  in such a way that the response will be sent to attacker controlled machine/ip/server. 

## Description

# Description

In case of out of band XXE attack, there will be no immediate response from the application. An attacker will send a crafted XXE *payload*  in such a way that the response will be sent to attacker controlled machine/ip/server.

# 

# Instructions

# 

1. Intercept the login request in Burp and send it to repeater. The request is submitted and successful login message is observed in the response.

2. XML request is modified and an external entity is added, which makes request to the specified URL

3. A listener is setup in the remote machine to capture the request that is initiated by server.

**Command** ([[Netcat windows in listening mode on port 80]]):

```bash
nc.exe -nlvp 80
```

4. Upon submitting the request in step 2, the server initiates a connection to the listener. 

## Platforms

- Web

## Commands Used

- [[Netcat windows in listening mode on port 80]]

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xxe]]
