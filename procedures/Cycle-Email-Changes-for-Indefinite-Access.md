---
id: proc-email-cycle-indefinite
tags:
  - email-cycling
  - persistence
  - 2fa-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.483Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Cycle-Email-Changes-for-Indefinite-Access

## Summary

This procedure maintains the 2FA bypass indefinitely by repeatedly changing the email between the attacker's controlled address and the victim's, re-verifying trust each time to extend session life without full re-authentication.

## Description

The logic flaw allows email changes without session termination, so the attacker reverts to their email, re-verifies via OTP, and re-trusts the device to reset the 1-month timer. Then, they switch back to the victim's email. This cycle can be repeated, exploiting the lack of ownership checks or notifications. In the web platform, this ensures perpetual impersonation until a password reset intervenes.

## Requirements

1. Trusted session active
2. Control over initial email for OTPs
3. Repeated access to account details page

## Defense

Defensive measures and detection strategies:

- Limit email change frequency (e.g., cooldown periods)
- Require full 2FA and password confirmation for each change
- Detect and flag oscillating email updates from single sessions

## Objectives

1. Extend device trust beyond initial period
2. Retain impersonation without session expiry
3. Avoid detection through minimal footprint

## Instructions

### Step 1: Revert to Attacker Email

**Context**: Switch back to controlled email to enable re-verification.

In account details, update email to the original attacker address and submit.

### Step 2: Re-Verify and Trust Device

**Context**: Complete OTP to refresh trust.

Check email for new OTP, enter it, and select 'Trust this device for 1 month' again.

### Step 3: Switch Back to Victim

**Context**: Return to impersonation state.

Update email to victim's address once more; session persists without prompt.

**Expected Output**: Indefinite access confirmed by repeated logins sans 2FA.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-cycling]]
- [[Persistence]]
- [[2fa-bypass]]
