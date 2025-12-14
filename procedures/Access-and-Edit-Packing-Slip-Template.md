---
tags:
  - broken-access-control
  - template-edit
  - data-exposure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.441Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a21501ce-d7b5-4716-af5d-885d33fe50db
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access-and-Edit-Packing-Slip-Template

## Summary

This procedure exploits broken access control in Shopify's packing slip template endpoint, enabling a zero-permission staff user to edit the template and preview sensitive product and shipping data via PDF generation.

## Description

The vulnerability stems from the /admin/settings/packing_slip_template endpoint lacking proper authorization checks, allowing any authenticated user, even with no permissions, to load, edit, and preview the template. In an attack scenario, a low-priv staff logs in and directly navigates to the URL, modifies the Liquid template if desired, and uses the preview to expose store data. The target is Shopify's web admin panel in a sandbox store. Prerequisites: A configured sandbox with data and a low-priv staff account. Expected outcomes: Unauthorized access to editor and data disclosure in preview PDF.

## Requirements

1. Active low-privileged staff session in the sandbox store.
2. Pre-configured products and shipping data in the store.
3. Web browser capable of handling PDF previews.

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) checks on all admin endpoints, including template editors.
- Log and alert on access to sensitive endpoints from low-priv accounts; use WAF rules to block unauthorized URL patterns.

## Objectives

1. Bypass authorization to access the template editor.
2. Edit the template to potentially inject malicious content.
3. Preview and extract sensitive store data.

## Instructions

### Step 1: Navigate to Vulnerable Endpoint

**Context**: Directly access the packing slip template page as staff to test controls.

From the staff session, enter https://<store>.myshopify.com/admin/settings/packing_slip_template in the address bar and press enter.

> The page should load the template editor without errors, confirming the bypass.

### Step 2: Edit and Save Template

**Context**: Demonstrate full control by modifying the template.

In the editor, alter the Liquid code (e.g., add a custom field or comment), then click "Save".

> Changes persist, showing write access despite no permissions.

### Step 3: Generate Preview for Data Exposure

**Context**: Use preview to view and exfiltrate sensitive information.

Click the "Preview" button to generate a PDF of a sample packing slip.

> The PDF includes unauthorized details like product lists and shipping addresses; download or screenshot for evidence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-access-control]]
- [[template-edit]]
- [[data-exposure]]
