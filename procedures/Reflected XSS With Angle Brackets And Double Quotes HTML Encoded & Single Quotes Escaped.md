---
id: 50160d32-16f6-4c36-980e-9c84344e0d7c
name: Reflected XSS With Angle Brackets And Double Quotes HTML Encoded & Single Quotes
  Escaped
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T17:40:53.986734+00:00'
updated_at: '2023-05-26T15:54:46.452082+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With Angle Brackets And Double Quotes HTML Encoded & Single Quotes Escaped

**Status**: ✓ Verified

## Summary

Descritpion Application functionality or application's WAF will try to prevent user input from breaking out of JS string by encoding single quote. An attacker can bypass this by using backslah instead of single quote to craft a JavaScript load. Instructions 1. Submit a random alpha numeric string i

## Description

# Descritpion

Application functionality or application's WAF will try to prevent user input from breaking out of JS string by encoding single quote. An attacker can bypass this by using backslah instead of single quote to craft a JavaScript load.

# Instructions

1. Submit a random alpha numeric string in the searh box

2.Observe that the random string has been reflected inside a JavaScript string

3. Insert the* test'payload *in the search box . Use chrome developer tools to identify the payload in the JS response . 

4.Observe that single quote gets backslash-escaped, preventing from breaking out of the string

5. Replace the payload from above step to *`\'-alert(1)/*/ and click on *search`*.

6. A alert popup can be seen in the response of the page.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]
