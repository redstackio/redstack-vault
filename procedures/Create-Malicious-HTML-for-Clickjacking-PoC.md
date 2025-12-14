---
tags:
  - clickjacking
  - html
  - iframe
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
updated_at: '2025-12-14T17:28:12.820Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 7a2998cb-e725-4b72-a94c-8bfbe4ec3074
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-HTML-for-Clickjacking-PoC

## Summary

This procedure creates a simple HTML file that embeds the Acronis CAS login page in an iframe, exploiting the lack of frame protection to demonstrate clickjacking potential.

## Description

Clickjacking involves tricking users into clicking on invisible elements overlaid on a legitimate page. Here, the target https://cas.acronis.com/ login page can be iframed without restrictions due to missing CSP frame-ancestors or X-Frame-Options headers. An attacker can host this HTML or send it as an attachment, then add transparent overlays to capture clicks on actions like account deactivation. Prerequisites include a text editor; no server hosting is needed for local PoC.

## Requirements

1. Text editor installed on the attacker's machine
2. Knowledge of basic HTML syntax
3. Internet access to verify the target URL

## Defense

Defensive measures and detection strategies:

- Implement Content-Security-Policy header with frame-ancestors 'self' to restrict framing
- Use X-Frame-Options: DENY or SAMEORIGIN to prevent embedding
- Monitor for unusual iframe embeddings in web traffic logs

## Objectives

1. Generate PoC HTML to embed the vulnerable login page
2. Verify the absence of frame protections
3. Set up for overlaying malicious elements to hijack user interactions

## Instructions

### Step 1: Open Text Editor

**Context**: Start creating the HTML structure for the iframe.

Open a text editor like Notepad or VS Code.

### Step 2: Write HTML Code

**Context**: Input the exact HTML that sources the target in an iframe.

Paste the following HTML:

```html
<!DOCTYPE HTML><html lang="en-US"><head><meta charset="UTF-8"><title>I Frame</title></head><body><h2>Clickjacking Vulnerability</h2><iframe src="https://cas.acronis.com/" frameborder="0" height="700px" width="850px"></iframe></body></html>
```

> This code creates a basic page with an iframe loading the login page. In a full attack, add CSS for invisible overlays positioned over buttons.

### Step 3: Review and Adjust

**Context**: Ensure the iframe dimensions cover the target elements.

Adjust height and width if needed to match the login page layout.

**Expected Output**: Valid HTML ready for saving.

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
- [[iframe]]
- [[html-poc]]
