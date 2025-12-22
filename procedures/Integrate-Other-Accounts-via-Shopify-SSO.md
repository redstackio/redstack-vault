---
tags:
  - shopify
  - sso-integration
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 7b4e640e-ec22-4159-a5ec-598b0464acf4
created_at: '2025-12-13T09:01:26.833Z'
updated_at: '2025-12-13T09:01:26.833Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Integrate Other Accounts via Shopify SSO

## Summary

This procedure integrates additional accounts linked to the confirmed email via Shopify SSO.

## Description

Leveraging the confirmed email, the attacker gains access to all associated shops.

## Requirements

1. Confirmed target email in account
2. Target has existing Shopify accounts

## Defense

Defensive measures and detection strategies:

- Require multi-factor authentication for SSO integrations
- Monitor for unexpected account linkages

## Objectives

1. Link associated stores
2. Escalate access scope

## Instructions

### Step 1: Select Integration

**Context**: Choose to integrate accounts.

In the profile, select to integrate other Shopify accounts associated with the confirmed email.

> Integration should list and connect the stores.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- sso-integration
