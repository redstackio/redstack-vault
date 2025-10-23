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









![7d43c611-3c36-4fef-b3ce-e0bd5c806d3d.png](_assets/images/Mash/7d43c611-3c36-4fef-b3ce-e0bd5c806d3d.png)





2. Send the intercepted request to repeater









![e5a84635-e39a-4cc0-a8d2-20c11d2ea397.jpg](_assets/images/Mash/e5a84635-e39a-4cc0-a8d2-20c11d2ea397.jpg)









3. Replace the request in step 2 to following 





**Code**: [[POST / HTTP/1.1
Host: your-lab-id.web-security-ac]]







4. Send the modified request to the server couple of times . Observe the request being parswed by the application server with an error showing *Unrecognized method GPOST*





![1775ee32-6a53-4aa1-88f2-aed0f083fefc.jpg](_assets/images/Mash/1775ee32-6a53-4aa1-88f2-aed0f083fefc.jpg)









## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]


