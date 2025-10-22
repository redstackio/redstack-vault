---
id: 7ccbbbf5-d9e9-401b-b794-05d64fa545b0
name: UserID Controlled By Request Parameter With Password Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T09:56:01.762495+00:00'
updated_at: '2023-05-26T18:48:57.606718+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled By Request Parameter With Password Disclosure

**Status**: ✓ Verified

## Summary

Appliaction's detect the unwarranted access of resource without authentication and redirect the response to home page. While redirection , the response sometimes may leak the sensitive inforamtion due to logical flaw of the application 

## Description

# Description

Appliaction's detect the unwarranted access of resource without authentication and redirect the response to home page. While redirection , the response sometimes may leak the sensitive inforamtion due to logical flaw of the application

# Instructions

1.Login with the credentials provided and access *my account* .

2. Intercept the request using burp proxy tab.Observe that update password filed already contains the current password which is masked.

3.Change the *id *paramter value to *administrator and send the request. *

4. Observe the request is redirected  because the server didnot permit to access the resource and the response contains a password for the *administrator*.

5. Login with the password identified in the above step

6. Login was successful

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]
