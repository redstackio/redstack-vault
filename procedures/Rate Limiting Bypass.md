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









![f255b6dc-d8f3-43c0-b182-3bc081061d1b.png](_assets/images/Mash/f255b6dc-d8f3-43c0-b182-3bc081061d1b.png)





2. Try ***X-Forwarded-For** to Spoof Originating IP but observe the response as 403 .*





![b7a6c24a-ee95-4b33-9cb1-e9ffbad8da93.png](_assets/images/Mash/b7a6c24a-ee95-4b33-9cb1-e9ffbad8da93.png)







3.Try with X-Forwarded-For: IP Header 2x times Instead of One time. Observe that the response is 200 which indicate bypassing Rate limit Protection.







![d9c18507-2f5d-4e5a-acae-9a3fe2d26f24.png](_assets/images/Mash/d9c18507-2f5d-4e5a-acae-9a3fe2d26f24.png)



## Platforms

- Web

## Tags

- [[Rate Limiting]]
- [[Web Applications]]


