---
tags:
  - bounty-claim
  - 2fa-bypass
  - auth-bypass
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.773Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 703dc1b7-6ada-4ff0-972a-15f95cdbd78b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Claim Bounty Using Dummy Account

## Summary

This procedure logs into a dummy account without 2FA to claim a rewarded bounty, proving the business logic flaw where program 2FA requirements are not enforced.

## Description

After rewarding the dummy account, this step involves standard login and claim actions on the HackerOne platform. The key vulnerability is that the claiming interface does not prompt for or validate 2FA, despite the program's settings, allowing direct access to financial payouts. This impacts program security by enabling unauthorized reward claims.

## Requirements

1. Dummy account with pending bounty
2. Valid username/password for dummy account
3. No 2FA configured on the account

## Defense

Defensive measures and detection strategies:

- Enforce 2FA uniformly for all financial actions
- Implement claim approval workflows
- Detect claims from low-security accounts via logging

## Objectives

1. Access bounty without multi-factor auth
2. Complete payout process
3. Validate unauthorized access impact

## Instructions

### Step 1: Log In to Dummy Account

**Context**: Authenticate using only basic credentials.

Visit hackerone.com, enter the dummy account's username and password, and submit without 2FA (which isn't enabled).

### Step 2: Navigate and Claim Reward

**Context**: Proceed to the rewards section to finalize the claim.

Go to the dashboard, locate the pending bounty under reports or rewards, and click to claim or initiate payout. The process completes without additional auth prompts.

**Expected Output**: Bounty claimed; payout details updated in account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bounty-claim]]
- [[2fa-bypass]]
