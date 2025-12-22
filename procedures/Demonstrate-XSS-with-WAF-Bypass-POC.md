---
id: 123e4567-e89b-12d3-a456-426614174002
name: Demonstrate-XSS-with-WAF-Bypass-POC
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.659Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - waf-bypass
  - poc
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Demonstrate-XSS-with-WAF-Bypass-POC

## Summary

This procedure details crafting and testing a proof-of-concept (POC) payload for the reflected XSS vulnerability that evades the web application firewall (WAF), confirming the ability to execute arbitrary JavaScript in the victim's browser.

## Description

Building on the discovered vulnerability in the Rockstar Games video player, this involves creating obfuscated payloads to bypass WAF rules that might detect standard XSS strings like 'script' or 'alert'. Techniques include case manipulation, encoding, or alternative tags. Successful execution demonstrates medium-severity impact, such as stealing session cookies via `document.cookie`. Requires proxy tools for request manipulation and ethical disclosure context.

## Requirements

1. Proxy interceptor like Burp Suite or OWASP ZAP
2. Knowledge of WAF evasion techniques (e.g., payload obfuscation)
3. Access to the vulnerable endpoint on www.rockstargames.com/reddeadredemption

## Defense

Defensive measures and detection strategies:

- Update WAF rules to detect obfuscated payloads (e.g., via regex for mixed-case scripts)
- Employ client-side sanitization libraries like DOMPurify
- Log and alert on suspicious parameter values in video player requests

## Objectives

1. Bypass WAF to deliver the XSS payload
2. Execute JavaScript to simulate impact (e.g., cookie theft)
3. Document the POC for vulnerability reporting

## Instructions

### Step 1: Intercept and Analyze Request

**Context**: Capture the legitimate request to the video player to identify injectable parameters.

Use Burp Suite to proxy traffic. Navigate to the video player, submit a normal input, and intercept the POST/GET request. Note parameters like 'video_url' or 'query' that reach the reflection point.

### Step 2: Craft Obfuscated Payload

**Context**: Modify the payload to evade WAF detection while preserving XSS functionality.

Replace standard payload with an obfuscated version, e.g., `<sCrIpT>alert(document.domain)</sCrIpT>` or using event handlers like `onerror=alert(1)`. Ensure it targets the reflected context (e.g., img src if applicable).

### Step 3: Test and Execute POC

**Context**: Replay the modified request and verify execution.

Forward the intercepted request with the payload through the proxy. Observe if the WAF blocks it; iterate on obfuscation if needed. Upon success, check the browser for JavaScript execution, such as an alert or console output showing site domain.

> Expected: Payload executes without WAF intervention, confirming bypass and XSS viability.

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
- [[poc]]
