---
id: 26b40818-e691-4cb2-80b2-117420e72a3c
name: Password Reset Broken Logic
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T16:19:37.720885+00:00'
updated_at: '2023-05-26T01:09:34.963005+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Password Reset Broken Logic

**Status**: ✓ Verified

## Summary

Most of the applications will send an email with an unique url to reset the password. During the reset process, the functional logic can be exploited to change the user's password. 

## Description

# Description

Most of the applications will send an email with an unique url to reset the password. During the reset process, the functional logic can be exploited to change the user's password.

# Instructions

1.Login to the application  with the credentials provided. Keep the burp running while it is intercepting the requests from the browser.

2.Enter the username and click on submit 

3. Access email to check for password link.

4.Click on the link to change the password

5. Enter new password and confirm password.

6.From the HTTP history , identify the request with POST forgot-password and send the request to the repeater tab.Observe the temp-forgot-password-token in the url and body as well.

7.Remove the forgot-password-token value from the url and body . Change the username to *carlos *and submit the request to the server. Observe the *302 *response. Now from the browser, enter new password and submit to change the password of *carlos*.

8. Login to the application using newly changed password.

## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]
