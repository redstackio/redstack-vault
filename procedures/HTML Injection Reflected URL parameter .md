---
id: 6bf9f487-b164-43c5-976a-1626ca9118ad
name: 'HTML Injection Reflected URL parameter '
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T16:47:07.781259+00:00'
updated_at: '2023-05-26T18:11:29.969512+00:00'
platforms:
- Web
tags:
- '[[HTML Injection]]'
- '[[injection]]'
- '[[Web Applications]]'
---

# HTML Injection Reflected URL parameter 

**Status**: ✓ Verified

## Summary

Reflected injection vulnerability can be exploited by an attacker by injecting malicious code by manipulating the url parameter. 

## Description

# Description

Reflected injection vulnerability can be exploited by an attacker by injecting malicious code by manipulating the url parameter.

# Instructions

1. Observe the url in the browser and in the body.

2. Intercept the request using burp 

3. Modify the host parameter in burp request with malicious url. 

4. Modified url has been reflected onto the page as shown below.

## Platforms

- Web

## Tags

- [[HTML Injection]]
- [[injection]]
- [[Web Applications]]
