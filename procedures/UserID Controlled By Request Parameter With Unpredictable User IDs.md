---
id: fa552cbf-10c2-49eb-b78f-85ec91fe49dc
name: UserID Controlled By Request Parameter With Unpredictable User IDs
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T08:26:35.801312+00:00'
updated_at: '2023-05-26T01:35:56.145773+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled By Request Parameter With Unpredictable User IDs

**Status**: ✓ Verified

## Summary

Applications use unpredictable parameter values to tampering of the parameters. An attacker might replace the parameter id's with that of other users whch are disclosed somewhere in the application and gain unauthorised access. 

## Description

# Description

Applications use unpredictable parameter values to tampering of the parameters. An attacker might replace the parameter id's with that of other users whch are disclosed somewhere in the application and gain unauthorised access.

# Instructions

1. Navigate to the blog post by Carlos.

2. Click on *Carlos *and Observe the url and identify *ID *parameter.

3.Login with the user *weiner *credentials and access *My Account* . 

4. Intercept the request using burp proxy . Observe the ID parameter value.

5. Change the id parameter value to the one from step 2 and submit the request to the server.

6. Navigate to the browser window and observe that you are logged in without providing credentials.

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]
