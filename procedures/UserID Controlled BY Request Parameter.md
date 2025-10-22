---
id: 0af1c9e6-8967-4840-abcd-5fb23eb6041b
name: UserID Controlled BY Request Parameter
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T04:28:09.969872+00:00'
updated_at: '2023-05-26T05:22:31.107584+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled BY Request Parameter

**Status**: ✓ Verified

## Summary

Description Instructions 1.Log in to the account with credentials provided and acces account details 

## Description

Description

Instructions

1.Log in to the account with credentials provided and acces* account details*

2. Observe that the url contains username in the *id *parameter.

3.Myaccount will have* APIkey of the user .*

4. Relaod the page and capture the reuqest using burp intercept.

5. Modify the *id *parameter value to *carlos *to access the account

6.Observe that the apikey in the* my accoun*t details which belongs to carlos account

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]
