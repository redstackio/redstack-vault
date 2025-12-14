---
id: p-identify-csrf-endpoint-concrete
tags:
  - csrf
  - recon
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:06.328Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify Vulnerable CSRF Endpoint in Concrete CMS

## Summary

This procedure involves reconnaissance to identify the profile preferences save endpoint in Concrete CMS that lacks CSRF protection, enabling subsequent forgery of user profile updates.

## Description

In Concrete CMS, the profile update functionality at `/profile/preferences/-/save/` processes POST requests to modify user details like username, email, and account type without requiring CSRF tokens or password confirmation. This procedure uses browser tools or source analysis to confirm the vulnerability, setting the stage for account takeover by verifying that forged requests can alter sensitive data.

## Requirements

1. Access to the target Concrete CMS instance (publicly accessible)
2. Web browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTTP requests and web forms

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Require password confirmation for sensitive profile changes
- Monitor for anomalous profile update requests from unusual sources

## Objectives

1. Confirm the endpoint's lack of CSRF validation
2. Document required POST fields for exploitation
3. Validate that updates succeed without authentication challenges

## Instructions

### Step 1: Inspect Network Traffic

**Context**: Use browser developer tools to capture legitimate profile update requests and analyze for missing protections.

Navigate to the profile preferences page on the target site, attempt a test change, and monitor the Network tab for the POST request to `/profile/preferences/-/save/`.

**Expected Output**: Request details showing form data like `uName=newusername`, `uEmail=attacker@example.com`, `uAccountType=owner` without a CSRF token field.

### Step 2: Test Forged Request Manually

**Context**: Simulate a forged request using browser console or a tool like Postman to confirm vulnerability.

In the browser console (while authenticated), execute a simple fetch or form submission mimicking the POST without tokens.

**Expected Output**: Successful update of profile details, confirming no validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[recon]]
- [[concrete-cms]]
