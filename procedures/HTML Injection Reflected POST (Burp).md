---
id: 9ec46650-c34d-40a2-878f-304754bf8a94
name: HTML Injection Reflected POST (Burp)
type: procedure
verified: true
submitted: true
created_at: '2020-07-26T17:10:02.088152+00:00'
updated_at: '2023-05-26T01:29:44.851910+00:00'
platforms:
- Web
tags:
- '[[HTML Injection]]'
- '[[injection]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# HTML Injection Reflected POST (Burp)

**Status**: ✓ Verified

## Summary

A malicious user can use any of the unvalidated user input fields in a post request through HTML tags. The malicious HTML tags get parsed by the application and will be reflected in the response page . 

## Description

# Description

A malicious user can use any of the unvalidated user input fields in a post request through HTML tags. The malicious HTML tags get parsed by the application and will be reflected in the response page .

# Instructions

1.Enter any text in the *First name *and *Last name* fields as shown/

2.Intercept the request using burp . Observe the Post request in the image below.

3. Replace the *First name* and *Last nam*e field with HTML tags and forward the request . In this case, *<h1>, <a>* tag  and  *<h2>* tags are used .

4.Observe the* Follow me* and* redstack.io* in the response page .

5. Clicking  on *Follow me* will take you to the referenced website as mentioned in step 3.

## Platforms

- Web

## Tags

- [[HTML Injection]]
- [[injection]]
- [[owasp top 10]]
- [[Web Applications]]
