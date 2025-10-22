---
id: 76ce3cdb-42bf-46f1-b5b3-a47f2adfa941
name: XXE Access Private Portals
type: procedure
verified: true
submitted: true
created_at: '2020-08-04T19:29:48.509038+00:00'
updated_at: '2023-05-26T18:08:56.956264+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xxe]]'
---

# XXE Access Private Portals

**Status**: ✓ Verified

## Summary

An XML request can be modified by adding external entities to access internal/private portals on the network where the application is hosted. 

## Description

# Description

An XML request can be modified by adding external entities to access internal/private portals on the network where the application is hosted.

# Instructions

# 

# 

1. In the below screenshot, an XML request is sent for authentication

2. The XML request is modified and SYSTEM entity is added to request internal portal with sensitive information. The application makes request to the internal portal and loads the contents.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xxe]]
