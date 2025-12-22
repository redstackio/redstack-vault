---
tags:
  - xss-trigger
  - firefox
  - javascript
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
updated_at: '2025-12-14T03:16:02.461Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8c5893b8-46a2-4557-8056-747a6640094e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-and-Trigger-XSS-in-Firefox

## Summary

This procedure accesses the uploaded .mml file URL in Firefox to render the MathML and trigger JavaScript execution upon user interaction.

## Description

When the file is served with application/mathml+xml, Firefox parses it as MathML, rendering the <math> element as clickable content. Interacting with it (e.g., clicking 'click page') executes the javascript:alert, demonstrating arbitrary JS execution. This affects any Firefox user viewing the file, enabling session hijacking or phishing.

## Requirements

1. Direct URL to the uploaded .mml file
2. Firefox browser (tested on version 63, Mac)
3. Victim-like access (no auth needed for public URLs)

## Defense

Defensive measures and detection strategies:

- Implement CSP headers blocking inline JavaScript
- Proxy file serves through sanitizing filters
- Educate users on risks of viewing unknown file types

## Objectives

1. Render the malicious MathML
2. Execute JavaScript payload
3. Confirm impact like data theft potential

## Instructions

### Step 1: Open File URL

**Context**: Load the stored file in Firefox.

Copy the direct blob URL from Active Storage and paste into Firefox address bar.

> Expected: Page renders MathML content without download prompt.

### Step 2: Interact to Trigger

**Context**: Activate the XSS vector.

Click within the rendered MathML element (e.g., the text 'click page').

> Expected: Alert dialog appears with the current page location, proving JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- firefox
- javascript
