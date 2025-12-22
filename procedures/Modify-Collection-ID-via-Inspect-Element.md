---
tags:
  - authorization-bypass
  - idor
  - inspect-element
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.751Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: 108d4b3e-a313-48dd-8a78-eb3092ce83a3
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Modify-Collection-ID-via-Inspect-Element

## Summary

This procedure uses browser developer tools to alter the hidden collection_id in the tax override form, bypassing ShopID validation to reference foreign collections.

## Description

The root cause is the lack of ShopID ownership check in the tax_override[collection_id] parameter during form submission. By inspecting the HTML form elements (e.g., via Chrome DevTools), the attacker locates the input and changes its value to a foreign ID like '137861635' from another shop. This exploits an IDOR-like vulnerability in Shopify's Rails backend, allowing arbitrary collection references. Prerequisites include an open form from the prior step. Expected outcome is the form now targeting unauthorized data without triggering client-side errors.

## Requirements

1. Tax override form loaded with a local collection selected
2. Browser with developer tools (e.g., Chrome, Firefox)
3. Knowledge of a target foreign collection_id (e.g., from prior recon)

## Defense

Defensive measures and detection strategies:

- Server-side validation of collection ownership by ShopID
- Client-side integrity checks on form fields (e.g., CSRF + field hashing)
- Audit logs for mismatched collection IDs in requests

## Objectives

1. Inject foreign collection_id into the form
2. Bypass authorization without detection
3. Enable exposure of unauthorized collection names

## Instructions

### Step 1: Open Developer Tools

**Context**: Access inspection capabilities to view form HTML.

Right-click on the form and select 'Inspect Element' or press F12 to open DevTools.

### Step 2: Locate and Modify Input

**Context**: Target the specific hidden field for manipulation.

In the Elements tab, search for 'tax_override[collection_id]' and edit the value attribute to a foreign ID, e.g., 137861635.

> Double-click the value in the inspector and enter the new ID. The form now submits with the bypassed parameter, leading to unauthorized access upon save.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- authorization-bypass
- idor
- inspect-element
