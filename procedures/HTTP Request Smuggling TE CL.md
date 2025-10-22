---
id: b9c33cfa-209e-4e31-85f4-dccd89039896
name: HTTP Request Smuggling TE CL
type: procedure
verified: true
submitted: true
created_at: '2020-08-11T17:22:02.803091+00:00'
updated_at: '2023-05-26T18:09:24.981300+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
---

# HTTP Request Smuggling TE CL

**Status**: ✓ Verified

## Summary

In TE CL HTTP request smuggling , the front end server uses Transfer Encoding header and the backend uses content length header while parsing the application's response . 

## Description

# Description

In TE CL HTTP request smuggling , the front end server uses Transfer Encoding header and the backend uses content length header while parsing the application's response .

# Instructions

# 

# 

1. Intercept the request using Burp Suite

2. Send the intercepted request to repeater

3. Replace the request in step 2 to following 

**Code**: [[POST / HTTP/1.1
Host: your-lab-id.web-security-ac]]

4. Send the modified request to the server couple of times . Observe the request being parswed by the application server with an error showing *Unrecognized method GPOST*

## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]
