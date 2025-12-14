---
tags:
  - csrf
  - token-extraction
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:29.380Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: af60e336-e5ec-4171-b8f6-772fc0153225
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-CSRF-Token-from-Legitimate-Form

## Summary

This procedure involves creating an account on the target application and performing a legitimate form submission to extract a valid CSRF token, which can then be reused in forged requests for unauthorized actions.

## Description

In the context of the ███████mil application, the 'My Account' page forms lack proper CSRF token validation on submissions. By logging in, navigating to the page, and submitting a benign change (e.g., updating a phone number), the attacker can inspect the network request or HTML source to obtain the token value named ██████████. This token is session-bound and allows the attacker to craft requests that appear legitimate. Prerequisites include having an attacker account and basic web inspection skills. Expected outcome is possession of a reusable token for CSRF exploitation.

## Requirements

1. Valid attacker account on ███████mil
2. Web browser with developer tools (e.g., Chrome DevTools)
3. Internet access to the target application

## Defense

Defensive measures and detection strategies:

- Implement and enforce CSRF token validation on all state-changing endpoints
- Use SameSite cookies to mitigate session hijacking in cross-site contexts
- Monitor for anomalous form submissions from unusual referrers

## Objectives

1. Obtain a valid, session-specific CSRF token
2. Understand the form structure for PoC crafting
3. Enable subsequent forged requests without authentication bypass

## Instructions

### Step 1: Account Creation and Login

**Context**: Establish an authenticated session to access protected forms.

Log in to the ███████mil application using your attacker account credentials.

### Step 2: Perform Legitimate Update and Inspect Token

**Context**: Trigger a form submission to expose the CSRF token in the request.

Navigate to the 'My Account' page, select an update form (e.g., phone number), enter a temporary change, and submit. Open browser developer tools (F12), go to the Network tab, and inspect the submitted request. Locate the CSRF token parameter (██████████) and copy its value.

> Alternatively, view the page source before submission to find the hidden input field containing the token.

**Expected Output**: A string value for the CSRF token, e.g., a 32-character hexadecimal token.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[Reconnaissance]]
