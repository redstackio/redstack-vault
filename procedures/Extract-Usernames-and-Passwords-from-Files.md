---
tags:
  - credential-extraction
type: procedure
tools:
  - '[[tools/download.py]]'
  - '[[tools/grep]]'
  - '[[tools/GPU]]'
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Credential Dumping]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 84820c07-a963-445a-847e-a1605636e8db
created_at: '2025-12-11T06:10:40.294Z'
updated_at: '2025-12-11T06:10:40.294Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1003]]'
---
# Extract Usernames and Passwords from Files

## Summary

This procedure involves parsing downloaded files from a vulnerable VPN server to extract plaintext usernames and passwords using simple search tools.

## Description

After obtaining files via arbitrary read, attackers use pattern matching to pull out cached plaintext credentials from system and database files, enabling further access without brute-forcing.

## Requirements

1. Downloaded files from the target (e.g., /data/runtime/mtmp/system)
2. [[tools/grep]] or similar text processing tool
3. Local environment for analysis

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive data at rest and avoid plaintext caching
- Monitor file access logs for unusual reads

## Objectives

1. Compile list of valid credentials
2. Prepare for authentication bypass
3. Escalate access using extracted data

## Instructions

### Step 1: Search for Credentials

**Context**: Grep for patterns indicating usernames and passwords.

Execute [[tools/grep]] on the files:

```bash
grep -E 'username|password' /data/runtime/mtmp/system
grep -E 'username|password' /data/runtime/mtmp/lmdb/dataa/data.mdb
```

> This extracts plaintext credentials cached after user logins.

### Step 2: Compile Credential List

**Context**: Organize extracted data for use.

Manually curate the results into a usable list of username:password pairs.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credential Dumping]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/grep]]

## Tags

- [[credential-extraction]]
