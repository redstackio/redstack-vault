---
id: 69960aa4-8578-4ce7-9945-de02db4de51b
name: Rate Limiting Bypass
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T16:20:51.836608+00:00'
updated_at: '2023-05-26T01:36:50.691914+00:00'
platforms:
- Web
tags:
- '[[Rate Limiting]]'
- '[[Web Applications]]'
---

# Rate Limiting Bypass

**Status**: ✓ Verified

## Summary

An attacker can bypass the rate limiting by adding the x-forwarded-for header . 

## Description

# Description

An attacker can bypass the rate limiting by adding the* x-forwarded-for* header .

# Instructions

1. Intercept the following request using burp suite and send the request to the repeater . From the repeater tab keep sending the request to the server multiple times and obeserve the response being changed to *403 forbidden. I*P address is blocked due to sending the same request multiple times.

2. Try ***X-Forwarded-For** to Spoof Originating IP but observe the response as 403 .*

3.Try with X-Forwarded-For: IP Header 2x times Instead of One time. Observe that the response is 200 which indicate bypassing Rate limit Protection.

## Platforms

- Web

## Tags

- [[Rate Limiting]]
- [[Web Applications]]
