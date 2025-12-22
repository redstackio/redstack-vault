---
tags:
  - xss-payload
  - markdown-injection
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
updated_at: '2025-12-14T03:16:31.100Z'
sub_techniques: []
id: e0c20900-96f0-4c03-9a2c-9916dd352f36
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Markdown-Payload

## Summary

This procedure inserts a malicious Markdown payload into the profile statement field, exploiting the lack of sanitization for javascript: URIs to enable Stored XSS.

## Description

The core of the attack involves crafting payloads that render as clickable links executing JavaScript. Tested payloads include link-based onerror handlers or direct script tags. This targets the Sundown Markdown library's misconfiguration via mikasa wrapper, allowing unsafe protocols. Prerequisites include an open edit form; outcome is payload ready for saving.

## Requirements

1. Open statement edit form
2. Knowledge of XSS payloads (e.g., javascript: URIs)
3. Web browser dev tools for testing

## Defense

Defensive measures and detection strategies:

- Enable HTML_SAFELINK flag in Markdown processors
- Strip or whitelist link protocols (block javascript:)
- Scan inputs for suspicious patterns like 'javascript:'

## Objectives

1. Embed executable JS in Markdown
2. Bypass input validation
3. Set up for stored execution

## Instructions

### Step 1: Craft Payload

**Context**: Select and prepare the malicious input.

Choose a payload like `[notmalicious](javascript:window.onerror=alert;throw%20document.cookie)` which creates a link that throws an error to capture cookies via onerror.

### Step 2: Enter Payload

**Context**: Input the payload into the form.

Paste the payload into the statement text area, ensuring it appears as plain text.

### Step 3: Preview if Available

**Context**: Optionally test rendering without saving.

If a preview option exists, use it to confirm the link renders; otherwise, proceed to save.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-payload]]
- [[web]]
