---
id: proc-trigger-domxss-visit
tags:
  - dom-xss
  - javascript-injection
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
updated_at: '2025-12-13T23:06:26.569Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-based-XSS-by-Visiting-Poisoned-Page

## Summary

This procedure triggers the DOM-based XSS by loading the cache-poisoned page in a browser, where JavaScript fetches and injects unescaped JSON from the attacker's domain into the page DOM.

## Description

After cache poisoning, visiting the URL causes the browser to parse the tainted HTML with 'data-site-root' pointing to the attacker's JSON endpoint. The client-side JavaScript on catalog.data.gov fetches this JSON and writes it directly to the DOM without escaping, allowing the payload (e.g., malicious SVG) to execute. This results in stored XSS affecting any visitor to the poisoned page.

## Requirements

1. Successful prior cache poisoning
2. Web browser with developer tools for inspection
3. Access to the poisoned URL: https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all dynamic content injected into the DOM
- Validate JSON sources and use safe parsing methods (e.g., textContent instead of innerHTML)
- Implement strict CSP to block external fetches or inline scripts
- Log and alert on unexpected JSON fetches from non-whitelisted domains

## Objectives

1. Load the poisoned response to initiate the JSON fetch
2. Inject the malicious payload into the DOM
3. Prepare for XSS execution in the victim's browser

## Instructions

### Step 1: Navigate to Poisoned URL

**Context**: Open the target page in a browser to trigger the client-side logic.

**Instructions**: Visit https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6 in a modern web browser. Monitor the Network tab in developer tools for the JSON fetch.

> Expected: Page loads; a request to the attacker's JSON endpoint (e.g., portswigger-labs.net/.../json.php?) occurs, followed by DOM injection.

### Step 2: Inspect for Injection

**Context**: Verify the tainted attributes and fetch.

**Instructions**: Use browser dev tools to check the (body) tag (/body) for 'data-site-root' and observe the injected content.

> Expected: Console shows no errors; DOM elements reflect unescaped JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dom-xss
- javascript-injection
