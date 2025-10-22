---
id: dc6d91bb-4c9a-4d4c-a2ae-646b65f6b31a
name: Identifying SQL Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T14:43:10.239045+00:00'
updated_at: '2023-05-26T01:00:57.530761+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[Web Applications]]'
---

# Identifying SQL Injection

**Status**: ✓ Verified

## Summary

An attacker will inject SQL queries through user input fields or parameters in the URL to execute them on the database and extract sensitive information. To identify SQL injection in an application, special characters like single quote (') can be injected through user input fields. 

## Description

# Description

An attacker will inject SQL queries through user input fields or parameters in the URL to execute them on the database and extract sensitive information. To identify SQL injection in an application, special characters like single quote (') can be injected through user input fields.

# Instructions

1. Insert single quote into the user input field or through the parameters in the URL

2. Observe the response from the web server with SQL warning message, which confirms the existence of SQL injection.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[Web Applications]]
