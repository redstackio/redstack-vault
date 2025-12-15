---
tags:
  - xss
  - payload-craft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 22e91df3-5c35-49ec-af21-b5223c948bf6
created_at: '2025-12-14T17:26:55.707Z'
updated_at: '2025-12-14T17:26:55.707Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Malicious-Emoji-Payload-for-XSS

## Summary

This procedure creates a malicious emoji payload exploiting the lack of sanitization in phpBB's SMILEY_IMG field during import, allowing injection of XSS scripts like onmouseover alerts.

## Description

The emoji import parses files without HTML-escaping the SMILEY_IMG field, enabling stored XSS. The payload is crafted in the expected code block format for import, such as '"onmouseover=alert() ><script>alert()</script>"', which will be output unsanitized in forum posts and admin pages, affecting all viewers.

## Requirements

1. Knowledge of phpBB emoji import format
2. Text editor for payload creation
3. Target for testing import

## Defense

Defensive measures and detection strategies:

- Sanitize SMILEY_IMG with HTML entity encoding before storage and output
- Validate imported emoji files against strict whitelists
- Scan uploads for script tags or event handlers

## Objectives

1. Inject executable JavaScript into emoji data
2. Ensure payload survives import regex checks
3. Enable persistent execution on display

## Instructions

### Step 1: Design XSS Payload

**Context**: Create script that triggers on interaction, e.g., mouseover.

**Command** (Manual Creation):

Write: '"onmouseover=alert() ><script>alert()</script>"' as SMILEY_IMG value in emoji format.

> Expected output: String ready for embedding in temp file.

### Step 2: Format for Import

**Context**: Structure as expected by phpBB import parser.

**Command** (Manual):

Place in code block: code:SMILEY_IMG="payload" ...

> Expected output: File content that mimics valid emoji pack.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-craft]]
