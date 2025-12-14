---
tags:
  - shopify
  - checkout-config
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3e1152a5-2280-4b06-bbcc-ffc42412e6c9
created_at: '2025-12-14T17:29:57.121Z'
updated_at: '2025-12-14T17:29:57.121Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Configure-Account-Requirements-in-Checkout

## Summary

Adjust the customer account options in Shopify checkout settings to enable paths for Multipass activation.

## Description

This step modifies the 'Accounts are required or optional' setting in checkout, a basic configuration under 'Settings' permission. It prepares the environment for Multipass without triggering higher privileges. Expected: Setting updated successfully.

## Requirements

1. Active session in checkout settings
2. 'Settings' permission confirmed
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Audit changes to checkout configurations
- Require elevated permissions for account-related settings
- Monitor for frequent config tweaks by staff

## Objectives

1. Enable optional account flows
2. Avoid permission denials
3. Stage for feature enablement

## Instructions

### Step 1: Locate Account Section

**Context**: Find the relevant option in settings.

Scroll to customer accounts in checkout page.

### Step 2: Select and Save

**Context**: Apply the configuration change.

Choose 'Accounts are required or optional' and save.

> Expected output: Confirmation toast or updated UI reflecting change.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[shopify]]
- [[account-config]]
- [[checkout]]
