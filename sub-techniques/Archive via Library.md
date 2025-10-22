---
id: 8e0baaaf-b974-4938-9443-5499b55a20ea
name: Archive via Library
type: sub-technique
mitre_id: T1560.002
mitre_url: null
created_at: '2023-04-06T00:31:25.997544+00:00'
updated_at: '2023-04-06T00:31:25.997544+00:00'
parent_technique: '[[Archive Collected Data|T1560 - Archive Collected Data]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Archive via Library

**MITRE ID**: T1560.002

**Parent Technique**: [[Archive Collected Data|T1560 - Archive Collected Data]]

This is a sub-technique of T1560 - Archive Collected Data.

## Summary

An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party libraries. Many libraries exist that can archive data, including [Python](https://attack.mitre.org/techniques/T1059/006) rarfile (Citation: PyPI RAR), libzip (Citation: libzip), and zlib (Citation: Zlib

## Description

An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party libraries. Many libraries exist that can archive data, including [Python](https://attack.mitre.org/techniques/T1059/006) rarfile (Citation: PyPI RAR), libzip (Citation: libzip), and zlib (Citation: Zlib Github). Most libraries include functionality to encrypt and/or compress data.

Some archival libraries are preinstalled on systems, such as bzip2 on macOS and Linux, and zip on Windows. Note that the libraries are different from the utilities. The libraries can be linked against when compiling, while the utilities require spawning a subshell, or a similar execution mechanism.

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
