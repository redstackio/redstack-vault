---
id: b1e10fa8-2c4f-4134-b661-c0387f79c16e
name: Path Traversal Traversal Sequences Stripped Non-recursively
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T15:54:57.463041+00:00'
updated_at: '2023-05-26T01:13:15.182245+00:00'
platforms:
- Web
tags:
- '[[Path Traversal]]'
- '[[Web Applications]]'
---

# Path Traversal Traversal Sequences Stripped Non-recursively

**Status**: ✓ Verified

## Summary

Nested traversal sequences can used to bypass the application's functionality and access the files 

## Description

# Description

Nested traversal sequences can used to bypass the application's functionality and access the files

# Instructions

1. Use the burp suite to intercept the following request.

2. Send the request to the repeater tab

3.Send the request to the server and observe the response. 

4.Modify the filename parameter to the following payload and send the modified request to server . Observe that the response contains the *passwd *file contents

*`....//....//....//etc/passwd ( observe the nested traversal sequences will revert to simple traversal sequences *)`

## Platforms

- Web

## Tags

- [[Path Traversal]]
- [[Web Applications]]
