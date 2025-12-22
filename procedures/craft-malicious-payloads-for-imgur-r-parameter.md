---
tags:
  - xss
  - payload-crafting
  - javascript
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
detection_risk: medium
sub_techniques: []
id: 44f00938-dea5-426f-b68c-48a1f7bd0762
created_at: '2025-12-14T03:15:26.995Z'
updated_at: '2025-12-14T03:15:26.995Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious Payloads for Imgur 'r' Parameter

## Summary

This procedure focuses on creating and testing JavaScript payloads for injection into the 'r' parameter of Imgur's GIF endpoints, exploiting the lack of sanitization to enable code execution when the resource is accessed.

## Description

Targeting Imgur's vulnerable endpoints, this involves embedding HTML and JS in the 'r' parameter, such as script tags that alert or log data. Payloads are persistent, executing in the viewer's browser upon GIF access or embedding. Prerequisites include endpoint identification; outcomes range from simple alerts to cookie exfiltration, potentially leading to session hijacking in a real attack.

## Requirements

1. Knowledge of JavaScript and HTML injection techniques
2. Access to the identified endpoints
3. Browser dev tools for payload testing

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Employ web application firewalls (WAF) to block script tags
- Log and alert on requests containing <script> patterns

## Objectives

1. Develop executable JS payloads for 'r' injection
2. Test payload reflection and execution
3. Simulate impacts like data logging

## Instructions

### Step 1: Build Basic Payload

**Context**: Start with a simple alert to confirm execution.

Craft `<script>alert(2)</script>` and append to 'r' parameter, e.g., `r=<script>alert(2)</script>`.

> When sent to the endpoint, the response should include the raw script tag, ready for execution on access.

### Step 2: Advanced Payload for Data Theft

**Context**: Escalate to exfiltrate sensitive info like cookies.

Use `<script>console.log('XSS', document.cookie)</script>` in 'r'.

> Expected output: On endpoint access, console logs cookies, demonstrating collection capability.

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
- [[JavaScript]]
