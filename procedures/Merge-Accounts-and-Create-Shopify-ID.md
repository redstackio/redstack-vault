---
id: 849f55eb-a7a0-45b9-9435-f25ce12f9376
name: Merge Accounts and Create Shopify ID
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:40.640Z'
updated_at: '2025-12-11T06:10:40.640Z'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - shopify
  - account-merge
commands:
  - '[[commands/update-organization-email]]'
  - '[[commands/update-user-email]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Browser-Dev-Tools]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1078]]'
---

# Merge Accounts and Create Shopify ID

## Summary

This procedure refreshes the profile to trigger account merging and creates a Shopify ID, completing the takeover of the victim's account.

## Description

Following staff email update, refreshing the profile prompts an account merge without email validation, allowing the attacker to create a verified Shopify ID and gain control. This targets Shopify's account system in a web environment.

## Requirements

1. Staff email updated to victim's
2. Access to shop profile page
3. Control over merged account

## Defense

Defensive measures and detection strategies:

- Enforce email validation during account merges
- Monitor for unauthorized merge attempts

## Objectives

1. Merge accounts without validation
2. Create verified Shopify ID
3. Achieve full account takeover

## Instructions

### Step 1: Refresh Profile

**Context**: Trigger the merge prompt.

Refresh the shop profile page to initiate the account combine prompt.

> This merges the accounts without validating the new email.

### Step 2: Create Shopify ID

**Context**: Finalize the ID creation.

Proceed with Shopify ID creation for the merged accounts.

> This grants access to the victim's shop.

### Step 3: Optional Email Change

**Context**: Secure the taken-over account.

Optionally change the email to the attacker's controlled address.

> Ensures persistent access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- account-merge
