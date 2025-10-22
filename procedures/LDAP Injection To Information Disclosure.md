---
id: 04a42434-7e7a-4e43-aeea-eef3249172e9
name: LDAP Injection To Information Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T15:03:36.120633+00:00'
updated_at: '2023-05-26T18:22:20.652618+00:00'
platforms:
- Web
tags:
- '[[LDAP Injection]]'
- '[[Web Applications]]'
---

# LDAP Injection To Information Disclosure

**Status**: ✓ Verified

## Summary

An attacker may exploit LDAP injection technique to disclose information that is otherwise disclosed to only authorised users. 

## Description

# Description

An attacker may exploit LDAP injection technique to disclose information that is otherwise disclosed to only authorised users.

# Instructions

1.Suppose a resources explorer allows users to know the resources available in the system (printers, scanners, storage systems, etc...). This is a typical OR LDAP Injection . Rsc1=printer and Rsc2=scanner to show all the available printers and scanners in the system

2.The following query is sent to the server:* (|(type=printer)(uid=*))(type=scanner))* The LDAP server responds with all the printer and user objects.

## Platforms

- Web

## Tags

- [[LDAP Injection]]
- [[Web Applications]]
