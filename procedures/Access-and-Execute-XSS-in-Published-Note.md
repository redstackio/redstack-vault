---
id: proc-uuid-003
name: Access-and-Execute-XSS-in-Published-Note
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.356Z'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss-execution
  - javascript
  - svg-trigger
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Access-and-Execute-XSS-in-Published-Note

## Summary

This procedure involves accessing the published note URL and interacting with the rendered SVG to trigger the stored XSS, executing arbitrary JavaScript in the app.simplenote.com context for session theft or data exfiltration.

## Description

Once published, the note's Markdown is rendered in the viewer's browser, parsing the SVG and allowing the <animate> attribute to execute the javascript: URI on click. This affects logged-in users, potentially leading to account compromise. The procedure requires the victim to be authenticated; outcomes include JS execution like alerts or more malicious actions (e.g., cookie theft).

## Requirements

1. Published note URL from previous procedure
2. Victim browser session authenticated to Simplenote
3. No tools; browser interaction only

## Defense

Defensive measures and detection strategies:

- Block or escape animate attributes in SVG sanitizers
- Implement user-agent or behavior monitoring for unexpected JS pops
- Educate users on not clicking suspicious elements in shared notes

## Objectives

1. Render the payload in victim context
2. Trigger JS execution for impact
3. Collect session data or perform actions on behalf of victim

## Instructions

### Step 1: Navigate to Published URL

**Context**: Load the note to initiate Markdown rendering of the SVG.

Open the URL in a browser logged into app.simplenote.com.

> Page loads with note content; SVG appears as a large black circle.

### Step 2: Interact with SVG Element

**Context**: Click the rendered element to animate and execute the payload.

Click the black rectangle (circle) in the SVG.

> Animation changes xlink:href, executing javascript:alert(document.domain); alert confirms success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[JavaScript]]
- [[svg-trigger]]
