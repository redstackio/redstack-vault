---
id: 7132288a-ffc2-4049-b8b5-b844f19ef0cf
name: Reflected XSS Using HTTP Request Smuggling
type: procedure
verified: true
submitted: true
created_at: '2020-08-16T18:48:44.398483+00:00'
updated_at: '2023-05-26T01:25:20.287823+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# Reflected XSS Using HTTP Request Smuggling

**Status**: ✓ Verified

## Summary

HTTP Request Smuggling can be used to perform Reflected XSS. This can be done by adding an XSS payload in the smuggled request in User-Agent header. 

## Description

# Description



HTTP Request Smuggling can be used to perform Reflected XSS. This can be done by adding an XSS payload in the smuggled request in User-Agent header.



# Procedure



1. Intercept the request and find the User-Agent header. Check the view-source of the page and observe the User-Agent being part of a form.





![1fc79e32-ad66-4e31-8580-1d351ee193bc.jpg]()



2. Add an additional HTTP GET request as shown in the below screenshot. Modify the User-Agent header and replace with XSS payload.





![06e24616-b095-4d81-8456-f2d65ab35310.jpg]()



3. Observe the response with an alert box as the script is reflected in the response and gets executed.





![399f2fe2-8b79-4a35-9ae0-af816f9e301f.jpg]()







## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]


