---
id: 637479f2-91d0-45fd-b4fa-82f1c4cf9cac
name: SSRF With Blacklist-based Input Filter
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T15:50:50.887116+00:00'
updated_at: '2023-05-26T01:33:43.366214+00:00'
platforms:
- Web
tags:
- '[[SSRF]]'
- '[[Web Applications]]'
---

# SSRF With Blacklist-based Input Filter

**Status**: ✓ Verified

## Summary

Application servers block request with inputs containing hostnames like 127.0.0.1 and localhost . An attacker can bypass this kind of black listed input filter by using techniques like encoding. 

## Description

# Description

Application servers block request with inputs containing hostnames like 127.0.0.1 and localhost . An attacker can bypass this kind of black listed input filter by using techniques like encoding.

# Instructions

# 



1. Naviagte to product  and click on "check stock" . Intercept the request and send it to repeater tab.





![742f1de8-45a7-4d94-85d3-1e25f9e7152e.png]()







2.Change the URL in the `stockApi` parameter to `http://127.0.0.1/` and observe that the request is blocked.





![59473176-6433-41e3-a065-0e33a28809e8.png]()







3.Bypass the block by changing the URL to: [http://127.1/](http://127.0.0.1/)` , `Change the URL to `http://127.1/admin` and observe that the URL is blocked again , Obfuscate the "a" by double-URL encoding it to %2561 to access the admin interface and delete the target user.





![988b12e7-f041-4fac-8a4c-d2fa5c05e4a5.png]()





## Platforms

- Web

## Tags

- [[SSRF]]
- [[Web Applications]]


