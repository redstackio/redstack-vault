---
tags:
  - csrf
  - shopify
  - pinterest
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:03.688Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6483e94e-0c0c-4fa7-b9f2-21e4d9ed6acd
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify Victim Pinterest Connection

## Summary

This procedure confirms an existing Pinterest integration on the victim's Shopify store, establishing the baseline for hijacking via CSRF.

## Description

In the context of exploiting CSRF in Shopify's Pinterest OAuth, the attacker first verifies the victim's setup to ensure there's an active connection to override. This is done manually through the Shopify admin interface, assuming reconnaissance or insider knowledge. The target environment is a web-based Shopify admin panel with Pinterest app enabled.

## Requirements

1. Access to victim's Shopify admin (via phishing or prior compromise) or reconnaissance tools to check integrations
2. Victim's store URL and login state
3. Basic web navigation knowledge

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication (MFA) on Shopify accounts to prevent unauthorized access
- Monitor integration changes via Shopify audit logs for unexpected account swaps

## Objectives

1. Confirm active Pinterest connection on victim's store
2. Identify the integration as hijackable
3. Set up for OAuth exploitation

## Instructions

### Step 1: Access Victim's Shopify Admin

**Context**: Log in or observe the victim's admin panel to check integrations.

No specific command; navigate to Apps > Installed Apps and look for Pinterest.

> Manual UI check: Verify 'Pinterest' shows as connected with account details.

### Step 2: Document Connection Status

**Context**: Note the current connected Pinterest account for later verification of hijack.

Screenshot or record the account ID/email linked.

> Expected: Active status confirmed, e.g., 'Connected to user@example.com'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[pinterest]]
