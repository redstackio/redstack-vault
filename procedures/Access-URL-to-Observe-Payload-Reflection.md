---
tags:
  - xss
  - payload-reflection
  - browser-testing
type: procedure
tools:
  - '[[tools/Web-Browser]]'
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
updated_at: '2025-12-14T00:11:16.138Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c8ed07d3-6bd4-4aeb-8267-239c07732cb5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-URL-to-Observe-Payload-Reflection

## Summary

This procedure loads the crafted malicious URL in a browser to inspect how the injected payload reflects in the page's HTML, title, JSON responses, and search results, confirming the vulnerability's presence.

## Description

The Mail.ru search at go.mail.ru/search uses a Yandex Neuralsearch API backend, reflecting the 'q' parameter in multiple contexts: page title, JSON state (escaped as Unicode), and dynamic search snippets. Loading the URL allows observation of partial escaping, indicating potential for XSS. This step requires a modern browser with dev tools for inspection.

## Requirements

1. Crafted URL from prior procedure
2. Web browser with developer tools (e.g., Chrome)
3. Network access to Mail.ru

## Defense

Defensive measures and detection strategies:

- Enforce context-aware output encoding (e.g., HTML vs. JSON)
- Log and alert on reflected queries with script tags
- Deploy WAF rules to block common XSS payloads

## Objectives

1. Visualize payload reflection in real-time
2. Identify weak sanitization points
3. Gather evidence for exploitation potential

## Instructions

### Step 1: Load the URL

**Context**: Navigate to the malicious URL to trigger the search and reflection.

No command; paste `https://go.mail.ru/search?fr=mn&q=%3Cscript%3Ealert(1)%3C%2Fscript%3E` into the browser address bar and press Enter.

> Expected output: Search page loads with payload in title and results.

### Step 2: Inspect Elements

**Context**: Use dev tools to examine source and network.

No command; right-click page > Inspect > Network tab to see API calls; search for payload in response bodies.

> Expected output: Reflection in JSON (e.g., `query: '\\\u003cpayload\\\>'`) and HTML snippets.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[reflection]]
