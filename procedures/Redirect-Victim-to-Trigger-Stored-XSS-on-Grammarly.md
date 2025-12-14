---
tags:
  - redirect
  - xss-trigger
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 6762bc13-ee2c-40ee-8972-3faec777c668
created_at: '2025-12-14T17:33:34.374Z'
updated_at: '2025-12-14T17:33:34.374Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Redirect-Victim-to-Trigger-Stored-XSS-on-Grammarly

## Summary

This procedure redirects the victim from the malicious page to a specific Grammarly URL where the tainted gnar_containerId cookie is reflected in a noscript tag's img src, executing the injected XSS payload.

## Description

The reflection occurs on www.grammarly.com/upgrade page in a noscript fallback img tag without proper encoding, allowing the payload to inject and load poc.js in the victim's authenticated context.

## Requirements

1. Malicious cookie already set
2. Victim authenticated to Grammarly
3. JavaScript execution on malicious page

## Defense

Defensive measures and detection strategies:

- Encode cookie values in all HTML attributes (e.g., URL-encode src)
- Avoid reflecting user-controlled data in noscript contexts
- Log and monitor redirects from suspicious domains

## Objectives

1. Load the vulnerable page
2. Trigger payload execution
3. Transition to victim's Grammarly session

## Instructions

### Step 1: Implement Redirect in Script

**Context**: After setting the cookie, redirect to the reflection point.

In JavaScript:
```javascript
window.location.replace('https://www.grammarly.com/upgrade?utm_source=upHook&app_type=app&page=free&utm_campaign=editorMenu&utm_medium=internal');
```

> Expected output: Browser navigates to Grammarly; payload executes silently.

### Step 2: Verify Trigger

**Context**: Check browser console for script load.

Monitor network tab for poc.js request.

> Success if external script loads without CSP blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[redirect]]
- [[stored-xss]]
