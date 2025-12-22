---
id: 48b1c906-8d4b-4d5b-b770-d023fa78d142
name: find-interesting-strings-in-raw-memory-dump
type: procedure
verified: true
submitted: false
created_at: '2020-03-31T05:01:26.346855+00:00'
updated_at: '2023-05-25T19:46:57.396431+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
sub_techniques: []
tags:
  - memory
commands:
  - '[[commands/strings-search-raw-data-for-human-readable-strings]]'
platforms:
  - Windows
  - Linux
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: none
validated: true
---

# find-interesting-strings-in-raw-memory-dump

## Summary

This procedure extracts human-readable strings from a raw memory dump file using the strings command, revealing credentials, configs, or keys without advanced forensics.

## Description

Memory dumps contain ASCII/Unicode strings from processes. Grepping for keywords like 'password' or 'admin' quickly yields value. Effective first pass before Volatility or full analysis.

## Requirements

1. .dmp file exfiltrated to attacker
2. strings and grep on Linux
3. Keyword list (password, key, admin)

## Defense

- Clear memory on process exit
- Use full-disk encryption and secure boot
- Detect dump exfil via DLP

## Objectives

1. Identify readable artifacts
2. Extract creds for cracking
3. Guide deeper analysis

## Instructions

### Step 1: Run Strings Extraction

**Context**: Convert dump to strings.

strings $_DUMP_FILE > strings.txt

> Filters printable chars >4 bytes.

### Step 2: Grep for Interests

**Context**: Search for sensitive data.

**Command** ([[commands/strings-search-raw-data-for-human-readable-strings]]):
```bash
strings $_DUMP_FILE | grep -i $_KEYWORD
```

> Use -A 5 for context post-match.

### Step 3: Analyze Hits

**Context**: Manually review for validity.

cat strings.txt | grep -C 2 "password"

> Save useful strings to creds.txt.
