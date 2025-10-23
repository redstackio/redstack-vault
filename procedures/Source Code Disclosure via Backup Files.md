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





![489bb71b-c52a-422b-8bd3-f5fd6bb343d3.png]()



2. Access robots.txt file in the application. It reveals hidden or sensitive directories.





![4d509317-6bf9-436e-86ec-bfc0a26cbe8c.png]()



3. Access the */backup* directory found in the robots.txt file.





![334a9ace-9ba0-4f2a-aff5-e91190b91493.png]()



4. Access the source code backup file found in the */backup* directory.





![7f49eccc-803a-4bfb-b0b9-7732b6a590c3.png]()



5. The backup file contains source code along with hardcoded *postgres *secret as shown in the above screenshot.

## Platforms

- Web

## Tags

- [[information disclosure]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


