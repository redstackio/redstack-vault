---
id: cc26c9d0-cbf1-4c75-b5f0-f6cdf7a820dc
name: No Rate Limiting On The Application
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T16:05:02.699695+00:00'
updated_at: '2023-05-26T01:24:42.204031+00:00'
platforms:
- Web
tags:
- '[[Rate Limiting]]'
- '[[Web Applications]]'
---

# No Rate Limiting On The Application

**Status**: ✓ Verified

## Summary

Description Instructions 1. Go to the email verification feature of the application. 

## Description

Description

Instructions

1. Go to the email verification feature of the application.

2. click on* send confirmation link* with the burp intercept on and capture the request.

3.send the request to intruder and repeat it multiple times and set an arbitrary value in scope

4.Set the payload options as required to start the attack and then click on *start attack. *Observe that a attack window is opened.

5. Observe the *200 *responses in the attacker's window. You will receive emails in vast amount as there is no rate limit.

## Platforms

- Web

## Tags

- [[Rate Limiting]]
- [[Web Applications]]
