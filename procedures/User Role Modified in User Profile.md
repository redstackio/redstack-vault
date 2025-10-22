---
id: 9a6fc951-29ca-4a8e-9fe8-20b372fd58cb
name: User Role Modified in User Profile
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T18:35:39.509371+00:00'
updated_at: '2023-05-26T01:36:23.761397+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# User Role Modified in User Profile

**Status**: ✓ Verified

## Summary

Few applications due to poor design will let an attacker to modify the user role from the attacker's legitimate profile to get unauthorised access to other user accounts sometimes admin account. 

## Description

# Description

Few applications due to poor design will let an attacker to modify the user role from the attacker's legitimate profile to get unauthorised access to other user accounts sometimes admin account.

# Instructions

1.Login with the credentials provided.

2. Click on "My Account" and submit a new email address and capture the request on Burp and send it to the Repeater and observe the response that contains your role ID.

3.`Add "roleid":2` into the JSON in the request body, and resend it.

4.Observe that the response shows your `roleid` has changed to 2 and the email is successfully changed.

5.Observe that the you have access to admin panel.

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]
