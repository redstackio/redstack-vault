---
tags:
  - xss
  - waf
  - payload-test
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.133Z'
sub_techniques: []
id: 9983fd24-b5ff-4afc-b997-9331ea637553
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test XSS Payloads Against WAF

## Summary

This procedure attempts standard XSS payloads in the reflected 'url' parameter to evaluate WAF blocking, identifying the need for bypass techniques.

## Description

With reflection confirmed, inject common XSS strings like <script>alert(1)</script> into the error-triggering request. The WAF typically intercepts these, returning blocks or sanitized outputs, but confirms the vulnerability type.

## Requirements

1. Confirmed reflection from previous procedure
2. List of standard XSS payloads
3. Ability to send and observe HTTP responses

## Defense

Defensive measures and detection strategies:

- Tune WAF rules for XSS patterns in API parameters
- Implement client-side escaping for reflected content
- Log and alert on blocked XSS attempts

## Objectives

1. Trigger WAF blocks on XSS attempts
2. Understand protection mechanisms
3. Gather data for bypass fuzzing

## Instructions

### Step 1: Send Standard Payload

**Context**: Use a basic XSS payload to test interception.

**Command** ([[commands/curl-test-xss]]):
```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=<script>alert(1)</script>" -H "Authorization: Bearer YOUR_API_TOKEN"
```

> Expect a WAF block (e.g., 403) or stripped payload in response.

### Step 2: Iterate Payloads

**Context**: Test variations to map WAF behavior.

Repeat with payloads like <img src=x onerror=alert(1)>.

> Document which are blocked to inform bypass strategy.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss]]

## Tools Used


## Tags

- [[xss]]
- [[waf]]
- [[payload-test]]
