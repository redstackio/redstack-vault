---
tags:
  - credential-extraction
  - plaintext-passwords
type: procedure
tools:
  - '[[tools/download.py]]'
  - '[[tools/GPU]]'
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Credential Dumping]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: ec1b2317-8b7b-47dd-9f8d-0e7179dce3d0
created_at: '2025-12-11T03:48:05.859Z'
updated_at: '2025-12-11T03:48:05.859Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1003]]'
---
# Extract Credentials from Downloaded VPN Files

## Summary

This procedure uses pattern searching to extract usernames and plaintext passwords from files downloaded via VPN exploits, leveraging cached data in system and database files.

## Description

After downloading files like /data/runtime/mtmp/system and .mdb files, grep is used to find cached plaintext credentials post-login. This is effective in environments where passwords are temporarily stored in plaintext.

## Requirements

1. Downloaded files from the target VPN
2. Access to command-line tools like grep
3. Files containing cached session or user data

## Defense

Defensive measures and detection strategies:

- Enable encryption for cached data and monitor file access logs
- Implement least-privilege access and regular patching

## Objectives

1. Obtain usable username/password pairs
2. Enable further access like 2FA bypass
3. Escalate to internal resources

## Instructions

### Step 1: Search for Patterns

**Context**: Grep for username and password strings in the files.

**Command** ([[commands/grep-extract-credentials]]):
```bash
grep -E 'username|password' /data/runtime/mtmp/system
grep -E 'username|password' /data/runtime/mtmp/lmdb/dataa/data.mdb
```

> This extracts pairs from cached data; look for patterns like '█████████ / ████'.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credential Dumping]]

### Sub-Techniques



## Commands Used

- [[commands/grep-extract-credentials]]

## Tools Used

- #grep

## Tags

- #credential-extraction
- #plaintext-passwords
