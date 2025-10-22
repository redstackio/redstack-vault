---
id: 323f458f-ea3b-4a63-9a1d-df517ad24319
name: Path Traversal With Absolute Path
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T15:39:14.770226+00:00'
updated_at: '2023-05-26T01:37:47.891462+00:00'
platforms:
- Web
tags:
- '[[Path Traversal]]'
- '[[Web Applications]]'
---

# Path Traversal With Absolute Path

**Status**: ✓ Verified

## Summary

Sometimes applications allow to access internal files using absolute paths due to security misconfigurations. Traversal sequences may be blocked WAF or application's code 

## Description

# Description

Sometimes applications allow to access internal files using absolute paths due to security misconfigurations. Traversal sequences may be blocked WAF or application's code 

# Instructions

1. Click on view details and use the burp intercept to capture the request

2.Send the below request to repeater tab

3. Send the request to server and observe the response

4. Modify the* filename* parameter to absolute path of the file you want to access 

 `/etc/passwd` file

Observe that the response contains contents of passwd file.

## Platforms

- Web

## Tags

- [[Path Traversal]]
- [[Web Applications]]
