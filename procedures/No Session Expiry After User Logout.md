---
id: ed1cbb2b-ea1f-4397-b6eb-bc3e3e4ef7d4
name: No Session Expiry After User Logout
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:43:04.369480+00:00'
updated_at: '2023-05-26T18:22:45.114586+00:00'
platforms:
- Web
tags:
- '[[Session Management]]'
- '[[Web Applications]]'
---

# No Session Expiry After User Logout

**Status**: ✓ Verified

## Summary

An attacker can take over the victim's account if the victim's session doesnot gets expired even after logout. 

## Description

# Description

An attacker can take over the victim's account if the victim's session doesnot gets expired even after logout.

# Instructions

1.Login to the application.

2. Install Cookie-editor extension on your browser.

3.Go to the web page and export all the cookies with the extension

4.Now log out from the web app

5. Go to the Cookie-editor extension and delete all the cookies and paste the previously copied cookies in the import section and import the cookies.

6. Reload the page and see the session still persists.

## Platforms

- Web

## Tags

- [[Session Management]]
- [[Web Applications]]
