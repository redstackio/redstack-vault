---
id: b9909e88-014b-4e75-aba1-bb846d162b6f
name: Privilege Escalation Using LDAP Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-16T19:14:49.521323+00:00'
updated_at: '2023-05-26T01:24:54.940284+00:00'
platforms:
- Web
tags:
- '[[LDAP Injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Privilege Escalation]]'
- '[[Web Applications]]'
---

# Privilege Escalation Using LDAP Injection

**Status**: ✓ Verified

## Summary

Injecting/Modifying LDAP parameters through user input fields or URL parameters could lead to privilege escalation if the application is depending on them to provide access to resources. 

## Description

# Description

Injecting/Modifying LDAP parameters through user input fields or URL parameters could lead to privilege escalation if the application is depending on them to provide access to resources.



# Procedure



1. In the below example the user is able to access the documents of low level security. The application creates the below LDAP query using the URL parameters to list the low security files.

*(&(directory=documents)(security_level=low)) *





![cb690f54-eac6-4354-90a7-a0782c41c325.png]()





2. URL parameters can now be modified by adding *)(level=*))* to load the High and Medium severity files that are not intended for the current user.





![13444285-1715-4169-bc0e-97be709dfc46.png]()



## Platforms

- Web

## Tags

- [[LDAP Injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Privilege Escalation]]
- [[Web Applications]]


