---
id: 6b631471-15c0-4a21-9419-67832309e8db
name: SSRF With Whitelist-based Input Filter
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T16:04:00.841131+00:00'
updated_at: '2023-05-26T01:12:59.756498+00:00'
platforms:
- Web
tags:
- '[[SSRF]]'
- '[[Web Applications]]'
---

# SSRF With Whitelist-based Input Filter

**Status**: ✓ Verified

## Summary

Description Instruction 1. Navigate to any of the product and click on check stock to check the stock of the product .Intercept the request using burp suite and send the request to the repeater . 

## Description

Description

Instruction

1. Navigate to any of the product and click on *check stock* to check the stock of the product .Intercept the request using burp suite and send the request to the repeater .

2.  Change the URL to *`http://username@stock.weliketoshop.net*/` and observe that this is accepted, indicating that the URL parser supports embedded credentials.

3.Append a `#` to the username and observe that the URL is now rejected.

4. Double-URL encode the `#` to `%2523` and observe the extremely suspicious "Internal Server Error" response, indicating that the server may have attempted to connect to "username".

5. Change the URL to `http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos` to access the admin interface and delete the target user.

## Platforms

- Web

## Tags

- [[SSRF]]
- [[Web Applications]]
