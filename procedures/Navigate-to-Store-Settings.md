---
tags:
  - auth-bypass
  - mobile
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:19.779Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: c20e9014-03ec-4bee-b04b-9b8b3ecfa275
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Navigate-to-Store-Settings

## Summary

This procedure navigates through the Shopify mobile app's menu to reach the Plan and Permissions section, accessing the Sell or Close feature without any authentication barriers.

## Description

The vulnerability stems from the mobile app's lack of verification for sensitive navigation paths. Unlike the web version, which prompts for passwords, the mobile app allows direct access to critical settings. An attacker can scroll to the 'Sell or Close' option at the bottom of the Plan and Permissions page, exploiting the app's design oversight.

## Requirements

1. Active session in the Shopify mobile app
2. Physical device access
3. Basic familiarity with mobile app interfaces

## Defense

Defensive measures and detection strategies:

- Require multi-factor authentication (MFA) or PIN for settings access in mobile apps
- Log all navigation to sensitive sections for anomaly detection
- Use app shielding to enforce runtime checks on privileged actions

## Objectives

1. Reach high-privilege settings without interruption
2. Identify exploitable options like store closure
3. Maintain stealth by avoiding alerts

## Instructions

### Step 1: Enter Settings Menu

**Context**: From the app dashboard, access the global settings to begin navigation.

Tap the profile or menu icon, then select 'Settings'.

> This loads the settings overview without prompts.

### Step 2: Access Plan and Permissions

**Context**: Drill down to the specific section containing sensitive actions.

Within Settings, tap 'Plan and Permissions', then scroll to the bottom to locate 'Sell or Close'.

> The section appears fully accessible, confirming the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[auth-bypass]]
- [[mobile]]
- [[shopify]]
