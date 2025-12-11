---
tags:
  - token-reuse
  - credential-exposure
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Man in the Browser]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 286f1798-186c-4c0f-9c08-cbe4aced56e4
created_at: '2025-12-11T06:10:40.522Z'
updated_at: '2025-12-11T06:10:40.522Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1185]]'
---
# Complete Challenge with Leaked Token to Expose Credentials

## Summary

This procedure uses the leaked token to complete the security challenge, replaying the victim's authentication to expose their email and plaintext password.

## Description

The attacker submits a POST request with the token to solve the CAPTCHA, triggering the replay of the queued authentication request and revealing credentials.

## Requirements

1. Leaked token from prior steps.
2. Knowledge of PayPal's challenge endpoint.
3. Ability to send HTTP requests.

## Defense

Defensive measures and detection strategies:

- Prevent token reuse with one-time tokens or session binding.
- Monitor for anomalous challenge completions.

## Objectives

1. Solve CAPTCHA using leaked token.
2. Replay authentication to expose credentials.
3. Achieve account compromise.

## Instructions

### Step 1: Prepare POST Request

**Context**: Craft request to submit the token.

Use a tool like curl or browser to POST to the challenge endpoint with the token.

```bash
curl -X POST https://paypal.challenge.endpoint -d 'token=leaked_token'
```

> This simulates solving the CAPTCHA.

### Step 2: Observe Credential Exposure

**Context**: Monitor for replayed authentication response.

Check the response or logs for exposed email and password.

> Successful replay reveals plaintext credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Man in the Browser]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[token-reuse]]
- [[credential-exposure]]
