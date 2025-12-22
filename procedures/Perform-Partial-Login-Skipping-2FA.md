---
tags:
  - 2fa-bypass
  - partial-auth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.086Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: 8d7226a3-1473-4c04-af6b-e27a7ab6b34b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Partial-Login-Skipping-2FA

## Summary

This procedure logs in to CS.Money using Steam credentials while intentionally skipping the 2FA code entry, exploiting a flaw that allows partial session creation.

## Description

Central to the authentication bypass, this step leverages incomplete verification in Steam integration. Targeted at the web login flow, it requires Steam credentials post-reset. Success yields a session with limited but sufficient access for subdomain exploitation.

## Requirements

1. Steam credentials
2. Clean browser session
3. Enabled 2FA on the account

## Defense

Defensive measures and detection strategies:

- Mandate 2FA completion before granting any session tokens
- Alert on login attempts without 2FA verification

## Objectives

1. Create incomplete authenticated session
2. Bypass 2FA enforcement
3. Gain entry without full credentials

## Instructions

### Step 1: Initiate Steam Login

**Context**: Start the authentication process to trigger Steam redirect.

Visit https://cs.money and select Steam login, entering credentials.

> Steam authorizes and redirects back to CS.Money.

### Step 2: Skip 2FA Prompt

**Context**: When 2FA code is requested, proceed without entering it.

Ignore the 2FA input field and click continue or submit.

> The system fails to enforce, creating partial session.

### Step 3: Validate Partial Access

**Context**: Test if basic site functions are available without full auth.

Attempt to access non-restricted pages; no errors should block navigation.

> Partial access confirmed if dashboard loads minimally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[partial-auth]]
