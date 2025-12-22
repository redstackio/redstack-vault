---
id: proc-uuid-1102591
name: Detect-and-Confirm-Blind-SQL-Injection
tags:
  - blind-sqli
  - sql-injection
  - web
  - dod
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.004Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect-and-Confirm-Blind-SQL-Injection

## Summary

This procedure outlines the detection and confirmation of a Blind SQL Injection vulnerability in a web application by injecting malformed SQL payloads into URL-encoded POST parameters and observing boolean-based response differences, enabling inference attacks on the backend database without direct error exposure.

## Description

In a typical attack scenario targeting public-facing web applications like those in government sectors, attackers identify POST endpoints processing user input without proper sanitization. By crafting payloads that alter SQL query logic, they force the database to evaluate conditions, inferring true/false outcomes from application responses (e.g., page content or timing). This vulnerability, reported in a U.S. Department of Defense application, allows potential data extraction or server control through chained inferences. Prerequisites include access to a proxy tool for request manipulation and knowledge of SQL syntax.

## Requirements

1. Network access to the target web application endpoint (e.g., HTTPS on port 443)
2. Tools for intercepting and modifying HTTP POST requests (e.g., browser dev tools or Burp Suite)
3. Basic understanding of SQL injection techniques and boolean logic

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries to sanitize all user inputs
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns in requests
- Enable database logging to monitor for unusual query evaluations and response anomalies

## Objectives

1. Confirm the presence of a blind SQL injection vulnerability
2. Map response behaviors for TRUE/FALSE conditions to enable data inference
3. Document exploitation for reporting and remediation

## Instructions

### Step 1: Identify and Target the Vulnerable Endpoint

**Context**: Locate the POST parameter vulnerable to injection by sending baseline requests and inspecting for processing flaws.

Intercept the POST request to https://██████████/██████ and focus on the URL-encoded parameter ███. Submit a legitimate value and note the baseline response.

> Expected: Standard application output without errors.

### Step 2: Inject Basic SQL Payload for Initial Testing

**Context**: Introduce SQL syntax to check if the parameter influences query execution without revealing errors.

Modify the parameter to `-1' OR 3 _2_ 1=6 AND 1=1 or '4mEwSPwJ'='` and submit the request. Compare the response to the baseline.

> Expected: Subtle change in response (e.g., different content or status), indicating blind injection.

### Step 3: Execute Boolean-Based Confirmation Tests

**Context**: Use conditional payloads to verify inference capability by differentiating TRUE and FALSE outcomes.

Submit sequential requests with these payloads:
- `-1' OR 1=1 or '4mEwSPwJ'='` (should return TRUE response)
- `-1' OR 2=4 or '4mEwSPwJ'='` (should return FALSE response)
- `-1' OR 3 _2<(1+2+4) or '4mEwSPwJ'='` (TRUE, testing arithmetic)
- `-1' OR 3_ 2>(1+2+4) or '4mEwSPwJ'='` (FALSE, testing arithmetic)

Observe patterns in responses to confirm boolean evaluation.

> Expected: Consistent differentiation allowing logical inference of database state.

### Step 4: Document the Exploitation

**Context**: Record the process to provide verifiable proof of the vulnerability.

Use screen recording software to capture the request crafting, payload injection, and response analysis.

> Expected: Video showing reproducible TRUE/FALSE behaviors tied to SQL conditions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[blind-sqli]]
- [[sql-injection]]
- [[web]]
- [[dod]]
