---
id: proc-install-stocky-001
tags:
  - installation
  - shopify-app
  - stocky
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.729Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Stocky-App-on-Stores

## Summary

This procedure installs the Stocky inventory management app on two Shopify test stores, preparing the environment for accessing the vulnerable low stock variants feature.

## Description

The Stocky app, integrated via Shopify's App Store, provides inventory tracking including low stock alerts. Installation on multiple stores exposes the IDOR-vulnerable endpoint /settings_for_low_stock_variants/{ID}, where {ID} is a numeric identifier lacking ownership checks. This step ensures both attacker and victim stores have the app deployed identically.

## Requirements

1. Active Shopify stores
2. Admin access to each store
3. Internet access to Shopify App Store

## Defense

Defensive measures and detection strategies:

- Review app installation logs for suspicious patterns
- Use Shopify's app review process to vet permissions

## Objectives

1. Deploy Stocky on attacker store
2. Deploy Stocky on victim store
3. Verify app functionality

## Instructions

### Step 1: Install on Attacker Store

**Context**: Add the app to User A's store.

From test.myshopify.com admin, go to Apps > Search 'Stocky' > Install.

> Expected output: App listed in installed apps, redirect to https://app.stockyhq.com/dashboard/.

### Step 2: Install on Victim Store

**Context**: Mirror installation on User B's store.

Repeat the process for test1.myshopify.com.

> Expected output: Identical app access for User B.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[installation]]
- [[shopify-app]]
