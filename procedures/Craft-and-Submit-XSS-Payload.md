---
id: p-craft-xss-payload
tags:
  - xss
  - svg-payload
  - waf-bypass
  - web
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
updated_at: '2025-12-13T23:52:21.100Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Submit XSS Payload

## Summary

This procedure crafts a specialized XSS payload using an SVG element with an onauxclick event handler to bypass WAF filters and inject executable JavaScript into a reflected HTML injection point.

## Description

Standard XSS payloads like <script>alert(1)</script> are often blocked by WAFs, but SVG elements are less commonly filtered. The payload injects an SVG with attributes that render a visible graphic and attach a JavaScript event (onauxclick) triggered by auxiliary mouse clicks. This executes in the browser's context, confirming XSS. Target environments include web apps with partial sanitization. Prerequisites: confirmed HTML injection from prior recon. Outcomes: reflected SVG ready for triggering, evading basic WAF rules.

## Requirements

1. Knowledge of the vulnerable input field from Step 1
2. Browser or proxy (e.g., Burp Suite) for payload submission and inspection
3. Understanding of HTML/SVG syntax and event handlers

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs with HTML entity encoding and strip dangerous tags/attributes
- Configure WAF to block SVG injections and event handlers like onauxclick
- Enable strict CSP to prevent event handler execution
- Log and monitor anomalous SVG renders or event firings

## Objectives

1. Create a WAF-bypassing payload using SVG for XSS
2. Submit and verify reflection without blocking
3. Prepare for JavaScript execution via event trigger

## Instructions

### Step 1: Design the Payload

**Context**: Build a payload that closes the reflected tag, injects SVG, and adds a low-profile event handler.

Construct: `1"><svg height="1000" width="1000" onauxclick=confirm`12233`><circle cx="500" cy="500" r="400" stroke="black" stroke-width="3" fill="red"/></svg>`. The `1">` breaks out of attributes; SVG renders a red circle; onauxclick runs confirm(12233).

**Expected Output**: Payload string ready for submission.

### Step 2: Submit and Verify

**Context**: Inject the payload into the vulnerable field and check for successful reflection.

Enter the payload in the input (e.g., search box) and submit. Inspect the page source to ensure the SVG is intact and renders visually.

**Expected Output**: Red circle appears on the page; source shows full SVG with onauxclick attribute.

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
- [[waf-bypass]]
