---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - clickjacking
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
updated_at: '2025-12-14T17:28:12.291Z'
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
# Create-HTML-Page-with-Iframe-Embedding

## Summary

This procedure creates a simple HTML page that embeds the target WordPress site in an iframe, exploiting the lack of X-Frame-Options to demonstrate clickjacking feasibility.

## Description

To exploit clickjacking, an attacker constructs an HTML document with an iframe pointing to the vulnerable site. Attributes like src, width, height, and frameborder are set to make the embedded content visible or manipulable for overlaying deceptive elements. This file can be hosted on a malicious domain or tested locally. The target environment is any web browser, and the outcome is a proof-of-concept page showing unrestricted framing, which could trick users into clicking hidden buttons for actions like form submissions or data disclosure.

## Requirements

1. Text editor (e.g., Notepad, VS Code)
2. Local file system access
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header to block cross-origin framing
- Scan for iframe usage in client-side code and restrict via CSP
- Detect anomalous traffic patterns to sites from embedded contexts using server logs

## Objectives

1. Build iframe-based embedding
2. Prepare for UI redressing simulation
3. Confirm exploit readiness

## Instructions

### Step 1: Create HTML File

**Context**: Write the basic structure of the HTML page with iframe.

Use a text editor to create a file named demo.html.

Add the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Demo</title>
</head>
<body>
    <iframe src="https://mercantile.wordpress.org/" frameborder="0" height="550px" width="700px"></iframe>
</body>
</html>
```

> This creates a visible iframe; for real attacks, add transparent overlays with malicious elements.

### Step 2: Save and Prepare

**Context**: Ensure the file is ready for loading.

Save the file to your local directory.

> Expected: File saved without syntax errors, ready to open in browser.

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
- [[html-exploitation]]
