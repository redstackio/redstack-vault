---
tags:
  - discovery
  - shopify
  - template-editor
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:08:54.970Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 62811628-92fd-4594-b624-5125b2319471
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Navigate-to-Packing-Slip-Template-Editor

## Summary

This procedure locates and accesses the Packing Slip Template editor within the Shopify admin dashboard, identifying the entry point for HTML injection attacks.

## Description

Following authentication, this step involves navigating the admin interface to the specific feature vulnerable to HTML sanitization bypass. The editor allows custom HTML input for packing slips, which is processed by a PDF generator susceptible to injected iframes. This reconnaissance-like step confirms access to the target functionality in a Shopify environment.

## Requirements

1. Active Shopify admin session
2. Web browser with the dashboard loaded
3. Knowledge of the admin menu structure

## Defense

Defensive measures and detection strategies:

- Restrict template editing to privileged roles only
- Log access to admin settings pages
- Audit changes to template configurations

## Objectives

1. Reach the Packing Slip Template editor
2. Confirm editable HTML fields are present
3. Set up for payload injection

## Instructions

### Step 1: Access Settings Menu

**Context**: From the dashboard, enter the settings area to find shipping-related features.

No command required; click 'Settings' in the left sidebar, then select 'Shipping and delivery'.

> This opens shipping configuration. Expected output: List of shipping options including templates.

### Step 2: Open Template Editor

**Context**: Directly access the vulnerable editor URL or via menu.

No command required; click 'Packing slip template' or navigate to https://[store].myshopify.com/admin/settings/packing_slip_template.

> Editor loads with HTML input area. Expected output: Template preview and edit interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Discovery]]
- [[shopify]]
- [[template-editor]]
