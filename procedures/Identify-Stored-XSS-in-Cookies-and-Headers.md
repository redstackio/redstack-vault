---
id: p-stored-xss-cookies-headers
tags:
  - xss
  - stored-xss
  - cookies
  - headers
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-xss-cookie-header]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:55.699Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Identify Stored XSS in Cookies and Headers

## Summary

This procedure detects unexploitable stored XSS on endpoints like https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/, where payloads in cookies and headers are stored but not executed due to encoding, preparing for cache-based escalation.

## Description

Stored XSS was identified on survey pages when payloads are submitted via cookies and custom headers, persisting in storage but sanitized on render. This targets web apps with header/cookie processing. Outcomes include payload persistence confirmation for poisoning integration.

## Requirements

1. Access to survey or input endpoints
2. Capability to inject custom HTTP headers and cookies
3. Tools for request submission and response inspection

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all stored inputs from headers/cookies
- Implement server-side validation for custom headers
- Log and alert on suspicious header values

## Objectives

1. Locate stored XSS injection point
2. Confirm non-execution due to safeguards
3. Capture stored payload for chaining

## Instructions

### Step 1: Submit Payload via Cookie and Header

**Context**: Inject XSS into cookie and header on the survey endpoint to test storage.

**Command** ([[commands/curl-test-xss-cookie-header]]):
```bash
curl -H "Cookie: vuln=\"<script>alert(1)</script>\"" -H "X-Custom: \"<script>alert(1)</script>\"" "https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/" -v
```

> Submit the request and check if the payload is stored (e.g., in session or DB echo). No execution expected.

### Step 2: Retrieve and Inspect Stored Payload

**Context**: Request the page again to verify persistence without triggering.

**Command** ([[commands/curl-test-xss-cookie-header]]):
```bash
curl -H "Cookie: vuln=\"<script>alert(1)</script>\"" "https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/" | grep -i script
```

> Grep response for the payload. Success if it's present but encoded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-cookie-header]]

## Tools Used


## Tags

- xss
- stored-xss
