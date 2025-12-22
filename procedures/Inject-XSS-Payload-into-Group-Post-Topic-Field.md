---
tags:
  - xss
  - injection
  - payload
  - ok.ru
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
updated_at: '2025-12-14T03:16:14.519Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: 5e4e6901-75b0-4150-9fde-a6660477caa1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Group-Post-Topic-Field

## Summary

This procedure involves entering a malicious JavaScript payload into the topic field of a new group post on ok.ru to exploit the lack of input sanitization.

## Description

The vulnerability stems from improper escaping in the topic field during post processing. The payload `'><svg onload=prompt(document.domain)>` closes any open tags and injects an SVG element that executes JavaScript on load. This step is performed in the browser's post form and leads to stored injection when submitted. Prerequisites include an open post form; outcomes confirm payload acceptance.

## Requirements

1. Open new post form in ok.ru group
2. Knowledge of XSS payloads
3. Active browser session

## Defense

Defensive measures and detection strategies:

- Client-side and server-side input sanitization (e.g., HTML entity encoding)
- Content Security Policy (CSP) to block inline scripts
- WAF rules to detect common XSS patterns

## Objectives

1. Insert executable JavaScript without triggering errors
2. Store the payload in the post context
3. Set up for execution trigger

## Instructions

### Step 1: Focus on Topic Field

**Context**: Prepare the input area for the payload.

Click into the topic field of the new post form to make it active.

> Cursor is positioned for text entry.

### Step 2: Enter the Payload

**Context**: Input the specific string designed to break out of HTML context and inject script.

Type or paste: `'><svg onload=prompt(document.domain)>`

> The field accepts the input without escaping or rejection.

### Step 3: Validate Input

**Context**: Ensure the payload is fully entered and form is intact.

Review the field content and confirm no auto-correction or warnings appear.

> Payload is ready for submission.

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
- [[injection]]
- [[payload]]
- [[ok.ru]]
