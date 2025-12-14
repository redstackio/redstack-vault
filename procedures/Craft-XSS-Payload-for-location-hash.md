---
id: proc-uuid-2
tags:
  - xss
  - payload-crafting
  - jquery
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
updated_at: '2025-12-14T03:47:12.754Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-for-location-hash

## Summary

This procedure details crafting a malicious payload that exploits jQuery's vulnerable selector parsing in location.hash to inject executable HTML/JavaScript, specifically targeting innerHTML insertion flaws.

## Description

Exploiting jQuery 1.10.1's improper handling of location.hash, the payload uses attribute selector tricks to inject an img tag with an onerror handler. When inserted via innerHTML, it executes JavaScript like alert(document.domain). This is applicable to Starbucks subdomains on Demandware, where the hash is processed on page load, enabling DOM-based XSS without server interaction.

## Requirements

1. Knowledge of jQuery selector vulnerabilities (e.g., attribute ending selectors).
2. Target URL from reconnaissance (e.g., store.starbucks.de endpoint).
3. Text editor or browser URL bar for payload construction.

## Defense

Defensive measures and detection strategies:

- Validate and escape all client-side inputs, including URL fragments.
- Use DOMPurify or similar libraries for sanitization.
- Deploy CSP to block inline script execution from injected elements.

## Objectives

1. Create a payload that evades basic filtering and triggers execution.
2. Ensure compatibility with browsers like Chrome and IE 11.
3. Prepare for delivery via URL hash.

## Instructions

### Step 1: Design Core Payload

**Context**: Build the injection using a broken attribute selector to force HTML insertion.

Construct the base: `<img onerror="alert(document.domain)" src=x.jpg`. Wrap in jQuery selector: `a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>`.

> This exploits jQuery's parsing to insert the img tag directly.

### Step 2: Append to URL Hash

**Context**: Integrate the payload into the target URL.

Take the base URL (e.g., http://store.starbucks.de/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start) and append `#` followed by the payload: `#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>`.

> Test locally by pasting into browser address bar to validate syntax.

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
- [[payload-crafting]]
