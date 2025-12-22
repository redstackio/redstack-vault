---
id: proc-wordpress-inject-xss-001
tags:
  - xss
  - stored-xss
  - payload-injection
  - wordpress
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
updated_at: '2025-12-14T03:16:37.249Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-App-Description

## Summary

This procedure injects a proof-of-concept JavaScript payload into the WordPress app description field, exploiting lack of sanitization to store executable code server-side.

## Description

Targeting the Description field in the app creation form, this step crafts and submits an XSS payload that breaks out of HTML context and includes an onmouseover event for delayed execution. The payload is stored without escaping and later reflected in the OAuth authorize page. Prerequisites include populated basic fields; outcomes enable arbitrary JS in victim sessions.

## Requirements

1. Completed basic field population
2. Knowledge of XSS payloads (e.g., HTML breakouts)
3. Ability to note generated client ID post-save

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user input in description fields (e.g., using HTML entity encoding)
- Content Security Policy (CSP) to block inline JavaScript
- Scan stored content for script tags or event handlers before rendering

## Objectives

1. Store unsanitized JavaScript in app metadata
2. Obtain client ID for URL construction
3. Set up reflection vector for victims

## Instructions

### Step 1: Craft and Submit Payload

**Context**: Insert the malicious payload to exploit the vulnerable field.

No command required; paste `'><div id="test"><head><base href="javascript://"></head><body><a href="/. /, /' onmouseover=confirm(document.domain); abc=abc">TESTLINK` into the Description field, then click Save.

> Expected output: Application saves successfully; client ID (e.g., 123456) is generated and displayed on the apps list page.

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
- [[stored-xss]]
- [[wordpress]]
