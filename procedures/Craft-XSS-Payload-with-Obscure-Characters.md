---
tags:
  - xss
  - payload-craft
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8b5af128-c726-499a-a409-50c829c5079b
created_at: '2025-12-13T23:52:39.414Z'
updated_at: '2025-12-13T23:52:39.414Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-with-Obscure-Characters

## Summary

This procedure crafts a Stored XSS payload that bypasses HTML entity conversion filters by embedding malicious JavaScript within obscure characters, specifically targeting incomplete sanitization in message processing.

## Description

The vulnerability stems from the failure to convert non-standard characters like †‡•…‰€ to HTML entities, allowing tags like `<img>` with `onerror` handlers to execute. This is tested in a web context like Rockstar Games' feeds. Prerequisites: Knowledge of XSS vectors and a text editor for payload building. Outcomes: A functional payload that executes `alert('hacked')` or escalates to session theft.

## Requirements

1. Understanding of HTML/JS and Unicode characters
2. Local HTML file or online sandbox for testing
3. Access to the target platform for validation

## Defense

Defensive measures and detection strategies:

- Ensure all characters, including Unicode, are normalized and entity-encoded
- Employ strict output encoding (e.g., via libraries like DOMPurify)
- Log and alert on unusual character usage in inputs

## Objectives

1. Create a payload evading standard filters
2. Embed executable JavaScript for demonstration
3. Validate payload in isolated environment

## Instructions

### Step 1: Select Bypass Characters

**Context**: Choose characters not handled by the sanitization routine.

Identify obscure symbols: † (dagger), ‡ (double dagger), • (bullet), … (ellipsis), ‰ (per mille), € (euro). These avoid triggering entity conversion.

### Step 2: Build Malicious Tag

**Context**: Construct an img tag with onerror to execute JS.

Form the core: `<img src=a onerror=javascript:alert('hacked')>`. Note the full-width less-than/greater-than if needed, but here use standard with surrounds.

### Step 3: Assemble Full Payload

**Context**: Wrap to evade detection.

Combine: `†‡•＜img src=a onerror=javascript:alert('hacked')＞…‰€`. Test by saving as HTML and opening in browser.

> Expected output: Alert fires without sanitization blocking the tag.

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
- [[bypass]]
