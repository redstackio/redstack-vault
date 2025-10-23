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





![e5d996c6-31d7-4703-9467-cadf55332ad0.png]()





2. Send the request to the repeater tab and replay the request until* x-cache: hit* is observed in the response headers is observed.







![46c35030-068e-44a0-83ab-5a747f40c662.png]()



3. Modify the cookie parameter *fehost *with similar xss payload as below.



*payload:hellohacker"-alert(1)-"hellohacker*





![733e4935-9c20-4fab-9ac6-f77b10f6aa0d.png]()

4. Send the request to the server until *x-cache:hit* and the payload is observed in the response.





![d2caf1ba-0089-4225-8151-6e5442782106.png]()





5. Right click on the response and copy the url to open it in the web browser.







![f6bf0f23-da5a-4da6-8fed-1dd5d5cd1c24.png]()



6. Remove the cache buster from the repeater tab and send the request to the server until the victim visits the posined cache .





![23918873-8320-4b6d-9a73-44e238607971.png]()



## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]


