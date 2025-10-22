---
id: 777fda65-727e-4bd2-ac87-848ddc1972d5
name: Method Based Access Control
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T19:19:59.458475+00:00'
updated_at: '2023-05-26T18:49:48.483999+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# Method Based Access Control

**Status**: ✓ Verified

## Summary

Few applications allow alternate HTTP request methods.An attacker can modify the HTTP methods to perform actions on resticted urls 

## Description

# Description

Few applications allow alternate HTTP request methods.An attacker can modify the HTTP methods to perform actions on resticted urls

# Instructions

1. Log in to the application using admin credentials

2.Navigate to admin panel and upgrade user carlos and intercept the request

3. Observe that the account has been upgraded to admin account 

4.Open incognito window and login with non-admin credentials and intercept the request 

5. Attempt to repromote the carlos with the non admin user by copying that user's session cookie into the existing Burp Repeater request, and observe th at the response says "Unauthorized ". 

6. Change the method from `POST` to `POSTX` and observe that the response changes to "missing parameter". Convert the request to use the `GET` method by right-clicking and selecting "Change request method". 

7.Change the username parameter to weiner username and resend the request.

8.Observe that the request has been accpeted by the server.

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]
