---
id: 06c60f55-5d85-4fcd-8953-84a5858de96d
name: Privilege Escalation
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T18:14:21.196503+00:00'
updated_at: '2023-05-26T15:55:31.610026+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Privilege Escalation]]'
- '[[privileges]]'
- '[[Web Applications]]'
---

# Privilege Escalation

**Status**: ✓ Verified

## Summary

One method of performing privilege escalation is to directly access the URL of the function that belongs to other users. Escalation would be successful if the application loads the other user's functionality. 

## Description

# Description

One method of performing privilege escalation is to directly access the URL of the function that belongs to other users. Escalation would be successful if the application loads the other user's functionality.

# Instructions

1. Login into the application

2. Access the URL that belongs to other user. In the below example, *Users List* functionality that belongs to an admin user is loaded by accessing the URL by normal user. It can be observed that the session identifier remains the same.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Privilege Escalation]]
- [[privileges]]
- [[Web Applications]]
