---
tags:
  - privilege-escalation
  - shopify
  - ui-navigation
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
updated_at: '2025-12-14T17:29:10.039Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4b9b45f5-ad6c-458d-842f-1624443a197b
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Navigate to Edit Staff POS Access and Manage POS Roles

## Summary

This procedure uses the elevated POS session to edit a staff member's POS access, clicking into the 'Manage POS Roles' link to access the roles listing page.

## Description

With full permissions now active in POS, this step begins the UI chaining exploit by navigating to role management, where improper controls allow deeper admin access. It relies on the session escalation from prior steps.

## Requirements

1. POS session with full permissions active
2. At least one staff member configured for POS
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Validate permissions at each UI navigation depth
- Block cross-context links from POS to admin
- Monitor navigation patterns for anomalies

## Objectives

1. Enter staff edit mode in POS
2. Trigger roles management interface
3. Expose nested UI elements

## Instructions

### Step 1: Select Staff for Edit

**Context**: Start from staff overview.

In POS Staff section, choose any staff member and click Edit POS app access.

> Edit panel opens with access options.

### Step 2: Access Roles Link

**Context**: Proceed to management view.

Click the 'Manage POS Roles' button or link in the edit interface.

> Transitions to the full roles listing page.

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
- [[ui-navigation]]
