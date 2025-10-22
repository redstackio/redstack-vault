---
id: 1f299e01-171d-4be7-9ce0-37e06aa57a6a
name: SSRF With Filter Bypass Via Open Redirection
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T16:11:51.392583+00:00'
updated_at: '2023-05-26T01:05:37.268037+00:00'
platforms:
- Web
tags:
- '[[Open Redirection]]'
- '[[SSRF]]'
- '[[Web Applications]]'
---

# SSRF With Filter Bypass Via Open Redirection

**Status**: ✓ Verified

## Summary

Description Instructions 1.Navigate to product page and click on check stock . Intercept the request and send it to the repeater tab. 

## Description

Description

Instructions

1.Navigate to product page and click on *check stock* . Intercept the request and send it to the repeater tab.

2.Create a URL to exploit open redirection vulnerability and redirects to the admin interface.Modify the *`stockAp*i` parameter to 

 `/product/nextProduct?path=http://192.168.0.12:8080/admin`

3.The stock checker should follow the redirection and show the admin page. An attacker can then amend the path to delete the target user: `/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos`

## Platforms

- Web

## Tags

- [[Open Redirection]]
- [[SSRF]]
- [[Web Applications]]
