---
id: 74c88a1d-9ced-41b1-beea-19dcd4fcb63f
name: Directory Traversal Fuzzing Using DotDotPwn Tool
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T18:36:33.294218+00:00'
updated_at: '2023-05-26T01:30:49.285818+00:00'
platforms:
- Web
tags:
- '[[Directory Traversal]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
commands:
- '[[DotDotPwn Command to Perform Directory Traversal Fuzzing]]'
---

# Directory Traversal Fuzzing Using DotDotPwn Tool

**Status**: ✓ Verified

## Summary

Directory traversal will allow writing or reading files to arbitrary locations. DotDotPwn tool can be used to test directory traversal issues in an application. The tool fuzzes at all the possible locations in the application. 

## Description

# Description



Directory traversal will allow writing or reading files to arbitrary locations. DotDotPwn tool can be used to test directory traversal issues in an application. The tool fuzzes at all the possible locations in the application.



# Procedure



1. The below DotDotPwn command can be used to perform directory traversal fuzzing. The tool tries to fuzz with all possible paths for directory traversal.







**Command** ([[DotDotPwn Command to Perform Directory Traversal Fuzzing]]):

```bash
dotdotpwn -m http -h 192.168.1.5 -M GET
```





## Platforms

- Web

## Commands Used

- [[DotDotPwn Command to Perform Directory Traversal Fuzzing]]

## Tags

- [[Directory Traversal]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


