---
id: proc-uuid-step3
tags:
  - csrf
  - protection-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:46:32.094Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify Absence of CSRF Protections

## Summary

This procedure checks for missing CSRF mitigations on the profile update endpoint, confirming that cross-origin requests can be submitted without validation.

## Description

CSRF vulnerabilities arise from the lack of token validation, origin checks, or referer header enforcement, allowing attackers to forge requests from external sites. In this case, the POST to /██████ accepts submissions without these protections, enabling the chaining with XSS for seamless exploitation.

## Requirements

1. Knowledge of the endpoint and parameters from prior interception
2. Ability to craft simple cross-origin requests (e.g., via browser dev tools or HTML)
3. Valid authentication context for testing

## Defense

Defensive measures and detection strategies:

- Implement synchronizer token pattern for CSRF protection
- Enforce strict origin and referer header validation
- Use SameSite=Strict/Lax cookies to mitigate cross-site requests

## Objectives

1. Confirm no CSRF token is required or validated
2. Test cross-origin submission success
3. Identify feasibility for PoC crafting

## Instructions

### Step 1: Inspect Request for Tokens

**Context**: Review the captured request for built-in protections.

Examine headers and body in Burp for CSRF-related fields (e.g., _csrf, X-CSRF-Token). Check server responses for errors on missing tokens.

### Step 2: Test Cross-Origin Submission

**Context**: Attempt submission from a different origin to verify acceptance.

Create a local HTML file with a form posting to /██████ using the known parameters, omitting any token. Load it in a browser and submit.

**Expected Output**: Server accepts the request and processes the update without CSRF errors, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- protection-bypass
