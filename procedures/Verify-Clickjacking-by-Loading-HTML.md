---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - clickjacking
  - verification
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.281Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify-Clickjacking-by-Loading-HTML

## Summary

This procedure loads the created HTML page in a browser to verify that the target site embeds successfully in the iframe, confirming the clickjacking vulnerability.

## Description

The final verification step in a clickjacking demonstration involves opening the attacker-controlled HTML file and observing if the WordPress plugin directory site loads within the iframe without any framing errors or restrictions. Interaction with the embedded content, such as clicking links, should work seamlessly, proving that users could be tricked into performing actions on the hidden site. This targets web browsers and highlights low-severity impacts like potential unauthorized clicks, though no direct compromise occurs here.

## Requirements

1. Web browser
2. The previously created HTML file
3. Local file access

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: SAMEORIGIN to prevent external embedding
- Implement browser-based frame-busting JavaScript
- Log and alert on cross-origin iframe requests in security tools

## Objectives

1. Confirm unrestricted embedding
2. Test interactivity within iframe
3. Validate exploit potential

## Instructions

### Step 1: Open HTML File

**Context**: Load the page to initiate the embedding test.

Double-click the demo.html file or use File > Open in your browser.

> The page should display with the iframe loading the target site.

### Step 2: Interact and Verify

**Context**: Test functionality to ensure no restrictions.

Click elements within the iframe, such as links or buttons on the WordPress site.

> Expected: Full interaction possible; no errors like "Refused to display in a frame." Success confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[vulnerability-verification]]
