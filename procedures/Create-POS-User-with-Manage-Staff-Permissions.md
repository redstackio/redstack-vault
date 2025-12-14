---
tags:
  - privilege-escalation
  - shopify
  - pos-permissions
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.049Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bb15a403-3eaa-44ac-a0ad-d9ea1037d9b0
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create POS User with Manage Staff Permissions

## Summary

This procedure sets up a POS-specific staff role restricted to 'Manage Staff' permissions, creating the low-privilege entry point for UI-based escalation in Shopify's retail settings.

## Description

Targeting the retail permission subset in Shopify, this step limits a staff account to POS staff management only, simulating an insider or compromised limited user. It exploits the separation between admin and POS permissions, allowing later navigation bypass. Prerequisites include admin access; outcomes enable session switching without full creds.

## Requirements

1. Shopify admin access with permission to manage staff
2. POS application enabled in the store
3. Web browser for admin navigation

## Defense

Defensive measures and detection strategies:

- Enforce least-privilege principles for POS roles
- Log and alert on permission changes in retail settings
- Regularly audit staff roles for over-privileging

## Objectives

1. Isolate POS access to minimal permissions
2. Assign a PIN for POS authentication
3. Prepare user for limited session in POS app

## Instructions

### Step 1: Navigate to Staff Permissions

**Context**: Reach the retail-specific settings.

In Shopify admin, go to Settings > Users and permissions > Staff. Select or add a new staff account.

> This opens the permission editor with admin and retail tabs.

### Step 2: Configure Limited Role

**Context**: Restrict to POS staff management.

Switch to the 'Retail' tab. Check only 'Manage staff' under POS permissions. Uncheck all other options. Set a POS PIN (e.g., a test value) and save the changes.

> Confirmation appears, and the role is updated to limited scope.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[pos-permissions]]
