---
id: 48b1c906-8d4b-4d5b-b770-d023fa78d142
name: Find Interesting Strings in a Raw Memory Dump
type: procedure
verified: true
submitted: true
created_at: '2020-03-31T05:01:26.346855+00:00'
updated_at: '2023-05-25T19:46:57.396431+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
platforms:
- BSD
- Linux
- Mac OSx
- Windows
tags:
- '[[memory]]'
commands:
- '[[Search Raw Data for Human Readable Strings]]'
---

# Find Interesting Strings in a Raw Memory Dump

**Status**: ✓ Verified

## Summary

Basic enumeration of human readable strings can quickly provide information from a raw memory dump. Depending on the source, a dump may include usernames and passwords, encryption keys, cookies, library calls, etc, all of which can be easily identified without the need for more sophisticated analys

## Description

# Description

Basic enumeration of human readable strings can quickly provide information from a raw memory dump. Depending on the source, a dump may include usernames and passwords, encryption keys, cookies, library calls, etc, all of which can be easily identified without the need for more sophisticated analysis.

# Instructions

**Tips**: Search for strings which are contextually relevant to the memory dump. If searching for:

- Cookies - Use strings in HTTP request headers, eg: "Cookie: "

- Passwords - Use strings like known usernames, or the string "password". Sometimes these strings will appear together if the dump includes authentication information

- File Signatures - Use strings that may appear in sensitive data, like "│-----BEGIN OPENSSH PRIVATE KEY-----"

- Function Calls - Use strings that match common library calls to find points for further analysis, or for a high level view of a process

- Nearby Lines - Use the "-B $_VALUE" argument for grep to includes lines before the match, "-A $_VALUE" to include those after, or "-C $_VALUE" to include before and after

**Command** ([[Search Raw Data for Human Readable Strings]]):

```bash
strings $_DUMP | grep $_STRING
```

## Platforms

- BSD
- Linux
- Mac OSx
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]

## Commands Used

- [[Search Raw Data for Human Readable Strings]]

## Tags

- [[memory]]
