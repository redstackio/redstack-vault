---
tags:
  - impersonation
  - email-spoof
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:31:52.506Z'
sub_techniques: []
id: 28edf7ee-dbde-40f3-a48f-e656d9efc302
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Phishing]]'
---
# Submit-Impersonated-Appeal-with-Victim-Email

## Summary

This procedure finalizes the attack by entering a victim's email address and submitting the appeal form, resulting in a spoofed confirmation email sent to the impersonated user.

## Description

With the form accessible, attackers input another user's email to spoof identity. Optional validation via query parameter confirms reachability, and submission triggers server-side email dispatch, compromising confidentiality without detection.

## Requirements

1. Fully populated form via prior steps
2. Known victim email address
3. Proxy for any final interceptions

## Defense

Defensive measures and detection strategies:

- Require authenticated sessions for email inputs and submissions
- Audit logs for anomalous submissions (e.g., IP mismatches)
- Email validation with sender verification

## Objectives

1. Impersonate user via email spoofing
2. Submit unauthorized appeal
3. Trigger victim notification

## Instructions

### Step 1: Enter Victim Email

**Context**: Spoof identity in the form.

In the email field, input the target's email (e.g., victim@domain.com). Optionally, test validation by navigating to /app/CreateAppeal.aspx?email=victim@domain.com and intercepting.

**Expected Output**: Email field accepts input; validation (if done) succeeds.

### Step 2: Submit Form

**Context**: Complete and send the appeal.

Fill remaining fields and click submit; intercept any final 302 if needed and change to 200.

**Expected Output**: Success message; email sent to victim confirming submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[impersonation]]
- [[email-spoof]]
