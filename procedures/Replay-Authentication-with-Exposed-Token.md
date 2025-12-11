---
tags:
  - replay-attack
  - credential-exposure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c308f6a1-e663-4850-8005-7ca2ce3ecf58
created_at: '2025-12-11T03:47:56.754Z'
updated_at: '2025-12-11T03:47:56.754Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1550]]'
---
# Replay Authentication with Exposed Token

## Summary

This procedure uses the exposed token to complete the security challenge, replay the authentication request, and expose the victim's credentials.

## Description

By sending a POST request with the stolen token, the attacker bypasses the CAPTCHA and retrieves the email and plain text password.

## Requirements

1. Extracted token from previous steps.

2. Knowledge of the security challenge endpoint.

3. Ability to forge POST requests.

## Defense

Defensive measures and detection strategies:

- Implement one-time-use tokens or nonce values.

- Monitor for replayed requests via timestamps or IP checks.

## Objectives

1. Complete CAPTCHA using token.

2. Expose victim's email and password.

3. Achieve unauthorized access.

## Instructions

### Step 1: Prepare Replay Request

**Context**: Construct the POST request with exposed token.

No specific command; use tools like browser console or scripts.

> Expected: Request mimics victim's authentication.

### Step 2: Send Replay Request

**Context**: Execute the replay to solve CAPTCHA.

```bash
curl -X POST https://paypal-security-endpoint -d 'token=exposed_token&auth_data=victim_params'
```

> Expected: Response contains email and plain text password.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #replay-attack
- #credential-exposure
