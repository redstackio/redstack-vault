---
id: proc-uuid-4
name: Send Modified Reset Request
tags:
  - request-modification
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.288Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Send Modified Reset Request

## Summary

This procedure forwards the token-swapped request to Remitly's endpoint, resetting the victim's password using the attacker's OTP due to validation flaws.

## Description

The modified POST to /orchestrator/v1/password_reset/start bypasses checks, applying the reset to the victim's account. There are two endpoints with the same name; target the one leaking JWT. Success grants the attacker control without further auth.

## Requirements

1. Fully prepared request with swapped tokens and OTP
2. Proxy interception

## Defense

Defensive measures and detection strategies:

- Validate all session params against the authenticated user
- Separate endpoints clearly and deprecate leaky ones
- Audit reset logs for cross-account anomalies

## Objectives

1. Execute reset on victim account
2. Confirm success without errors
3. Prepare for immediate login

## Instructions

### Step 1: Verify Modification

**Context**: Double-check payload in proxy.

Ensure AMP_d0cf3ed24c, JWT, and OTP are correctly set.

> Use Burp's inspector for validation.

### Step 2: Forward Request

**Context**: Send to server.

Click 'Forward' in Burp Suite.

> Target: POST /orchestrator/v1/password_reset/start

### Step 3: Check Response

**Context**: Validate reset completion.

Inspect response for success indicators.

> Look for confirmation message; no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-modification]]
- [[auth-bypass]]
