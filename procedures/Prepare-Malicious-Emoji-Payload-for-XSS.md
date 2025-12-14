---
tags:
  - xss
  - payload-craft
  - phpbb
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
updated_at: '2025-12-13T23:55:06.101Z'
sub_techniques: []
id: 6b68cfca-032a-49a9-9403-a8d85c9a4ec5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Prepare-Malicious-Emoji-Payload-for-XSS

## Summary

This procedure crafts a malicious emoji pak file content that injects unsanitized XSS payloads into the SMILEY_IMG field during import, enabling stored XSS execution.

## Description

phpBB's emoji import lacks HTML entity encoding, allowing direct injection of JavaScript into smiley images. The payload is formatted as CSV-like lines for the pak file, exploiting the storage and display mechanism to affect all users viewing posts or admin sections.

## Requirements

1. Knowledge of XSS payloads
2. Text editor for payload creation
3. Target phpBB version vulnerable to unsanitized imports

## Defense

Defensive measures and detection strategies:

- Sanitize imported emoji data with htmlspecialchars()
- Validate emoji file formats strictly
- Scan for script tags in uploads

## Objectives

1. Create injectable XSS in emoji format
2. Ensure compatibility with pak import
3. Enable persistent execution on display

## Instructions

### Step 1: Design Payload

**Context**: Build the XSS string targeting onmouseover or inline script.

Use payload: '"onmouseover=alert() ><script>alert()</script>", "17", "18", "1", "POC", ":POC:",'

### Step 2: Validate Format

**Context**: Ensure it matches pak file structure (code, width, height, remote, disc, emoticon).

Test parsing manually to confirm injection points.

> Expected output: Valid emoji line with embedded XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-craft
- phpbb

