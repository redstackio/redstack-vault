---
id: faf90a1e-6ac1-4342-8ffe-41212064c633
name: Archive via Custom Method
type: sub-technique
mitre_id: T1560.003
mitre_url: null
created_at: '2023-04-06T00:31:25.586258+00:00'
updated_at: '2023-04-06T00:31:25.586258+00:00'
parent_technique: '[[Archive Collected Data|T1560 - Archive Collected Data]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Archive via Custom Method

**MITRE ID**: T1560.003

**Parent Technique**: [[Archive Collected Data|T1560 - Archive Collected Data]]

This is a sub-technique of T1560 - Archive Collected Data.

## Summary

An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method. Adversaries may choose to use custom archival methods, such as encryption with XOR or stream ciphers implemented with no external library or utility references. Custom implementations of well-kno

## Description

An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method. Adversaries may choose to use custom archival methods, such as encryption with XOR or stream ciphers implemented with no external library or utility references. Custom implementations of well-known compression algorithms have also been used.(Citation: ESET Sednit Part 2)

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
