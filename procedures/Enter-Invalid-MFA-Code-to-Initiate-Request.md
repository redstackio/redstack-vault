---
tags:
  - mfa-invalid
  - request-trigger
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.295Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f226adf3-e3e7-43ff-9e86-e670511a5a85
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enter-Invalid-MFA-Code-to-Initiate-Request

## Summary

Input a random invalid MFA code on the challenge page to trigger the submission of the POST request, which can then be intercepted and modified.

## Description

On the MFA prompt after credential submission, enter any non-valid code (e.g., 123456) and click 'Sign in securely'. This forces the client to send the POST to /v3/api/login, where the vulnerability lies. No real MFA code is needed, as the bypass occurs pre-validation.

## Requirements

1. Active MFA challenge page
2. Proxy tool configured (e.g., Burp)

## Defense

Defensive measures and detection strategies:

- Log invalid MFA attempts and lock accounts after thresholds
- Validate MFA codes server-side before further processing

## Objectives

1. Initiate the vulnerable request flow
2. Avoid using valid codes to prevent alerts
3. Set up for payload modification

## Instructions

### Step 1: Input Invalid Code

**Context**: Proceed with submission despite invalid input.

Enter random 6-digit code; click 'Sign in securely'.

> Expected: Request captured in proxy; error if not intercepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mfa-invalid]]
- [[request-trigger]]
