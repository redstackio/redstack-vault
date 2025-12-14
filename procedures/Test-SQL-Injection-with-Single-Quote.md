---
tags:
  - sqli
  - injection-test
  - error-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-single-quote-sqli]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bd10fcb4-7ad3-4f3a-bf7c-090cde880b2b
created_at: '2025-12-14T03:46:20.274Z'
updated_at: '2025-12-14T03:46:20.274Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SQL-Injection-with-Single-Quote

## Summary

This procedure tests for SQL injection vulnerabilities by injecting a single quote into a GET parameter, causing a syntax error in the backend query to reveal potential exploitation points.

## Description

In the context of the Khan Academy web application, this targets the language parameter in the /translations/videos endpoint. Appending a single quote disrupts the SQL query, leading to a 500 error if inputs are unsanitized. This confirms the vulnerability before advancing to exploitation, applicable to web apps using dynamic SQL construction without parameterization.

## Requirements

1. Access to the target web endpoint (e.g., https://www.khanacademy.org/translations/videos)
2. Tool for HTTP requests like curl or a browser
3. Basic understanding of URL encoding

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries in backend code
- Implement web application firewalls (WAF) to block quote injections
- Log and monitor for 500 errors correlated with anomalous parameters

## Objectives

1. Confirm SQL injection susceptibility in the language parameter
2. Trigger a database error to validate unsanitized input
3. Establish foundation for boolean-based exploitation

## Instructions

### Step 1: Inject Single Quote

**Context**: Append a single quote to the language code to break the SQL query syntax.

**Command** ([[commands/curl-test-single-quote-sqli]]):
```bash
curl -s "https://www.khanacademy.org/translations/videos/en'_youtube_stats.csv"
```

> This sends a GET request with the malformed URL. A successful test returns a 500 error, indicating the quote reached the database query.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-single-quote-sqli]]

## Tools Used


## Tags

- [[sqli]]
- [[web]]
- [[injection-test]]
