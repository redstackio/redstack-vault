---
tags:
  - xss
  - copy-paste
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/decoded-mathml-xss]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: d18c291b-e926-4423-a7df-031f570137d6
created_at: '2025-12-13T23:55:06.770Z'
updated_at: '2025-12-13T23:55:06.770Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Copy-Payload-Text-for-Pasting

## Summary

This procedure copies the encoded XSS payload from the crafted HTML to the clipboard, preparing it for pasting into the Trix Editor where it will mutate and execute.

## Description

Copying the visible text from the HTML file transfers the hidden mutated MathML payload to the clipboard in a format that Trix Editor processes insecurely, leading to sanitizer bypass and JavaScript execution.

## Requirements

1. Crafted HTML file from previous procedure
2. Browser or text editor to select text

## Defense

- Implement clipboard content scanning in apps
- Use paste-as-plain-text options in editors

## Objectives

1. Transfer payload to clipboard
2. Maintain encoded structure

## Instructions

### Step 1: Select and Copy

**Context**: Highlight the 'copy me' text in the browser-rendered HTML.

**Command** (Manual):
```bash
# No CLI command; use Ctrl+C after selecting 'copy me' in browser
```

> The clipboard now holds the data-trix-attachment with mutated content.

### Step 2: Verify Clipboard

**Context**: Optionally paste into a plain text editor to inspect using [[commands/decoded-mathml-xss]] structure.

**Expected Output**: Encoded JSON with MathML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/decoded-mathml-xss]]

## Tools Used


## Tags

- [[xss]]
