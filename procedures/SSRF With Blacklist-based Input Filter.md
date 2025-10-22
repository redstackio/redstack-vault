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

2.Change the URL in the `stockApi` parameter to `http://127.0.0.1/` and observe that the request is blocked.

3.Bypass the block by changing the URL to: [http://127.1/](http://127.0.0.1/)` , `Change the URL to `http://127.1/admin` and observe that the URL is blocked again , Obfuscate the "a" by double-URL encoding it to %2561 to access the admin interface and delete the target user.

## Platforms

- Web

## Tags

- [[SSRF]]
- [[Web Applications]]
