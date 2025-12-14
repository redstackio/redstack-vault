---
tags:
  - xss
  - injection
  - paste-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6691d284-bb32-4ac2-93ec-75d80bbe5900
created_at: '2025-12-14T00:11:09.524Z'
updated_at: '2025-12-14T00:11:09.524Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-HTML-via-Ctrl-Shift-V-Paste

## Summary

This procedure exploits the Ctrl+Shift+V paste functionality in Nextcloud's Text app to insert HTML content via innerHTML, enabling self-XSS in the Markdown editor.

## Description

The Nextcloud Text app's Markdown editor handles Ctrl+Shift+V (intended for plaintext) by inserting content directly into a DOM element's innerHTML property, allowing arbitrary HTML injection. This occurs before any schema processing, making it vulnerable to rendering malicious structures. The target is any .md file in the app, requiring authenticated access. Expected outcome is the payload insertion without sanitization, leading to DOM manipulation.

## Requirements

1. Authenticated session in Nextcloud
2. Text app installed and accessible
3. Open Markdown file in the editor
4. Prepared HTML payload in clipboard

## Defense

Defensive measures and detection strategies:

- Implement plaintext-only paste handlers (e.g., textContent instead of innerHTML)
- Client-side input validation for paste events
- User training on paste sources

## Objectives

1. Bypass plaintext paste expectation
2. Insert HTML into editor DOM
3. Set up for rendering exploitation

## Instructions

### Step 1: Open Target File and Paste

**Context**: This step targets the vulnerable paste mechanism to inject the payload into the editor.

Navigate to a .md file in Nextcloud Text app, place cursor in the editor, and press Ctrl+Shift+V (or Cmd+Shift+V on macOS).

```
# No command; manual keyboard shortcut: Ctrl+Shift+V
```

> The content from clipboard is inserted via innerHTML. Verify by checking the editor content post-paste.

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
- [[injection]]
