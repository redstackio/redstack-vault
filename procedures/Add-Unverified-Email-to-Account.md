---
id: proc-uuid-2
tags:
  - email-bypass
  - account-manipulation
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.023Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Additional Cloud Roles]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Add-Unverified-Email-to-Account

## Summary

This procedure exploits a Broken Access Control flaw in Vimeo's 'Add a New Email' feature, allowing an authenticated user to append an arbitrary email address to the account without verification or password confirmation, paving the way for takeover.

## Description

The vulnerability lies in the account settings where adding a new email does not enforce ownership verification of the new address or require re-authentication via the existing password. This violates secure design principles and was demonstrated in a PoC at http://goo.gl/tsqR60. The attack scenario targets logged-in sessions on shared devices, with outcomes including the attacker's email being listed in the profile for subsequent reset use.

## Requirements

1. Active authenticated session in victim's Vimeo account
2. Access to account settings page
3. Attacker's own email address (e.g., attacker@example.com)

## Defense

Defensive measures and detection strategies:

- Require email verification codes for all additions
- Enforce password confirmation for account changes
- Implement rate limiting and anomaly detection on email modifications

## Objectives

1. Add attacker-controlled email to victim's account profile
2. Bypass verification to enable password reset vector
3. Maintain stealth by avoiding alerts during addition

## Instructions

### Step 1: Navigate to Account Settings

**Context**: From the logged-in dashboard, access the email management section.

Click on the profile icon, then select 'Settings' > 'Emails' or similar path to the 'Add a New Email' form.

> The page loads the current email list without additional auth.

### Step 2: Submit New Email

**Context**: Enter and add the attacker's email without triggering checks.

Fill in the email field with 'attacker@example.com' and click 'Add' or 'Save'.

> No verification email is sent, and the email is immediately added to the list. PoC reference: http://goo.gl/tsqR60.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques

- [[Additional Cloud Roles]]

## Commands Used


## Tools Used


## Tags

- [[email-bypass]]
- [[account-manipulation]]
