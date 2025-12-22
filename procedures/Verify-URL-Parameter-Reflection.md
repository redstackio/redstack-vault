---
tags:
  - reflection
  - parameter
  - xss-prep
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-reflection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:18.138Z'
sub_techniques: []
id: c0ab85e0-d4af-4f85-b090-3ee8b22e96d2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify URL Parameter Reflection

## Summary

This procedure tests whether the 'url' parameter in the Semrush API error response is reflected without sanitization, confirming a potential vector for HTML/JavaScript injection.

## Description

By injecting a traceable string into the 'url' parameter during error triggering, attackers can observe if it's directly echoed in the MongoDB error message. This lack of escaping enables subsequent XSS payloads. Applicable to APIs with reflective error handling.

## Requirements

1. Successful MongoDB error trigger from prior step
2. HTTP request tool
3. Valid API credentials

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before inclusion in error messages
- Use parameterized queries in database interactions
- Monitor for repeated error-triggering requests

## Objectives

1. Confirm direct reflection of input in error output
2. Assess sanitization level (e.g., HTML encoding)
3. Prepare for payload injection testing

## Instructions

### Step 1: Inject Test String

**Context**: Use a unique string to track reflection in the response.

**Command** ([[commands/curl-verify-reflection]]):
```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=test_reflection" -H "Authorization: Bearer YOUR_API_TOKEN"
```

> The response should include "test_reflection" verbatim in the error message, indicating no sanitization.

### Step 2: Inspect for Reflection

**Context**: Parse the error body to verify exact match.

No command; manual or scripted inspection.

> Success if the input appears unchanged, e.g., as part of the error text.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-reflection]]

## Tools Used


## Tags

- [[reflection]]
- [[parameter]]
- [[xss-prep]]
