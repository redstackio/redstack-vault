---
tags:
  - xss
  - open-redirect
  - nextcloud
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
updated_at: '2025-12-14T00:11:16.064Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 87009601-4a20-4fad-8be3-2a09a9b56789
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Opening-Image-in-New-Tab

## Summary

This procedure triggers the stored XSS by opening the contact image URL directly in a new browser tab, causing Chrome/Chromium to render the SVG and execute the embedded JavaScript.

## Description

Bypassing the modal's safe rendering, opening the raw image URL in a new tab forces the browser to process the SVG content, executing scripts. This leads to arbitrary JS execution, such as cookie theft or redirects, impacting the victim with low-severity effects like session hijacking.

## Requirements

1. Open modal from previous step with malicious image
2. Chrome or Chromium-based browser
3. Victim interaction to open in new tab

## Defense

Defensive measures and detection strategies:

- Serve images with strict Content-Security-Policy (CSP) blocking inline scripts
- Validate and sanitize image content on render
- Detect and block direct SVG rendering from user-generated content

## Objectives

1. Execute JavaScript payload in victim's browser
2. Achieve data exfiltration or redirect
3. Compromise session without further interaction

## Instructions

### Step 1: Access Image URL in Modal

**Context**: From the open modal, identify the direct URL of the image.

In the modal view, inspect or right-click the image to copy its URL (e.g., Nextcloud's image endpoint).

> URL points to the stored SVG file.

### Step 2: Open URL in New Tab

**Context**: Force browser rendering of the SVG content.

Right-click the image in the modal and select 'Open image in new tab', or paste the URL into a new tab.

> Browser renders SVG, executing <script> tags; e.g., redirect to attacker site with stolen cookies.

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
- [[open-redirect]]
- [[nextcloud]]
