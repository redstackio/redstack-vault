---
id: proc-csrf-credential-config
tags:
  - csrf
  - credentials
  - configuration
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:36.016Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Configure-CSRF-with-Attacker-Credentials

## Summary

This procedure configures the CSRF POC HTML by inserting valid attacker credentials, preparing it to force a victim login into the attacker's Unikrn account.

## Description

Building on the POC HTML, this step embeds the attacker's email and password into the form's hidden fields. The vulnerability stems from no session validation, allowing cross-site POSTs to succeed. In the attack scenario, once submitted by the victim, it authenticates as the attacker, hijacking the victim's session for monitoring or further actions like adding wallet payments or linking Steam accounts. Prerequisites: Valid Unikrn attacker account and the POC HTML from prior procedure.

## Requirements

1. Valid Unikrn email and password for attacker account
2. Access to the POC HTML file
3. Basic text editing capabilities

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on logins to prevent unauthorized access
- Log and alert on logins from mismatched IP/user-agent combinations
- Rate-limit login attempts from cross-origin requests

## Objectives

1. Securely insert credentials into hidden form fields
2. Ensure the form remains stealthy (no visible credential exposure)
3. Prepare for delivery without leaking credentials in transit

## Instructions

### Step 1: Edit Hidden Inputs

**Context**: Replace placeholder values in the HTML form with actual attacker details.

Open `csrf-poc.html` and update:

```html
<input type="hidden" name="usr" value="attacker@example.com">
<input type="hidden" name="pwd" value="attackerPassword123">
```

> Use real values; ensure no JavaScript exposes them. Save the file.

### Step 2: Validate Configuration

**Context**: Test the updated form in a controlled environment to confirm it submits correctly.

Load the HTML in a browser, submit, and verify the POST payload in dev tools includes the correct usr and pwd.

> Expected: Request body shows form-data with encoded credentials; response indicates successful auth if tested against a dummy account.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[Credentials]]
- [[configuration]]
