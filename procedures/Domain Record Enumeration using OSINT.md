---
id: 3bd393e7-f61b-4b8c-9894-fe7e9df6c95e
name: Domain Record Enumeration using OSINT
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T17:55:36.119392+00:00'
updated_at: '2023-05-26T00:47:15.907233+00:00'
tactics:
- '[[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]'
techniques:
- '[[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]'
platforms:
- Web
tags:
- '[[OSINT]]'
- '[[public]]'
commands:
- '[[Sublist3r Domain Name Enumeration with OSINT]]'
---

# Domain Record Enumeration using OSINT

**Status**: ✓ Verified

## Summary

Query Open Source Intelligence for information on a target's domain and sub domains. 

## Description

# Description

Query Open Source Intelligence for information on a target's domain and sub domains.

# Instructions

**Command** ([[Sublist3r Domain Name Enumeration with OSINT]]):

```bash
sublist3r -d $_DOMAIN
```

## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]

### Techniques

- [[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]

## Commands Used

- [[Sublist3r Domain Name Enumeration with OSINT]]

## Tags

- [[OSINT]]
- [[public]]
