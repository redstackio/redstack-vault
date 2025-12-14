---
id: 12146de8-8614-4831-bb78-693c4db4b00a
name: Grant-Access-and-Preserve-OAuth-Token
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.347Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - csrf
  - oauth
  - token-preservation
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Grant-Access-and-Preserve-OAuth-Token

## Summary

This procedure authorizes the Gratipay app in Bitbucket while interrupting the callback to keep the oauth_token valid for reuse in a CSRF attack.

## Description

Following token generation, the attacker grants permission but prevents the standard OAuth callback to Gratipay, ensuring the token isn't consumed. This exploits the flow's design, allowing token replay against victims.

## Requirements

1. Valid oauth_token from previous step
2. Logged-in Bitbucket session
3. Ability to interrupt browser redirects (e.g., dev tools or manual stop)

## Defense

Defensive measures and detection strategies:

- Invalidate tokens after single use or on callback failure
- Log and alert on interrupted OAuth flows
- Enforce short token lifetimes

## Objectives

1. Authorize the application without completing the flow
2. Preserve the token's validity
3. Enable token reuse for victim targeting

## Instructions

### Step 1: Grant Permission

**Context**: Authorize Gratipay access in Bitbucket.

Click 'Allow' or 'Grant Access' on the Bitbucket permission screen.

> This step simulates legitimate consent but sets up for interruption.

### Step 2: Interrupt Callback

**Context**: Prevent redirection to preserve the token.

As the browser attempts to redirect to Gratipay's callback (e.g., /auth/login/bitbucket:bitbucket.com/?oauth_token=...), stop the load (e.g., Esc key, close tab, or block in dev tools).

> Expected output: Token remains in history or notes; no invalidation occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[oauth]]
- [[token-preservation]]
