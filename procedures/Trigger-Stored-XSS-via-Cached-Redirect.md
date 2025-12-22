---
tags:
  - stored-xss
  - web-exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1951f937-b6e9-4425-adef-fefda6cb72f4
created_at: '2025-12-14T00:11:25.458Z'
updated_at: '2025-12-14T00:11:25.458Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS via Cached Redirect

## Summary

This procedure involves accessing a previously poisoned cache entry to trigger the rendering of malicious content, resulting in stored XSS on targeted web pages like PayPal's sign-in page.

## Description

Once the cache is poisoned with a malicious redirect, any user accessing the affected page will have the attacker's content rendered, potentially executing JavaScript payloads. This interferes with page integrity but does not affect back-end systems.

## Requirements

1. Prior successful cache poisoning
2. Browser access to the targeted page
3. Optional: Web proxy for inspection

## Defense

Defensive measures and detection strategies:

- Regularly purge and validate cache entries
- Implement Content Security Policy (CSP) to mitigate XSS

## Objectives

1. Render malicious content on legitimate pages
2. Execute stored XSS payloads
3. Interfere with user interactions like sign-in

## Instructions

### Step 1: Access Poisoned Page

**Context**: Navigate to the cached resource to trigger the redirect and XSS.

> Open a browser and visit https://paypal.com/signin. The cached redirect will load the malicious content.

### Step 2: Verify XSS Execution

**Context**: Confirm the payload execution by checking browser console or page behavior.

> Look for alerts, script execution, or altered page content indicating successful XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[stored-xss]]
- [[web-exploitation]]
