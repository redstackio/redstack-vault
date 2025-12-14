---
tags:
  - rate-limit-exhaustion
  - dos
  - 2fa
  - shopify
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T12:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:30:27.376Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 57df9eb1-79df-46b3-b7fc-0e4bfde37fe0
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Exhaust 2FA OTP Rate Limits via Resend Spam

## Summary

This procedure triggers 2FA verification on the tampered setup and repeatedly requests OTP resends to exhaust Shopify's per-phone rate limits, preventing legitimate delivery for 24 hours.

## Description

After tampering, log out and re-login to invoke 2FA, then spam the 'Resend Code' button. Shopify's rate limiting ties to the phone number, not session, so spam burns the quota (typically ~50-100 requests per 24 hours). This causes DoS for the victim attempting login, as no new OTPs can be sent.

## Requirements

1. Tampered 2FA setup completed
2. Access to the account login page
3. Victim's phone now linked to session

## Defense

Defensive measures and detection strategies:

- Tie rate limits to session/IP in addition to phone
- Implement exponential backoff on resends
- Alert on high-volume resend attempts from single sessions
- Require CAPTCHA after multiple resends

## Objectives

1. Trigger OTP send to victim's phone
2. Exhaust daily SMS quota via spam
3. Block victim's future OTP receipts

## Instructions

### Step 1: Trigger 2FA Verification

**Context**: Initiate login to activate 2FA prompt.

No command; UI action:

- Log out of the account
- Log back in with credentials
- Entered to 2FA code entry page

> Expected: Prompt for OTP; initial code sent to victim's phone (ignore).

### Step 2: Spam Resend Code Requests

**Context**: Rapidly request new codes to hit rate limits.

No command; manual or scripted UI spam:

- Click 'Resend Code' button 20-50 times quickly
- Continue until server stops responding or shows rate limit error

> Expected: Initial resends work, then errors like 'Too many requests'; no further OTPs sent.

### Step 3: Cease and Confirm Exhaustion

**Context**: Stop after exhaustion to avoid detection.

Observe server response:

- Stop clicking after no response
- Attempt one more resend to verify block

> Expected: Persistent throttling for 24 hours.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rate-limit-exhaustion
- dos
