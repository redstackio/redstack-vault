---
id: proc-romit-initiate-send-001
name: Initiate-Send-Money-to-Trigger-PIN-Verification
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.234Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - trigger-verification
  - api-endpoint
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
commands:
  - '[[commands/curl-trigger-login]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Initiate-Send-Money-to-Trigger-PIN-Verification

## Summary

This procedure uses the Romit app's 'Send Money' feature to input a victim's phone number, triggering the /v0/cash/auth/login endpoint and initiating PIN verification without rate limits, setting up the brute-force opportunity.

## Description

The Romit app's send money functionality exposes the login process to external phone numbers, invoking the vulnerable endpoint. This step requires an attacker account and targets the web API, leading to a PIN challenge that can be brute-forced. Prerequisites include API credentials from prior setup; outcome is an active verification session exploitable for guessing.

## Requirements

1. Attacker account with API credentials
2. Victim's phone number in international format (e.g., +1XXXXXXXXXX)
3. Access to app.romit.io or API proxy like [[tools/Burp-Suite]]

## Defense

Defensive measures and detection strategies:

- Rate-limit send money initiations per IP/account
- Require 2FA for initiating transfers to unknown numbers
- Log phone number inputs for anomaly detection (e.g., high-volume tests)

## Objectives

1. Invoke /v0/cash/auth/login for victim phone
2. Expose PIN verification without protections
3. Prepare for brute-force payload injection

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate as attacker and access send money UI.

Log in to app.romit.io using attacker credentials.

> Navigates to dashboard; no command needed.

### Step 2: Input Victim Phone and Trigger

**Context**: Enter victim details to hit the login endpoint.

Execute [[commands/curl-trigger-login]] to simulate or directly call:

```bash
curl -X POST https://api.romit.io/v0/cash/auth/login \
  -H "Content-Type: application/json" \
  -d '{"phone":"+1VICTIM_PHONE"}'
```

> Expected output: JSON response with PIN challenge status, e.g., {"status":"pending_pin"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-login]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[trigger-verification]]
- [[api-endpoint]]
