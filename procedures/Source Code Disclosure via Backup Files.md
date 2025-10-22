---
id: 8c561f69-72de-438e-984c-5f117f62a8af
name: Source Code Disclosure via Backup Files
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T12:07:58.056555+00:00'
updated_at: '2023-05-26T01:22:59.501370+00:00'
platforms:
- Web
tags:
- '[[information disclosure]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Source Code Disclosure via Backup Files

**Status**: ✓ Verified

## Summary

Backup files of the source code would reveal sensitive information if they are not moved to secure locations. Contents of robots.txt can be leveraged to access hidden directories and files inside them. 

## Description

# Description

Backup files of the source code would reveal sensitive information if they are not moved to secure locations. Contents of robots.txt can be leveraged to access hidden directories and files inside them.

# Procedure

1. Access the application

2. Access robots.txt file in the application. It reveals hidden or sensitive directories.

3. Access the */backup* directory found in the robots.txt file.

4. Access the source code backup file found in the */backup* directory.

5. The backup file contains source code along with hardcoded *postgres *secret as shown in the above screenshot.

## Platforms

- Web

## Tags

- [[information disclosure]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
