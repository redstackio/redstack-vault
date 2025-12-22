---
tags:
  - account-merger
  - takeover
  - shopify
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9c92df7a-8369-43fd-a72e-b5c38f226997
created_at: '2025-12-13T09:01:26.786Z'
updated_at: '2025-12-13T09:01:26.786Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Confirm Shopify Account Merger

## Summary

This procedure finalizes the account merger in Shopify, granting the attacker full access to the victim's merchant store.

## Description

After setting the new password, confirm the merger to combine accounts. This results in complete takeover, allowing control over the victim's store. Targets SSO-enabled accounts.

## Requirements

1. Password change completed
2. Confirmation page access

## Defense

Defensive measures and detection strategies:

- Require multi-factor confirmation for mergers
- Monitor and audit account merging events

## Objectives

1. Complete account merger
2. Achieve full takeover

## Instructions

### Step 1: Click Confirm

**Context**: Finalize the merger.

Click the confirm button on the page.

> Merges accounts and provides access.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[account-merger]]
- [[takeover]]
- [[shopify]]
