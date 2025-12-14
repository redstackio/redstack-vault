---
tags:
  - xss
  - reflected-xss
  - javascript-execution
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.397Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e4a16dde-2517-45c5-9854-469588410f16
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-for-Reflected-XSS

## Summary

This procedure exploits a confirmed reflected XSS vulnerability by injecting a URL-encoded JavaScript payload into a vulnerable parameter, leading to arbitrary code execution in the victim's browser. It is used in penetration testing to demonstrate client-side attacks such as session theft on web applications.

## Description

Once a parameter is identified as reflecting input unsanitized, craft a payload that breaks out of the context (e.g., HTML attribute) and executes JavaScript. In the DoD report, the payload %3Cimg/src/onerror=alert(document.domain)%3E (decoded: <img/src/onerror=alert(document.domain)>) was appended to the ██████= parameter, causing an alert with the domain upon page load. This targets browsers parsing the malicious img tag. Prerequisites: vulnerable endpoint confirmed. Expected outcomes: script execution, proof-of-concept alert, and potential data exfiltration if payload is modified (e.g., to send cookies to an attacker server).

## Requirements

1. Confirmed vulnerable parameter from prior identification
2. URL encoding tool or manual encoding knowledge
3. Victim browser (or self for PoC); no server-side access needed

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with libraries like OWASP ESAPI or built-in encoders
- Deploy Web Application Firewall (WAF) rules to block common XSS payloads
- Enable strict CSP to prevent inline script execution
- Log and alert on anomalous JavaScript in parameters

## Objectives

1. Execute arbitrary JavaScript in browser context
2. Demonstrate impact like domain alerting or session theft
3. Validate vulnerability for reporting

## Instructions

### Step 1: Craft and Encode Payload

**Context**: Create a simple JavaScript payload that executes on error (e.g., broken img src) to avoid direct script tags if filtered.

No command; manually encode: Use an online encoder or browser console to convert <img/src/onerror=alert(document.domain)> to %3Cimg%2Fsrc%2Fonerror%3Dalert(document.domain)%3E.

> This payload uses an onerror handler to trigger the alert reliably.

### Step 2: Inject Payload via Request

**Context**: Append the encoded payload to the parameter and send the request to trigger execution.

**Command** ([[commands/curl-xss-payload]]):
```bash
curl -s "https://█████?██████=%3Cimg%2Fsrc%2Fonerror%3Dalert(document.domain)%3E"
```

> Run this in a terminal, but for execution, visit the URL in a browser. The response will include the payload, and the browser will parse and execute it, showing an alert with the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[JavaScript]]
