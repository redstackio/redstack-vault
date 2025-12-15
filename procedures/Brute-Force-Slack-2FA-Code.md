---
id: proc-slack-2fa-bruteforce-001
tags:
  - brute-force
  - 2fa-bypass
  - slack
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:31:42.676Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-Slack-2FA-Code

## Summary

This procedure exploits the absence of rate limiting by manually attempting multiple incorrect 6-digit 2FA codes on the Slack password reset page, eventually succeeding in resetting the password for account takeover.

## Description

With the reset page loaded, the attacker enters random or sequential 6-digit codes (000000 to 999999) repeatedly. Testing showed up to 20+ manual attempts without lockout, confirming brute-force viability (1 in 1,000,000 chance per attempt, but feasible offline or with email access). Outcomes include password change and full control; manual to avoid automation bans in bug bounties.

## Requirements

1. Access to the loaded password reset page.
2. Knowledge of target's 2FA setup (time-based 6-digit).
3. Patience for manual entry; optionally, victim's authenticator for code if available.

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 attempts per 10 minutes) on 2FA inputs.
- Introduce progressive delays or CAPTCHAs after failures.
- Log and alert on excessive failed 2FA attempts during resets.

## Objectives

1. Bypass 2FA via unlimited guesses.
2. Complete password reset.
3. Achieve persistent account access.

## Instructions

### Step 1: Prepare for Entry

**Context**: Locate the 2FA field on the reset page.

On the loaded reset page, fill in a desired new password but leave the 2FA field empty initially. Note the 6-digit format.

> The form validates code length but not attempts.

### Step 2: Perform Manual Brute-Force Attempts

**Context**: Test incorrect codes repeatedly.

Enter incorrect codes like 000000, 000001, up to 20 times, submitting each. Observe no lockout; continue until correct (or guess based on time). Then submit with new password.

> Each failed submit shows an error like "Invalid code" without restrictions; success prompts password confirmation.

### Step 3: Verify Takeover

**Context**: Confirm control post-reset.

After successful reset, log in with the new password at slack.com to access the account.

> Dashboard loads with victim's workspaces and data.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[brute-force]]
- [[2fa-bypass]]
- [[slack]]
- [[credential-access]]
