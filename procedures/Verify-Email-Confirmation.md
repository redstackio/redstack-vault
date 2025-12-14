---
id: proc-verify-email
tags:
  - email
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.359Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify Email Confirmation

## Summary

This procedure completes the email verification for the bypassed account by clicking the confirmation link sent to the victim's actual email address, activating the unauthorized account.

## Description

After account creation, HackerOne sends a verification email to the base email (ignoring trailing characters). This step requires access to the email inbox, often via social engineering. Target is the verification endpoint. Prerequisites: Successful bypass and email receipt. Outcome: Account fully activated for login.

## Requirements

1. Access to the victim's email inbox
2. Verification link from HackerOne
3. No tools beyond email client

## Defense

Defensive measures and detection strategies:

- Send verification to exact normalized email and require exact match on click
- Monitor for verification clicks from unexpected IPs or sessions
- Implement secondary auth factors for new accounts

## Objectives

1. Activate the unauthorized account
2. Enable login without further restrictions
3. Bridge to SSO access in linked organizations

## Instructions

### Step 1: Receive and Click Link

**Context**: Wait for the verification email and click the link in the victim's session.

No command; manual action:

Open the email and click the verification URL (e.g., https://hackerone.com/users/verify?token=...).

> Expected: Page confirms "Email verified successfully." Account status updates to verified.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- email
- verification
