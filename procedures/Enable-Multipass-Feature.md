---
tags:
  - shopify
  - multipass
  - enable-feature
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
  - '[[Cloud Instance Metadata API]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4c8983ce-6408-454e-8753-55f0b3c92a44
created_at: '2025-12-14T17:29:57.117Z'
updated_at: '2025-12-14T17:29:57.117Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Cloud Instance Metadata API]]'
---
# Enable-Multipass-Feature

## Summary

Activate the Multipass feature in Shopify checkout settings, which exposes the secret key to users with 'Settings' access.

## Description

Multipass allows SSO-like logins for customers; enabling it generates a secret used for token creation. This procedure highlights the flaw where 'Settings' permission suffices, despite the secret's power. Outcome: Feature on, secret available.

## Requirements

1. Checkout settings access
2. Account requirements configured
3. Shopify Plus subscription

## Defense

Defensive measures and detection strategies:

- Restrict Multipass to 'Customers' or owner-only permissions
- Log Multipass enable/disable events
- Rotate secrets on enablement and audit access

## Objectives

1. Turn on Multipass
2. Expose the secret for reading
3. Demonstrate permission mismatch

## Instructions

### Step 1: Find Multipass Toggle

**Context**: Locate the feature in advanced settings.

In checkout, expand Multipass section.

### Step 2: Activate and Confirm

**Context**: Enable without verification issues.

Toggle to enabled and save.

> Expected output: Secret key generated and displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Cloud Instance Metadata API]] Unsecured Credentials: Cloud Services

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[shopify]]
- [[multipass]]
- [[feature-enable]]
