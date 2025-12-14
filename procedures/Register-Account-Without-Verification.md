---
id: proc-register-dod-account
tags:
  - information-disclosure
  - registration
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:16:37.498Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Register-Account-Without-Verification

## Summary

This procedure exploits an open registration endpoint on a DoD subdomain to create an account without email confirmation or restrictions, while simultaneously disclosing sensitive information about 162 organizations and 144,366 managers for reconnaissance purposes.

## Description

The registration page at https://██████/Disclaimer.aspx?user=new lacks access controls, allowing anyone to register using disposable emails and view internal organizational details. This enables initial foothold and reconnaissance, setting the stage for further exploitation like XSS. The target environment is a .NET-based web application on a U.S. Department of Defense subdomain.

## Requirements

1. Web browser with internet access to the target subdomain (https://█████).
2. No credentials or tools required; disposable email optional for anonymity.
3. Basic understanding of web navigation.

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration forms to prevent abuse.
- Restrict public access to sensitive data listings; require authentication for viewing organizational info.
- Monitor for anomalous registration patterns, such as high-volume disposable email usage.

## Objectives

1. Create a valid user account for authenticated access.
2. Gather reconnaissance data on organizations and managers.
3. Establish initial access without verification hurdles.

## Instructions

### Step 1: Access Registration Page

**Context**: Navigate to the target subdomain and locate the open registration endpoint to begin account creation and data collection.

No specific command; use browser to visit https://██████/Disclaimer.aspx?user=new.

> The page loads without restrictions, displaying a form for registration and a public list of 162 organizations and 144,366 managers. Note this data for reconnaissance, as it aids in social engineering or targeted attacks.

### Step 2: Complete Registration

**Context**: Fill out the form to submit a new account, confirming no email verification is required.

No specific command; enter details like username, disposable email, and password in the form, then submit.

> Upon submission, the account is created immediately, redirecting to login or dashboard. Verify success by checking for any confirmation message or direct access.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[web]]
- [[Reconnaissance]]
