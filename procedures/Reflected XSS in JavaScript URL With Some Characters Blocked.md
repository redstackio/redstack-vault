---
id: 0a59e028-bb6a-44a5-8ac4-0dd8d6b24a72
name: Reflected XSS in JavaScript URL With Some Characters Blocked
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T16:07:50.179064+00:00'
updated_at: '2023-05-26T18:22:59.250655+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS in JavaScript URL With Some Characters Blocked

**Status**: ✓ Verified

## Summary

Few application servers blocks the execution of JS code by blocking some special characters.An attacker can bypass these application level or WAF protections through different means. One way is to randomly experiment with the ways of calling JS functions. 

## Description

# Description

Few application servers blocks the execution of JS code by blocking some special characters.An attacker can bypass these application level or WAF protections through different means. One way is to randomly experiment with the ways of calling JS functions.

# Instructions

1.Observe the url with postID=1 whose value can be controlled by an user.

2. Add a single quote at the end of the postID value. Observe that the response throws an error with* Invalid blog postID.*

3.To bypass the filtering of charecters by the application server add an & before the single quote.

4.Use the belwo payload to alert a popup in the rsponse page of the application.

*payload : &'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'*

5. Observe that the response page contains a popup loaded from the payload .

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]
