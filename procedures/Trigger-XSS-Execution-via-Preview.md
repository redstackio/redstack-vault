---
id: proc-005
tags:
  - xss
  - shopify
  - web
  - execution-trigger
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
updated_at: '2025-12-13T23:52:55.583Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Preview

## Summary

This procedure triggers the XSS payload by interacting with the preview functionality, causing the unsanitized App name to be rendered in a <script> tag and executing the injected JavaScript.

## Description

Clicking 'Preview changes' loads the page where the App name is inserted directly into JavaScript code without escaping. The payload executes in the browser context, demonstrating impact on victims viewing the listing (e.g., alert() or cookie theft).

## Requirements

1. Loaded malicious preview page in incognito
2. Visible 'Preview changes' button or equivalent
3. Browser supporting SVG onload (Firefox, IE, Edge; partial Safari)

## Defense

Defensive measures and detection strategies:

- Escape user input in JS contexts (e.g., replace < with \u003c)
- Implement JS sandboxing or strict CSP
- Detect anomalous JS execution via browser monitoring tools

## Objectives

1. Render the vulnerable page to execute payload
2. Confirm arbitrary JS in victim context
3. Highlight potential for data exfiltration

## Instructions

### Step 1: Locate Preview Button

**Context**: Identify the interaction that triggers rendering.

On the loaded preview page, find the 'Preview changes' option.

> Expected: Button available post-URL load.

### Step 2: Click to Trigger

**Context**: Force the insertion and execution.

Click 'Preview changes' to refresh/render the listing.

> Expected: Payload executes, e.g., alert dialog appears.

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
- [[shopify]]
- [[web]]
