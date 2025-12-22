---
id: proc-modify-input-type
tags:
  - bypass
  - client-side
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.443Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-HTML-Input-Type-with-Developer-Tools

## Summary

This procedure bypasses client-side restrictions on a file upload input by changing its HTML type attribute from 'file' to 'url' using browser developer tools, allowing URL submission instead of file selection.

## Description

Targeted at web applications enforcing input types client-side without server validation, this technique modifies the DOM to trick the form into accepting URLs. In the SSRF scenario, this leads to the server fetching remote resources. Prerequisites include access to the upload form and developer tools.

## Requirements

1. Browser with developer console (e.g., Chrome DevTools)
2. Loaded upload form page
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Validate input types server-side regardless of client submission
- Use Content Security Policy (CSP) to restrict DOM manipulations
- Log and monitor unusual form submissions

## Objectives

1. Alter the input to accept URLs
2. Enable submission of arbitrary remote endpoints
3. Set up for SSRF exploitation

## Instructions

### Step 1: Open Developer Tools

**Context**: Access the inspection interface to edit HTML.

No command; press F12 or right-click > Inspect.

> Developer console opens. Expected output: Elements tab shows page DOM.

### Step 2: Locate and Edit Input Element

**Context**: Find the file input and change its type.

In the Elements tab, search for input[type="file"], double-click the type attribute, and change to "url".

> Edit directly in the inspector. Expected output: Input now renders as text/URL field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[bypass]]
- [[client-side]]
