---
id: 303072f8-9f50-4254-9db9-36e1a6321f4b
name: XSS Through File Upload
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T14:18:38.490107+00:00'
updated_at: '2023-05-26T18:17:23.654841+00:00'
platforms:
- Web
tags:
- '[[File Uploads]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# XSS Through File Upload

**Status**: ✓ Verified

## Summary

XSS can be performed on file upload functionality by renaming the file with XSS payload. The application response that contains the file name executes the payload. 

## Description

# Description

XSS can be performed on file upload functionality by renaming the file with XSS payload. The application response that contains the file name executes the payload.

# Instructions

1. Identify the file upload functionality

2. Rename the file with XSS payload

3. Select the file and click on submit

4. The payload is executed as the response contains the file name

## Platforms

- Web

## Tags

- [[File Uploads]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]
