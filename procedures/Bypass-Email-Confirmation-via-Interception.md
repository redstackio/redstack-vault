---
tags:
  - auth-bypass
  - email-swap
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1d2a79aa-75ee-47ad-9134-c1794938ce43
created_at: '2025-12-14T17:30:58.588Z'
updated_at: '2025-12-14T17:30:58.588Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Bypass-Email-Confirmation-via-Interception

## Summary

This procedure bypasses Shopify's email confirmation by toggling request modifications during the verification flow, allowing the attacker to confirm the victim's email on their own session.

## Description

By disabling interception to receive the confirmation link on the owned email, then re-enabling to swap during verification, the attacker claims ownership without victim interaction. This targets photo upload endpoints that trigger email-associated requests, exploiting legacy validation flaws.

## Requirements

1. Burp Suite rules configured from prior procedure
2. Owned email accessible for link receipt
3. Active session in Shopify admin

## Defense

Defensive measures and detection strategies:

- Require separate confirmation channels (e.g., SMS) for email changes
- Rate-limit and anomaly-detect upload requests tied to account changes
- Audit logs for mismatched IP/session during confirmations

## Objectives

1. Receive and activate confirmation without victim access
2. Associate victim's email with attacker's store
3. Complete verification on success page

## Instructions

### Step 1: Disable Rules and Change Back to Owned Email

**Context**: Allow normal flow to receive confirmation.

No specific command; configuration toggle:

- Uncheck Burp Match and Replace rules.
- Reload account page and set email to owned address.
- Submit to trigger email.

> Confirmation link arrives in owned inbox.

### Step 2: Re-Enable Rules for Swap During Confirmation

**Context**: Modify the verification request to victim's email.

No specific command; toggle and action:

- Re-check Burp rules to swap owned email back to victim's.
- Click the confirmation link in the logged-in browser.

> Request is intercepted and altered.

### Step 3: Trigger Final Modification with Upload

**Context**: Use upload to confirm the swapped state.

No specific command; interface:

- On verification success page, upload and save another photo.

> Endpoint processes with victim's email, finalizing bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]
- [[Modify Authentication Process]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[email-swap]]
