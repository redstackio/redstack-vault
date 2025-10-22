---
id: 1f52fba1-8ab5-418e-a668-adb4bc45d464
name: Identifying PHP Code Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T18:26:38.252802+00:00'
updated_at: '2023-05-26T18:40:05.656289+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Identifying PHP Code Injection

**Status**: ✓ Verified

## Summary

PHP code injection can be performed through user input fields or URL parameters. 

## Description

# Description

PHP code injection can be performed through user input fields or URL parameters.

# Instructions

# 

1. Identify an input field in the application.

2. Insert *<> * to observe if the application generates an error message.

3. As error message was observed in the previous step, php code can be passed through input fields.

4. Echo command along with a string is inserted through input field to observe if the message gets printed. Application response contains the inserted string.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
