---
id: craft-acronis-xss-payload-001
tags:
  - xss
  - javascript
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
updated_at: '2025-12-13T23:55:37.666Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Craft-and-Verify-XSS-Payload-in-Custom-Parameter

## Summary

This procedure crafts a JavaScript payload for the reflected XSS in the Acronis form's 'c' parameter and verifies its execution by triggering a confirm dialog that displays document cookies.

## Description

Building on the reflection test, this step develops a payload that breaks out of HTML context and executes JS. The payload '1"<!--><Svg OnLoad=(confirm)(document.cookie)<!--' is injected into the 'c' parameter via POST. When reflected, it executes on page load, demonstrating cookie access. This targets browsers rendering the response, with outcomes including session theft. Requires prior confirmation of reflection.

## Requirements

1. Web browser supporting SVG onload events.
2. Ability to submit custom POST requests.
3. Understanding of HTML/JS context breaking.

## Defense

Defensive measures and detection strategies:

- Sanitize inputs by stripping or encoding dangerous characters like <, >, ".
- Implement strict output encoding for HTML contexts.
- Deploy Web Application Firewall (WAF) rules to block common XSS patterns.

## Objectives

1. Create a working XSS payload for the vulnerable parameter.
2. Execute JS to access sensitive data like cookies.
3. Validate the vulnerability's exploitability.

## Instructions

### Step 1: Design the Payload

**Context**: Construct a payload that closes any open attributes and injects executable JS.

Use the payload: 1"<!--><Svg OnLoad=(confirm)(document.cookie)<!--1. This closes a potential quote, comments out trailing content, and uses SVG onload to run confirm(document.cookie).

### Step 2: Inject via POST

**Context**: Submit the payload in the 'c' parameter to the target endpoint.

Send a POST request to https://www.acronis.com/en-us/my/remind/index.html with c=1"<!--><Svg OnLoad=(confirm)(document.cookie)<!-- and other required fields like Submit=Send.

> The server reflects the payload in the response HTML, e.g., value="1"<!--><Svg OnLoad=(confirm)(document.cookie)<!--", executing the JS.

### Step 3: Observe Execution

**Context**: Load the response in a browser to trigger the payload.

Upon submission, the page loads with the reflected content, popping a confirm dialog showing cookie contents.

> Expected output: Dialog box displaying all cookies from the domain, confirming JS execution.

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
- [[web]]

