---
id: proc-uuid-1
tags:
  - xss
  - dom-xss
  - jquery
  - recon
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.756Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-DOM-based-XSS-in-jQuery-location-hash

## Summary

This procedure involves manual inspection of web applications using outdated jQuery to detect DOM-based XSS vulnerabilities stemming from unsanitized insertion of location.hash into DOM elements like DIV.innerHTML.

## Description

In the context of Starbucks store subdomains on the Demandware platform, jQuery 1.10.1 processes the location.hash parameter without validation and inserts it directly into DIV.innerHTML, allowing attackers to inject HTML and JavaScript. This procedure outlines how to identify such flaws through code review, targeting international subdomains like store.starbucks.de and store.starbucks.ca. Successful identification confirms the vulnerability for further exploitation, potentially leading to client-side attacks in the victim's browser.

## Requirements

1. Access to a web browser with developer tools (e.g., Chrome DevTools).
2. Public accessibility to target subdomains (no authentication needed).
3. Basic knowledge of JavaScript and jQuery internals.

## Defense

Defensive measures and detection strategies:

- Update jQuery to version 3.x or later, which includes fixes for hash handling.
- Implement input sanitization or use textContent instead of innerHTML for dynamic content.
- Monitor for anomalous JavaScript execution via Content Security Policy (CSP).

## Objectives

1. Confirm presence of vulnerable jQuery version and code pattern.
2. Map affected endpoints and subdomains.
3. Establish foundation for payload crafting.

## Instructions

### Step 1: Inspect Target Subdomains

**Context**: Load the target page and examine the JavaScript source to identify jQuery usage.

Navigate to a subdomain like http://store.starbucks.de/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start in your browser. Open developer tools (F12), go to the Sources tab, and search for "jQuery" or "$.fn.jquery" to check the version.

> Look for code like $("div").html(location.hash) or similar unsanitized insertions.

### Step 2: Analyze location.hash Handling

**Context**: Review how the hash is processed to confirm lack of sanitization.

In the Console tab, execute:

```javascript
console.log($.fn.jquery);
```

> Expected output: "1.10.1". Then, search the code for "location.hash" and verify direct innerHTML assignment without escaping.

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
- [[dom-xss]]
- [[jquery]]
