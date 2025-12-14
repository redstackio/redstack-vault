---
tags:
  - xss
  - discovery
  - web
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
updated_at: '2025-12-14T17:28:28.181Z'
sub_techniques: []
id: 972ea3fa-f56c-4d4f-a856-0e5acaf7ad97
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Discover XSS in Search Functionality

## Summary

This procedure identifies cross-site scripting (XSS) vulnerabilities in web search inputs by testing for HTML tag rendering without sanitization, specifically targeting Reverb.com's marketplace search where user queries are reflected unsafely.

## Description

In vulnerable web applications like Reverb.com, search parameters are often reflected back into the page without proper escaping, allowing attackers to inject HTML that executes in victims' browsers. This procedure involves manual testing via URL manipulation to confirm tag execution, setting the stage for payload crafting. It requires only a web browser and public site access, with outcomes including proof of concept (PoC) rendering that validates the vulnerability for further exploitation like phishing.

## Requirements

1. Web browser (e.g., Chrome or Firefox) with developer tools enabled
2. Public internet access to the target site (Reverb.com)
3. No authentication needed for initial search testing

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization using libraries like DOMPurify to escape HTML in user inputs
- Deploy Content Security Policy (CSP) headers to restrict inline script execution
- Monitor for anomalous HTML in logs and use WAF rules to block tag injections

## Objectives

1. Confirm lack of input sanitization in search queries
2. Verify HTML rendering to enable payload development
3. Establish foundation for reflected XSS exploitation

## Instructions

### Step 1: Navigate to Search Endpoint

**Context**: Access the vulnerable search functionality to prepare for input testing.

Navigate to `https://reverb.com/marketplace` in your browser.

> This loads the main search interface where the `query` parameter can be manipulated.

### Step 2: Inject Basic HTML Tag

**Context**: Test if simple HTML renders without escaping, indicating XSS potential.

Append a test payload to the URL: `https://reverb.com/marketplace?query=<span>Injected Test</span>`.

> Inspect the page source (right-click > Inspect) or rendered view; the `<span>` should appear as a DOM element, not plain text.

### Step 3: Validate Rendering

**Context**: Confirm execution by checking for visual or structural changes.

Use browser dev tools to search the DOM for the injected tag and verify no escaping (e.g., no `&lt;span&gt;`).

> Successful output shows the tag integrated into the search results HTML, proving vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[Discovery]]
