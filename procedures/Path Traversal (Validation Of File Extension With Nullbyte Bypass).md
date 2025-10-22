---
id: 80b8956b-d0b8-4e8c-8cb6-add962e0a8ad
name: Path Traversal (Validation Of File Extension With Nullbyte Bypass)
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:21:04.123201+00:00'
updated_at: '2023-05-26T01:38:01.246217+00:00'
platforms:
- Web
tags:
- '[[Path Traversal]]'
- '[[Web Applications]]'
---

# Path Traversal (Validation Of File Extension With Nullbyte Bypass)

**Status**: ✓ Verified

## Summary

Some applications validate the extension of the filename in the filepaths. An attacker can simply bypass this validation check by adding the file extension name to the file that needs to be accessed. 

## Description

# Description

Some applications validate the extension of the filename in the filepaths. An attacker can simply bypass this validation check by adding the file extension name to the file that needs to be accessed.

# Instructions

1.Use the burp proxy  to intercept the request

2. Send the request to the repeater tab

3. Send the reqeust from repeater to server and observe the response.

4. Modify the filename parameter value to *`../../../etc/passwd%00.jpg* and send the request to the server . Observe hte response from the server contains passwd file contents. `

## Platforms

- Web

## Tags

- [[Path Traversal]]
- [[Web Applications]]
