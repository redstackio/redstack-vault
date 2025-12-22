---
id: proc-uuid-9
tags:
  - sqli
  - blind
  - time-based
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/python-quiz-blind-sqli]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:55.513Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1190.003]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Blind-SQL-Injection-to-Extract-Admin-Password

## Summary

This procedure exploits a blind SQL injection in the name field of the Evil Quiz to confirm vulnerability with time delays, enumerate schema, and extract the admin password character-by-character using a Python script for login and flag access.

## Description

Un-sanitized name input allows ' OR sleep(5)=', causing delays for blind confirmation. Use substring/ord in queries to dump password 'S3creT_p4ssw0rd-$' from DB. Targets MySQL quizzes.

## Requirements

1. Python environment
2. Custom SQLi script
3. Target quiz endpoint

## Defense

Defensive measures and detection strategies:

- Parameterized queries/prepared statements
- WAF for SQL patterns
- Monitor query delays

## Objectives

1. Confirm blind SQLi
2. Extract credentials
3. Access admin area flag

## Instructions

### Step 1: Confirm SQLi

**Context**: Inject sleep to detect delay.

Submit name=' OR sleep(5)=' ; measure 5s response.

> Delay confirms vulnerability.

### Step 2: Enumerate Schema

**Context**: Dump tables/columns via conditional queries.

Use blind techniques to find admin password field.

### Step 3: Extract Password

**Context**: Run script for char extraction.

**Command** ([[commands/python-quiz-blind-sqli]]):
```bash
./quiz.py
```

> Outputs Password found: 'S3creT_p4ssw0rd-$'.

### Step 4: Login

**Context**: Use password for admin access.

Login to view flag.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[T1190.003]] Blind SQLi

## Commands Used

- [[commands/python-quiz-blind-sqli]]

## Tools Used

- [[tools/Python]]

## Tags

- [[sqli]]
- [[blind]]
- [[time-based]]
