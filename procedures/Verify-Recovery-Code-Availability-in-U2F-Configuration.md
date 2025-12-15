---
id: proc-003
tags:
  - 2fa
  - u2f
  - comparison
  - business-logic
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:47.478Z'
skill_level: beginner
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-Recovery-Code-Availability-in-U2F-Configuration

## Summary

This procedure compares recovery code access in a U2F-enabled 2FA setup against TOTP-only to confirm implementation inconsistencies, exposing business logic errors that risk permanent account lockouts.

## Description

In assessing 2FA parity across methods in web apps like Legal Robot, this step uses a secondary test account with U2F (hardware key) enabled to check for recovery codes and TOTP fallbacks. By contrasting with the TOTP-only account, the tester verifies that U2F users have superior recovery options, indicating an oversight in the rollout. This confirms the vulnerability's scope and impact on user experience.

## Requirements

1. Second test account with U2F hardware key
2. Access to 2FA settings on both account types
3. Documentation tool for screenshots/comparisons

## Defense

Defensive measures and detection strategies:

- Standardize recovery features across all 2FA methods in development
- Review configuration parity in code audits and QA testing
- Track 2FA method adoption rates to identify under-supported options

## Objectives

1. Enable U2F and inspect recovery features
2. Compare availability with TOTP-only setup
3. Validate the business logic disparity

## Instructions

### Step 1: Set Up U2F Account

**Context**: Create or configure a new account with U2F as the primary or additional 2FA method.

No command; register the hardware key via the UI prompt.

> Expected: U2F successfully registered, possibly with TOTP fallback option.

### Step 2: Access Recovery in U2F Settings

**Context**: Navigate to 2FA settings and look for recovery code generation.

No command; interact with the interface to generate/view codes.

> Expected: Recovery codes provided, along with any TOTP fallback mentions.

### Step 3: Document Comparison

**Context**: Note differences between U2F and TOTP accounts, such as presence of links or features.

No command; take screenshots or log observations.

> Expected: Clear evidence of missing features in TOTP-only, confirming the flaw.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[u2f]]
- [[business-logic]]
