---
tags:
  - dummy-account
  - bounty-reward
  - 2fa-bypass
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
updated_at: '2025-12-14T17:24:47.777Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e37b3223-dd41-48fb-8f5f-91b29b02d143
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reward Dummy Account Without 2FA

## Summary

This procedure uses an API token to issue a bounty reward to a HackerOne account lacking 2FA, exploiting the lack of enforcement in the rewarding process.

## Description

By leveraging the created API token, this step rewards a dummy account (configured without 2FA) for a test report. This sets up the vulnerability demonstration, as the reward is processed without checking the recipient's 2FA status, unlike submission requirements. The dummy account must exist and be associated with a valid report in the program.

## Requirements

1. API token with 'reward' scope
2. Dummy HackerOne account without 2FA
3. A test vulnerability report in the program

## Defense

Defensive measures and detection strategies:

- Validate recipient 2FA status during reward issuance
- Require program approval for all rewards
- Monitor API calls for anomalous rewarding patterns

## Objectives

1. Issue bounty to non-2FA account
2. Confirm reward processing succeeds
3. Enable claim bypass testing

## Instructions

### Step 1: Prepare Dummy Account and Report

**Context**: Ensure the target account and report are ready for rewarding.

Create or select a dummy account without 2FA enabled. Submit a dummy report to the program if needed to have a rewardable item.

### Step 2: Execute Reward via API

**Context**: Use the token to send the reward request.

Make a POST request to the HackerOne API endpoint `/api/v1/reports/{report_id}/rewards`, authenticating with `Authorization: Token token={your_token}`, and include payload specifying the dummy account as recipient and bounty amount.

**Expected Output**: API response confirms reward creation; check dummy account dashboard for pending reward.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dummy-account]]
- [[bounty-reward]]
