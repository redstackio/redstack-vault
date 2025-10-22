---
id: 24b6117a-912c-4e52-949d-c98231777b26
name: Insecure Direct Object References (IDOR)
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T14:51:37.891148+00:00'
updated_at: '2023-05-26T01:15:56.807089+00:00'
platforms:
- Web
tags:
- '[[IDOR]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Insecure Direct Object References (IDOR)

**Status**: ✓ Verified

## Summary

Leveraging the direct access provided to objects based on user-input, any user of the application can modify the referenced object or ID to obtain details of other users. 

## Description

# Description

Leveraging the direct access provided to objects based on user-input, any user of the application can modify the referenced object or ID to obtain details of other users.

# Instructions 

# 

1. In the below screenshot, orders are listed based on the *user* parameter in the URL.

2. If the *user* parameter is modified and replaced with the Email  ID of other user, the application loads the details of the modified user.

## Platforms

- Web

## Tags

- [[IDOR]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
