---
id: proc-upload-svg
tags:
  - ssrf
  - upload
  - svg
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
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.496Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-SVG-to-Trigger-SSRF

## Summary

This procedure uploads a crafted SVG file to Shopify's product image feature, causing the server-side parser to fetch referenced resources and execute SSRF.

## Description

During product creation, Shopify processes uploaded SVGs, including fetching external or local resources via xlink:href. This exploits the lack of URL validation, leading to arbitrary requests. Requires prior access to the upload interface; outcomes include server-initiated fetches observable via listeners or rendering.

## Requirements

1. Crafted SVG file from previous procedure
2. Active Shopify product creation session
3. Optional: Running listener for private tests

## Defense

Defensive measures and detection strategies:

- Disable SVG uploads or use secure parsers like librsvg with restrictions
- Validate and sandbox resource fetches during image processing
- Audit upload logs for anomalous file types and sizes

## Objectives

1. Submit the SVG for server processing
2. Trigger unauthorized resource fetches
3. Achieve SSRF for disclosure or scanning

## Instructions

### Step 1: Select Upload Field

**Context**: Locate the image attachment in the product form.

In the product editor, click the image upload area.

> Expected: File picker opens.

### Step 2: Attach and Submit

**Context**: Upload the malicious SVG.

Select the .svg file and save the product; the parser activates on upload.

> Expected: Upload succeeds, fetch occurs server-side without client errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- file-upload
