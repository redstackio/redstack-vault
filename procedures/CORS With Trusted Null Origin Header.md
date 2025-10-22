---
id: c40f557c-18a7-4584-b647-6220c86618c2
name: CORS With Trusted Null Origin Header
type: procedure
verified: true
submitted: true
created_at: '2020-08-13T07:03:21.981107+00:00'
updated_at: '2023-05-26T01:35:40.788128+00:00'
platforms:
- Web
tags:
- '[[CORS]]'
- '[[Web Applications]]'
---

# CORS With Trusted Null Origin Header

**Status**: ✓ Verified

## Summary

Origin Header supports the Null specification. An attcker can exploit the misconfiguration of origin header to deliver the malicious payload to victim and steal the sensitive information. 

## Description

# Description

Origin Header supports the Null specification. An attcker can exploit the misconfiguration of origin header to deliver the malicious payload to victim and steal the sensitive information.

# Instructions

1.Login to the application with the credentials provided

2. Access myaccount deatails and intercept the request using burp Suite.

3. Add ther origin header to the request from step 2 and assign null value to origin header. Null origin header can be seen reflected in the response .

## Platforms

- Web

## Tags

- [[CORS]]
- [[Web Applications]]
