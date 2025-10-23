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





![c859b4e4-1e0d-4bd2-b173-f7b4fd8be8d5.png]()





2.Send the below request to repeater tab





![7b49bb22-91fa-43a1-a14e-02135f7abb5c.png]()





3. Send the request to server and observe the response





![4062c35e-4bf4-48e3-a548-9a296e1f8959.png]()





4. Modify the* filename* parameter to absolute path of the file you want to access 

 `/etc/passwd` file



Observe that the response contains contents of passwd file.



![11c917f7-5bd7-4773-a97e-72fd906ec1e0.png]()



## Platforms

- Web

## Tags

- [[Path Traversal]]
- [[Web Applications]]


