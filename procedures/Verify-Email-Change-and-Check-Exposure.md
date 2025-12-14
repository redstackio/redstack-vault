---
id: proc-twitter-verify-exposure-001
tags:
  - twitter
  - android
  - verification
  - exposure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:45.322Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-Email-Change-and-Check-Exposure

## Summary

This procedure completes the email verification process and confirms that previously private tweets are now publicly accessible due to the unset protection, validating the full impact of the vulnerability.

## Description

After the email change initiation, the verification link is accessed from the new email on the same Android device. The procedure then checks tweet visibility from external views (e.g., incognito browser or another account) to confirm exposure. This step occurs post-logic error trigger and highlights the privacy violation. Target is Twitter's verification flow and public tweet search. Prerequisites include pending email verification. Expected outcome is confirmed public access to private content.

## Requirements

1. Access to the new email inbox
2. Same Android device for verification
3. Secondary account or incognito mode for checking exposure

## Defense

Defensive measures and detection strategies:

- Implement post-change audits for protection status in the app
- Use Twitter's search tools or API to monitor sudden visibility changes
- Alert users via email after any account setting modifications
- Browser-based checks for tweet visibility as a user habit

## Objectives

1. Finalize the email change
2. Confirm unintended data exposure
3. Assess impact for remediation or exploitation

## Instructions

### Step 1: Access Verification Email

**Context**: Retrieve and open the confirmation link.

No command required; check the new email inbox for Twitter's verification message and tap the link.

> Expected output: Browser or app opens to verification page; email confirmed.

### Step 2: Complete Verification on Device

**Context**: Ensure verification ties back to the app session.

No command required; if prompted, confirm in the Twitter app on the same device.

> Expected output: Success message in app; email updated in settings.

### Step 3: Check Tweet Exposure

**Context**: Validate public visibility.

No command required; from another Twitter account or incognito browser, search for and view previously private tweets.

> Expected output: Tweets now appear in public searches and profiles.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[android]]
- [[verification]]
- [[exposure]]
