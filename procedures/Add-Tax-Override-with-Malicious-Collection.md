---
tags:
  - xss
  - tax-override
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e7ddbad7-4ac6-4a4c-9d64-f3bbe54e538e
created_at: '2025-12-14T17:28:45.040Z'
updated_at: '2025-12-14T17:28:45.040Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Add-Tax-Override-with-Malicious-Collection

## Summary

This procedure assigns the malicious product collection to a tax override in Shopify's admin, embedding the XSS payload in the tax settings for later reflection during deletion.

## Description

Targeting the Settings > Taxes section, this step creates a tax override for 'Rest of World' and selects the collection from Step 1. The payload appears in the UI dropdown or list but does not execute yet, as no unsafe reflection occurs during addition. This requires admin privileges and sets up the vulnerability trigger. Outcome: Override active with payload visible.

## Requirements

1. Existing malicious collection from prior procedure
2. Authenticated admin access
3. Access to tax settings

## Defense

Defensive measures and detection strategies:

- Sanitize collection names when rendering in tax UI components
- Audit tax overrides for suspicious collection associations
- Enable rate limiting on admin UI actions

## Objectives

1. Link payload to tax configuration
2. Position for UI reflection on interaction
3. Maintain stealth until trigger

## Instructions

### Step 1: Navigate to Taxes Settings

**Context**: Access the tax management area to add overrides.

Go to Settings > Taxes in the admin dashboard. Scroll to 'Rest of World' and click 'Add a tax override'.

### Step 2: Select Malicious Collection

**Context**: Choose the collection to embed the payload.

In the override setup, select the malicious collection (named `'><IMG SRC=x onerror=prompt(7)>`) as the applicable product collection. Set any tax rate if prompted, then save.

> The payload is now tied to the override and visible in the list, but safe during this phase.

### Step 3: Confirm Assignment

**Context**: Verify the override is active.

Check the 'Rest of World' section; the override should list the collection name with payload intact.

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
- [[tax-settings]]
