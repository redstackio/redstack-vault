---
tags:
  - shopify
  - sales-channel
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7db2cc4e-d710-4ee7-84c3-b8f1b70af4ab
created_at: '2025-12-13T23:55:20.846Z'
updated_at: '2025-12-13T23:55:20.846Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Convert-Application-to-Sales-Channel

## Summary

This procedure converts a standard Shopify application to a sales channel type, unlocking the vulnerable SVG icon upload feature in the app configuration.

## Description

As part of the XSS exploitation chain, converting the app type exposes the icon upload endpoint that fails to properly sanitize SVGs with XML entities. This step targets the web interface of the Partners dashboard and requires the app to be already created. Outcomes include access to the App info section where the malicious payload can be introduced.

## Requirements

1. Existing app in the Partners dashboard
2. Partner account permissions for app extensions
3. Browser session active on the app settings page

## Defense

Defensive measures and detection strategies:

- Audit app type changes for unauthorized modifications
- Restrict sales channel conversions to verified partners
- Alert on rapid app reconfiguration post-creation

## Objectives

1. Enable sales channel-specific features like icon uploads
2. Position the app for payload integration
3. Avoid detection during configuration changes

## Instructions

### Step 1: Access App Extensions

**Context**: Navigate to the extensions management within the app to initiate type conversion.

No specific command; from the app overview, click "Extensions" in the sidebar.

> The extensions page loads. Expected output: Options for app types, including "Sales channel," are displayed.

### Step 2: Select and Save Sales Channel Type

**Context**: Choose the sales channel extension and persist the change to update the app.

No specific command; Select "Sales channel" and click "Save" or "Create extension."

> Changes apply immediately. Expected output: App status updates to sales channel, with new sections like App info available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[sales-channel]]
