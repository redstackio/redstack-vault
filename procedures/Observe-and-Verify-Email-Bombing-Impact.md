---
id: proc-khan-observe-impact
tags:
  - impact-verification
  - email-dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Email Service
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:24:18.861Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Observe-and-Verify-Email-Bombing-Impact

## Summary

This procedure monitors the target email account for the effects of the race condition exploitation, confirming multiple unwanted emails and validating that the links are invalid to assess the denial-of-service impact.

## Description

Post-exploitation, a random user (determined by the email entered) receives excessive 'Finish signing up for Khan Academy' emails due to the bypassed checks. Links contain expired or invalid tokens, leading to errors. This contrasts with normal behavior where duplicate emails trigger warnings, demonstrating the vulnerability's effectiveness in causing spam and user confusion without account takeover.

## Requirements

1. Access to the target email inbox (e.g., the entered address)
2. Web browser to test email links
3. Knowledge of normal vs. exploited behavior

## Defense

Defensive measures and detection strategies:

- Implement email throttling and sender reputation checks
- Expire auth tokens quickly and log unusual email volumes
- User notifications for suspicious activity and easy unsubscribe
- SIEM alerts for spikes in email service API calls

## Objectives

1. Confirm receipt of multiple emails from the attack
2. Verify link invalidity to rule out further compromise
3. Document the DoS impact for reporting

## Instructions

### Step 1: Monitor Email Inbox

**Context**: Check for incoming messages triggered by the concurrent requests.

Refresh the target email inbox (e.g., Gmail or similar).

> Expected output: 30 emails arrive titled 'Finish signing up for Khan Academy' from Khan Academy.

### Step 2: Test Email Links

**Context**: Validate that the confirmation links are non-functional.

Click links in several emails and observe the response.

> Expected output: Browser shows errors like 'Invalid or expired token' on the Khan Academy site.

### Step 3: Compare Normal Behavior

**Context**: Replicate without race to confirm bypass.

Attempt to add the same email normally without Turbo Intruder.

> Expected output: Warning message for already linked email, single send only.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- impact-verification
- email-dos
