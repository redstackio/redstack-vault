---
tags:
  - sqli
  - identification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/basic-sqli-identification-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.248Z'
sub_techniques: []
id: 5e2bf5c3-8a60-4969-a1d3-b09fec51ad07
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-SQL-Injection-in-doc_id-Parameter

## Summary

This procedure tests the 'doc_id' parameter in the library.php endpoint for SQL injection vulnerabilities by appending basic payloads and observing responses for errors or behavioral changes.

## Description

In a web application using PHP and MySQL, the lack of input sanitization in the doc_id parameter allows arbitrary SQL to be concatenated into backend queries. Testing involves sending requests to https://████/library.php?path=test&doc_id=1 with payloads like single quotes or boolean expressions to detect injection points. This is the initial reconnaissance step in exploiting blind SQLi on a public-facing DoD website.

## Requirements

1. Network access to the target endpoint
2. Ability to send HTTP GET requests (e.g., via curl or browser)
3. Basic understanding of SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in PHP
- Use input validation and sanitization (e.g., mysqli_real_escape_string)
- Monitor application logs for anomalous SQL errors or delays
- Deploy WAF rules to block common SQLi payloads

## Objectives

1. Confirm presence of SQL injection vulnerability
2. Identify if it's blind (no direct output) or error-based
3. Establish baseline response times for further testing

## Instructions

### Step 1: Send Basic Injection Test

**Context**: Append a single quote to trigger potential syntax errors in the SQL query.

**Command** ([[commands/basic-sqli-identification-test]]):
```bash
curl -X GET "https://████/library.php?path=test&doc_id=1'" -v
```

> This sends a GET request with a trailing single quote in doc_id. Expected output includes a 500 error or database syntax error if vulnerable.

### Step 2: Test Boolean Conditions

**Context**: Use simple OR conditions to alter query logic and observe response differences.

**Command** ([[commands/basic-sqli-identification-test]]):
```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 OR 1=1" -v
```

> Look for successful page loads or errors indicating injection; false conditions like 1=2 should differ.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/basic-sqli-identification-test]]

## Tools Used


## Tags

- [[sqli]]
- [[web]]
