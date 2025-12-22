---
id: proc-assign-collection-override
tags:
  - xss
  - shopify
  - tax-override
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.829Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Assign-Malicious-Collection-to-Tax-Override

## Summary

This procedure assigns a collection containing an XSS payload to a 'Rest of World' tax override in Shopify's admin, setting up the payload for reflection during UI interactions like deletion.

## Description

Shopify's tax settings allow assigning collections to geographic overrides without validating referenced object names. By selecting the malicious collection, the payload becomes part of the override configuration, visible in the UI. This creates a reflection point exploitable in actions like deletion, where the name is reprocessed without escaping. Requires admin access; impacts admin session security.

## Requirements

1. Existing malicious collection from prior procedure
2. Admin access to Settings > Taxes
3. Configured store with tax features enabled

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected data in admin UI components
- Log override assignments and scan for suspicious collection names
- Use output encoding (e.g., HTML entity encoding) for dynamic content

## Objectives

1. Link payload-laden collection to tax override
2. Ensure payload visibility in override details
3. Position for execution in delete flow

## Instructions

### Step 1: Navigate to Tax Settings

**Context**: Access the tax overrides interface.

In admin dashboard, go to Settings > Taxes and duties > Tax overrides.

### Step 2: Add Override

**Context**: Create a new override and select the malicious collection.

Click 'Add tax override for Rest of World'. In the collection selector, choose the one named `<img src=x onerror=prompt(7)>`. Set a tax rate (e.g., 0%) and save.

> The payload name appears in the UI (e.g., addtax.png), confirming reflection.

### Step 3: Confirm Assignment

**Context**: Verify the override includes the payload.

View the overrides list; the 'Rest of World' entry should show the malicious collection name.

**Expected Output**: Override active with payload visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[tax-override]]
