---
tags:
  - bruteforce
  - directory-enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/convert-hex-timestamp-to-utc]]'
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3e80442d-de3a-48e6-947b-8d7b666bd622
created_at: '2025-12-14T17:23:27.996Z'
updated_at: '2025-12-14T17:23:27.996Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Bruteforce-Temporary-Directory-Location

## Summary

This procedure predicts and bruteforces the name of the temporary directory created during the file import, using the UTC timestamp-based uniqid() to locate the uploaded PHP webshell.

## Description

Concrete CMS generates temp directories as volatile-0-[uniqid()], where the first 8 hex chars are the UTC timestamp in hex, and the last 5 are random. By converting the approximate timestamp and trying 00000-fffff suffixes, the exact directory in /application/files/ is found.

## Requirements

1. Approximate UTC time of import start
2. Access to target's file structure (via web or shell)
3. Python for timestamp conversion

## Defense

Defensive measures and detection strategies:

- Use cryptographically secure random IDs for temp files
- Restrict access to temp directories
- Monitor for enumeration attempts on file paths

## Objectives

1. Convert timestamp to predict prefix
2. Enumerate suffixes to find directory
3. Confirm presence of uploaded byc.php

## Instructions

### Step 1: Predict Timestamp Prefix

**Context**: Use import time to generate hex prefix.

**Command** ([[commands/convert-hex-timestamp-to-utc]]):
```python
import datetime
print(datetime.datetime.fromtimestamp(int('0x614daecb',16), tz=datetime.timezone.utc))
```

> Outputs UTC time, e.g., 2021-09-24 10:56:11+00:00; reverse to get 8-char hex prefix.

### Step 2: Bruteforce Directory

**Context**: Scan temp folder for matching directories.

No command; manually or script bruteforce http://target/application/files/volatile-0-[prefix][00000-fffff].

> Directory found when byc.php is accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/convert-hex-timestamp-to-utc]]

## Tools Used


## Tags

- [[bruteforce]]
- [[enumeration]]
