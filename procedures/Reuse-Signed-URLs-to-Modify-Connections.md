---
id: uuid-placeholder-6
tags:
  - shopify
  - authorization-bypass
  - signed-url-reuse
  - third-party-access
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.356Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reuse-Signed-URLs-to-Modify-Connections

## Summary

This procedure exploits the vulnerability by reusing saved signed URLs to modify third-party connections post-revocation, allowing unauthorized workflow integrations and data access.

## Description

The signed URLs, lacking expiration or unique validation, permit actions like connecting personal accounts to store workflows, potentially exposing customer data through services like Google Sheets.

## Requirements

1. Saved signed URLs from prior steps.
2. Revoked staff scenario.
3. Browser access.

## Defense

Defensive measures and detection strategies:

- Enforce URL expiration (e.g., 15 minutes) and per-user HMACs.
- Implement permission checks on every connector action, logging anomalies.

## Objectives

1. Bypass revocation for unauthorized modifications.
2. Integrate third-party accounts to workflows.
3. Achieve data access or manipulation.

## Instructions

### Step 1: Open Saved URL

**Context**: Access without auth.

Paste a saved URL, e.g., https://flow-connectors.shopifycloud.com/gsheet/connect?shop_id=24615823&path_hmac=%2BPnVhhFIC49KrHZGqwC08LoSMSkieG7UHWgtnriV2vQ%3D, into browser.

### Step 2: Modify Connection

**Context**: Perform unauthorized action.

Click to connect or disconnect a service, e.g., link a personal Google account.

> Expected output: Changes saved, no permission error.

### Step 3: Verify Impact

**Context**: Confirm access.

Check Flow workflows to see integrated account; attempt data pull if applicable.

> Expected output: Unauthorized connection active, potential data exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authorization-bypass]]
- [[signed-url-reuse]]
