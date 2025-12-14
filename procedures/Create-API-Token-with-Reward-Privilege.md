---
tags:
  - api-token
  - reward-privilege
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
updated_at: '2025-12-14T17:24:47.792Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4026062f-dfcd-4e4b-9f5e-e03760420d8a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create API Token with Reward Privilege

## Summary

This procedure generates an API token in HackerOne with the 'reward' scope, enabling programmatic bounty issuance as part of testing 2FA enforcement gaps.

## Description

HackerOne's API allows token-based authentication for various actions, including rewarding reports. By creating a token with reward privileges, attackers can issue bounties without direct UI interaction, facilitating the bypass scenario. This requires a logged-in session and awareness of API scopes. The token acts as a valid credential for subsequent API calls.

## Requirements

1. Active HackerOne session
2. Knowledge of API scopes (specifically 'reward')
3. Secure storage for the generated token

## Defense

Defensive measures and detection strategies:

- Limit API token scopes to least privilege
- Require 2FA for token generation
- Log and review all token creations and usages

## Objectives

1. Obtain credential for reward actions
2. Enable API-driven bounty issuance
3. Prepare for dummy account rewarding

## Instructions

### Step 1: Navigate to Account Settings

**Context**: Access the API management section to create a new token.

Log in to HackerOne, go to your profile settings, and select 'API Tokens' or similar under integrations.

### Step 2: Generate Token with Reward Scope

**Context**: Specify the necessary privileges during token creation.

Enter a name for the token (e.g., 'Test Reward Token'), select the 'reward' scope from available options, and generate it. Copy the token value immediately, as it may not be retrievable later.

**Expected Output**: Token string provided; verify by making a test API call if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-token]]
- [[reward-privilege]]
