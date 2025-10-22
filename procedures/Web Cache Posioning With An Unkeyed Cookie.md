---
id: c99e1236-70d9-4bd0-803a-263229892a14
name: Web Cache Posioning With An Unkeyed Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T16:31:54.694782+00:00'
updated_at: '2023-05-26T01:06:31.261570+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# Web Cache Posioning With An Unkeyed Cookie

**Status**: ✓ Verified

## Summary

An attacker will manipulate the cookie parameter to poison the web cache . 

## Description

# Description

An attacker will manipulate the cookie parameter to poison the web cache .

# Instructions

1. Navigate to application home page while the burp intercept is off . Under burp proxy tab , go to http history tab and observe the http requests and responses.

Observe that the first response contains cookie parameter *fehost=prod-cache-01.*

2. Send the request to the repeater tab and replay the request until* x-cache: hit* is observed in the response headers is observed.

3. Modify the cookie parameter *fehost *with similar xss payload as below.

*payload:hellohacker"-alert(1)-"hellohacker*

4. Send the request to the server until *x-cache:hit* and the payload is observed in the response.

5. Right click on the response and copy the url to open it in the web browser.

6. Remove the cache buster from the repeater tab and send the request to the server until the victim visits the posined cache .

## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]
