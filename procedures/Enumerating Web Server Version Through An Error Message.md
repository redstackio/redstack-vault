---
id: 4185b621-4941-430d-9264-e588a187f979
name: Enumerating Web Server Version Through An Error Message
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T15:31:13.065644+00:00'
updated_at: '2023-05-26T18:08:17.897224+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Enumerating Web Server Version Through An Error Message

**Status**: ✓ Verified

## Summary

URLs can be modified by adding special characters or browsing non-existent resources to generate error messages. The generated errors would reveal sensitive information. 

## Description

# Description

URLs can be modified by adding special characters or browsing non-existent resources to generate error messages. The generated errors would reveal sensitive information.

# Instructions

# 

1. Access the URL to load the application

2. The URL is modified by adding a special character at the end. This generates an error message which contain sensitive information.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
