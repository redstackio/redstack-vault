---
id: f6e00897-167f-491b-b25b-d4a60d76d664
name: 'UserID Controlled By Request Parameter With Data Leakage In Redirect '
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T09:30:24.864782+00:00'
updated_at: '2023-05-26T18:50:52.607662+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled By Request Parameter With Data Leakage In Redirect 

**Status**: ✓ Verified

## Summary

Applications sometimes leak sensitive information through redirect response . In this case application is leaking apikey while redirecting the response. 

## Description

# Description

Applications sometimes leak sensitive information through redirect response . In this case application is leaking apikey while redirecting the response.

# Instructions

1. Login to the account with the given details(Weiner)  and access my account details . Intercept the reqeust using burp proxy tab.

2.Send the request to the repeater tab.

3. Change the ID parameter to *carlos and  *observe that the response redirects to the home page since the paramater value is not being accepted by the server

4.While redirecting the request to the homepage , the response leaks sensitive data, in this case its an apikey. 

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]
