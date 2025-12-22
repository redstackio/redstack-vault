---
tags:
  - xss
  - svg-upload
  - xml-entity
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ef558ae3-46cf-43de-bdd6-715c05eef4a1
created_at: '2025-12-13T23:55:20.845Z'
updated_at: '2025-12-13T23:55:20.845Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-SVG-Icon

## Summary

This procedure involves uploading a crafted malicious SVG icon to a Shopify sales channel app, exploiting XML entity parsing to bypass attribute whitelisting and embed JavaScript for XSS.

## Description

The core of the vulnerability lies in Shopify's SVG sanitization failing open during XML parsing errors induced by entities, allowing onload attributes to execute JavaScript. This targets the App info upload field in the Partners dashboard. Prerequisites include a sales channel app; outcomes enable stored XSS rendering on save.

## Requirements

1. Sales channel app configured in Partners dashboard
2. Malicious SVG file prepared with XML entity and onload payload
3. Active browser session on the app's App info page

## Defense

Defensive measures and detection strategies:

- Enhance SVG sanitization to handle XML entities strictly
- Validate uploads against comprehensive attribute blacklists
- Scan uploaded files for JavaScript patterns pre-persistence

## Objectives

1. Bypass whitelist to include executable attributes in SVG
2. Store the payload for rendering in admin contexts
3. Set up for immediate XSS on save and later on authorization

## Instructions

### Step 1: Prepare Malicious SVG

**Context**: Craft the SVG with an XML entity to trigger parsing failure and preserve the onload attribute.

No specific command; Create a file with content: <?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE svg [<!ENTITY elem "">]><svg onload="alert(document.domain);" height="16" width="16">&elem;</svg>

> Save as .svg. Expected output: Valid-looking icon file ready for upload.

### Step 2: Upload to App Info

**Context**: Use the upload interface to submit the file, exploiting the sanitization gap.

No specific command; In App info, locate the icon upload field and select the SVG file, then proceed without saving yet.

> Upload processes. Expected output: File accepted; no rejection for malicious content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[svg-upload]]
- [[xml-entity]]
