---
id: 2e89ae3d-d1bb-4ad3-8f89-e4af3b72b723
name: Cache Key Injection
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T18:59:33.447621+00:00'
updated_at: '2023-05-26T01:16:29.698815+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# Cache Key Injection

**Status**: ✓ Verified

## Summary

Keyed components are used as a string to create the cache key. An attacker will exploit this by crafting two different requests with the same cache key. Cache will be poisoned first and subsequently execute the payload in the next request. 

## Description

# Description

Keyed components are used as a string to create the cache key. An attacker will exploit this by crafting two different requests with the same cache key. Cache will be poisoned first and subsequently execute the payload in the next request.

# Instructions

1.Intercept the login request using burp proxy tab

2.Identify the request from HTTP history and send the request to repeater tab

3.Observe that the redierect at login allows you to append the arbitary content to the *lang* parameter

4.Also observe that the login has an import from* /js/localize.js.* It can be observed that this is vulnerable to client side parameter pollution through lang parameter since the value isnt url encoded.

5. Craft a url in the folloiwng way . *lang* parameter is vulnerable to client side parameter pollution and * /js/localize.js is vulenrable to response host header injection.*

`GET /js/localize.js?lang=en?utm_content=z&cors=1&x=1 HTTP/1.1`

`Origin: x%0d%0aContent-Length:%208%0d%0a%0d%0aalert(1)$$$$`

6.Craft another url with similar one as above with /login request.

*`GET /login?lang=en?utm_content=x%26cors=1%26x=1$$Origin=x%250d%250aContent-Length:%208%250d%250a%250d%250aalert(1)$$%23 HTTP/1.*1`

7. After sending the above two requests to the server , it will poison the /login?lang=en request which redirects to the login page with poisoned js file  which triggers the alert(1)

## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]
