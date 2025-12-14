---
tags:
  - account-takeover
  - merge
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6ab60d3b-75f3-4b36-9514-81ef47def14a
created_at: '2025-12-14T17:30:58.580Z'
updated_at: '2025-12-14T17:30:58.580Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Merge-Accounts-and-Achieve-Takeover

## Summary

This procedure finalizes the account takeover by merging the attacker's development store with the victim's legacy account, granting full access to store admin and partner dashboard.

## Description

After bypassing confirmation, the attacker reviews accounts, sets up Shopify ID, and completes the merge process. This exploits legacy non-SSO accounts without 2FA, leading to privilege escalation. The outcome is unauthorized control over victim resources.

## Requirements

1. Email verification completed from prior procedure
2. Knowledge of victim's store password (may require separate recon)
3. Active session post-confirmation

## Defense

Defensive measures and detection strategies:

- Disable legacy account merges or require admin approval
- Monitor partner dashboard for unusual ID setups
- Enforce 2FA and SSO migration for all accounts

## Objectives

1. Initiate and complete account review and merge
2. Set up credentials for merged access
3. Gain persistent control over victim's assets

## Instructions

### Step 1: Review Accounts

**Context**: Access the merge interface.

No specific command; navigation:

- Click 'Review accounts' in account settings.

> Lists eligible legacy accounts for merge.

### Step 2: Enter Password and Set Up Shopify ID

**Context**: Authenticate to proceed with merge.

No specific command; form input:

- Enter store password to access Shopify ID.
- Click 'Set up Shopify ID' and follow prompts.

> Unlocks merge process.

### Step 3: Complete Merge and Access

**Context**: Finalize and verify takeover.

No specific command; completion:

- Click 'Continue', set up password, and log in to victim's store/partner account.

> Full access achieved.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[merge]]
