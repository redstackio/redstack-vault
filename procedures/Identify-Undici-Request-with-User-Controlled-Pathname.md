---
id: 123e4567-e89b-12d3-a456-426614174001
name: Identify-Undici-Request-with-User-Controlled-Pathname
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.238Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - ssrf
  - recon
platforms:
  - Node.js
  - JavaScript
tools:
  - '[[tools/undici]]'
commands: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Identify-Undici-Request-with-User-Controlled-Pathname

## Summary

This procedure involves examining the target application's code to identify instances of undici.request where the pathname option accepts user-controlled input without proper validation, setting the stage for SSRF exploitation.

## Description

In applications using the undici HTTP client library for Node.js, the pathname parameter in undici.request is intended to append a relative path to the specified origin. However, if user input is passed directly to pathname without checking for absolute or protocol-relative URLs, attackers can override the origin and direct requests to internal hosts. This procedure focuses on reconnaissance to locate such vulnerable code paths, typically through code review or black-box testing of input fields.

## Requirements

1. Access to application source code or ability to test inputs (e.g., via API endpoints)
2. Node.js environment for testing
3. Knowledge of the application's request-handling logic

## Defense

Defensive measures and detection strategies:

- Validate and sanitize pathname inputs to ensure they are relative paths only
- Use URL parsing libraries to enforce origin restrictions
- Monitor for anomalous outbound requests to internal IPs

## Objectives

1. Locate vulnerable undici.request calls
2. Confirm user control over pathname
3. Prepare for payload injection

## Instructions

### Step 1: Review Application Code

**Context**: Search for undici.request invocations and trace pathname sources.

No specific command; manually inspect code for patterns like `undici.request({ origin: baseUrl, pathname: userInput })`.

> Look for lack of validation on userInput.

### Step 2: Test Input Fields

**Context**: If source access is limited, fuzz inputs to endpoints that trigger HTTP requests.

Submit test strings like '/test' to confirm pathname influence, then escalate to suspicious payloads.

> Expected: No immediate errors, indicating potential vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/undici]]

## Tags

- [[ssrf]]
- [[recon]]
