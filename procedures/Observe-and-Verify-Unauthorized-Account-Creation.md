---
id: proc-uuid-3
tags:
  - csrf
  - account-takeover
  - verification
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.718Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-and-Verify-Unauthorized-Account-Creation

## Summary

This procedure confirms the success of the CSRF attack by checking for the new account creation and accessing the resulting dashboard on Factlink.

## Description

After the form submission, the endpoint processes the request as legitimate due to the victim's session, creating the account and redirecting to the home dashboard. The attacker can then log in with the predefined credentials to verify control.

## Requirements

1. The predefined credentials used in the HTML form
2. Access to the Factlink login page
3. Ability to monitor user creation logs if available

## Defense

Defensive measures and detection strategies:

- Rate-limit account creations per IP/session
- Require CAPTCHA or additional verification for sign-ups
- Audit logs for suspicious creation patterns

## Objectives

1. Validate account creation occurred
2. Confirm attacker access to the new account
3. Assess potential for further exploitation

## Instructions

### Step 1: Attempt Login with New Credentials

**Context**: Use the email and password from the form to log in and confirm creation.

Navigate to https://staging.factlink.com/users/sign_in and enter the credentials.

> Expected output: Successful login and redirect to the home dashboard, indicating account exists.

### Step 2: Check Dashboard and Logs

**Context**: Inspect the dashboard for new account details and any admin logs if accessible.

Once logged in, verify user profile matches the injected details.

> Expected output: Profile shows attacker-specified full_name, email, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[account-creation]]
- [[verification]]
