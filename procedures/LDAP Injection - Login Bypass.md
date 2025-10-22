---
id: 5f893737-d433-4d82-b138-a12a0e0f89eb
name: LDAP Injection - Login Bypass
type: procedure
verified: true
submitted: true
created_at: '2020-08-15T10:57:40.326777+00:00'
updated_at: '2023-05-26T01:26:13.355993+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[LDAP Injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# LDAP Injection - Login Bypass

**Status**: ✓ Verified

## Summary

Login mechanism in an application can be bypassed using LDAP injection. This can be achieved by using LDAP queries as payloads. 

## Description

# Description

Login mechanism in an application can be bypassed using LDAP injection. This can be achieved by using LDAP queries as payloads.

# Instructions

1. Access the login page and use the below payload in the user field. Where *slisberger* is the username.

*slisberger)(&))*

2. After clicking on Log In button, the application logins with the user *slisberger.*

## Platforms

- Web

## Tags

- [[injection]]
- [[LDAP Injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
