---
tags:
  - shopify
  - secret-extraction
  - multipass
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Cloud Instance Metadata API]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3342e425-a729-441c-be1b-bd5e0b92a06e
created_at: '2025-12-14T17:29:57.112Z'
updated_at: '2025-12-14T17:29:57.112Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
---
# Extract-Multipass-Secret

## Summary

Read and capture the Multipass secret from Shopify settings, enabling potential customer account takeovers.

## Description

The secret, once visible post-enablement, allows crafting Multipass tokens for impersonating any customer, per Shopify docs. This exploits the permission gap. Target: Admin UI; outcome: Secret obtained for misuse.

## Requirements

1. Multipass enabled
2. Active staff session
3. Means to copy/store the secret securely

## Defense

Defensive measures and detection strategies:

- Hide secrets behind additional auth (e.g., 2FA view)
- Monitor secret views and exports
- Implement secret rotation on access

## Objectives

1. View the secret key
2. Copy for external use
3. Escalate to customer data access

## Instructions

### Step 1: Locate Secret Field

**Context**: Identify the displayed key after enablement.

Refresh or check Multipass section.

### Step 2: Copy Secret

**Context**: Extract without further permissions.

Select and copy the alphanumeric secret.

> Expected output: Secret in clipboard, e.g., a 32-char string.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Cloud Instance Metadata API]] Unsecured Credentials: Cloud Services

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[shopify]]
- [[secret-read]]
- [[credential-access]]
