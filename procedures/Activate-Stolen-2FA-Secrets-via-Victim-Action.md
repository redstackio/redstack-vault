---
id: proc-uuid-3
tags:
  - 2fa-bypass
  - account-takeover
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.591Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Activate-Stolen-2FA-Secrets-via-Victim-Action

## Summary

This procedure leverages stolen pre-generated 2FA secrets by waiting for or inducing the victim to confirm/enable 2FA on HackerOne, activating the codes for attacker use.

## Description

After theft, the secrets remain valid until the victim interacts with the authentication page to enable or regenerate 2FA. The attacker monitors or uses phishing to prompt this action, allowing unauthorized access post-activation without needing the victim's current credentials or TOTP.

## Requirements

1. Previously stolen 2FA secrets/backup codes
2. Victim's continued engagement with HackerOne
3. Optional: Social engineering capabilities

## Defense

Defensive measures and detection strategies:

- Force secret regeneration on confirmation only, with immediate invalidation of pre-generated values
- Log and alert on 2FA enablement events
- Educate users on phishing risks around auth changes

## Objectives

1. Induce victim to activate 2FA using stolen secrets
2. Gain persistent access to the account
3. Bypass 2FA entirely for future logins

## Instructions

### Step 1: Monitor Victim Behavior

**Context**: Observe if victim naturally visits the auth page due to suspicion or routine.

No command; use session tracking or follow-up phishing.

> Expected: Victim reloads or confirms the page, activating codes.

### Step 2: Test Access

**Context**: Once activated, attempt login with stolen codes.

Navigate to HackerOne login and use the backup code or TOTP secret.

> Expected: Successful authentication as the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[2fa-bypass]]
