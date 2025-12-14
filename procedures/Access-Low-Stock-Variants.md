---
id: proc-access-variants-001
tags:
  - navigation
  - stocky
  - ui-access
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
updated_at: '2025-12-14T17:25:23.726Z'
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
# Access-Low-Stock-Variants

## Summary

This procedure navigates to the low stock variants section in the Stocky app, setting up for settings modification that triggers the vulnerable endpoint.

## Description

The low stock variants feature in Stocky displays inventory items below a threshold, with customizable column settings. Accessing this as the attacker prepares the legitimate request for interception, revealing the IDOR endpoint structure.

## Requirements

1. Stocky app installed and logged in
2. Valid session for the store

## Defense

Defensive measures and detection strategies:

- Log access to sensitive UI sections
- Session timeout enforcement

## Objectives

1. Load low stock variants page
2. Access column settings
3. Prepare for update action

## Instructions

### Step 1: Log In and Navigate

**Context**: Enter the app dashboard and select the feature.

Log in as User A at https://app.stockyhq.com/dashboard/, click 'Low Stock Variants'.

> Expected output: Page loads with variant list and settings link.

### Step 2: Enter Settings

**Context**: Go to configurable columns.

Click Settings > Columns.

> Expected output: Form with checkboxes for show_* options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
