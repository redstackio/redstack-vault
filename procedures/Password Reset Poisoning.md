---
id: f6926594-a03a-4a94-be07-50580306e5fc
name: Password Reset Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T17:26:11.571283+00:00'
updated_at: '2023-05-26T01:22:47.090957+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Password Reset Poisoning

**Status**: ✓ Verified

## Summary

Applications usually send the change password link to the customer's email.An attacker can maliciously change the password of the victim  by manipulating the password reset link . 

## Description

# Description

Applications usually send the change password link to the customer's email.An attacker can maliciously change the password of the victim  by manipulating the password reset link .

# Instructions

1.With burp running and proxying reqeusts ,Log in to the account with given credentials. Access my account page and observe the password reset functionality. Enter your username to reset the password and click on submit.

2. Observe that a reset link has been sent to email.

3. Access email and click on  the link to reset the password. Identify the forget-password request from the HTTPHistory and send the request to repeater tab.

4.Notice that the request supports the X*-Forwarded-Host *header .

5. Add the *X-Forwarded-Host *header to the request and change the username to *carlos *and send the request to server.

6.Access exploit server and identify the GET forget-password link

7.Load the link in the browser 

8.Enter new password to change the password of user *carlos*.

## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]
