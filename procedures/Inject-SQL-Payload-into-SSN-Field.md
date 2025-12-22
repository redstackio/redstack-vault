---
tags:
  - sqli-injection
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.927Z'
sub_techniques: []
id: 2f296340-0630-4a11-a9a5-19021c3564bd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-SQL-Payload-into-SSN-Field

## Summary

This procedure introduces a classic SQL injection payload into the SSN field to alter the authentication query, always evaluating to true and bypassing login checks.

## Description

With maxlength bypassed, enter a payload like ' OR '1'='1 to close the string in the SQL query (e.g., SELECT * FROM users WHERE ssn = '' OR '1'='1' AND birthdate = ?), logging in if the birth date matches any record. This can lead to data exfiltration or further escalation.

## Requirements

1. SSN field modified for longer input
2. Birth date entered

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries
- Input sanitization and escaping

## Objectives

1. Manipulate SQL query for unauthorized access
2. Access other users' scholarship data
3. Demonstrate injection vulnerability

## Instructions

### Step 1: Type Payload

**Context**: Enter the SQL tautology payload into the SSN field.

Form input:

```plaintext
' OR '1'='1
```

> The payload exploits lack of sanitization, making the WHERE clause always true.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sqli-injection]]
- [[auth-bypass]]
