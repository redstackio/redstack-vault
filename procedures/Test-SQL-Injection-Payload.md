---
id: proc-test-sqli-payload
tags:
  - sqli
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-basic-sqli-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.622Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test SQL Injection Payload

## Summary

This procedure tests for SQL injection vulnerabilities by injecting a simple payload into the search query to elicit database errors, confirming lack of input sanitization.

## Description

SQL injection occurs when user input is concatenated directly into SQL queries. Testing with a single quote or comment disrupts the query syntax, exposing errors if no parameterization is used. In this scenario, it reveals the vulnerability in search handling, paving the way for data exfiltration.

## Requirements

1. Identified search endpoint from reconnaissance
2. Command-line access for curl or equivalent
3. Understanding of SQL syntax basics

## Defense

Defensive measures and detection strategies:

- Enforce input validation and escaping on all query parameters
- Deploy intrusion detection systems (IDS) to flag SQL keywords in inputs
- Use prepared statements or ORMs in application code

## Objectives

1. Trigger SQL syntax error
2. Confirm vulnerability type (e.g., error-based)
3. Assess response for further exploitation clues

## Instructions

### Step 1: Inject Single Quote

**Context**: Send a payload that breaks SQL string termination to provoke an error.

**Command** ([[commands/curl-basic-sqli-test]]):
```bash
curl "https://target.com/search?q='" -v
```

> Look for error messages like "SQL syntax error near '''" in the response body, indicating unsanitized input reaches the database.

### Step 2: Test Comment Bypass

**Context**: Append a comment to ignore trailing query parts, verifying control.

**Command** ([[commands/curl-basic-sqli-test]]):
```bash
curl "https://target.com/search?q='--" -v
```

> Successful bypass shows no errors and potentially altered results, confirming injection point.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-sqli-test]]

## Tools Used


## Tags

- sqli
- injection
